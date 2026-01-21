#!/usr/bin/env python3
"""
Daily catalog sync - monitors sources for updates.

Checks:
1. GitHub repos (vercel-labs/agent-skills, anthropics/skills) for new skills
2. affaan-m/everything-claude-code for updates (syncs full repo)

Run: python check_new_skills.py
Cron: 0 9 * * * cd /Users/ss/claude-agent-sdk-demos/catalog && python scripts/check_new_skills.py
"""

import json
import os
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

CATALOG_DIR = Path(__file__).parent.parent
SKILLS_DIR = CATALOG_DIR / "skills"
EVERYTHING_DIR = CATALOG_DIR / "everything-claude-code"
LOG_FILE = CATALOG_DIR / "scripts" / "sync_updates.log"
TEMP_DIR = Path("/tmp")

# Skills repos to check for new skills
SKILLS_REPOS = [
    ("anthropics/skills", "skills"),
    ("vercel-labs/agent-skills", "skills"),
]

# Full repos to sync (copy all updates)
SYNC_REPOS = [
    {
        "repo": "affaan-m/everything-claude-code",
        "local_dir": EVERYTHING_DIR,
        "dirs_to_sync": ["agents", "commands", "contexts", "examples", "hooks", "mcp-configs", "rules", "skills", "plugins"],
        "files_to_sync": ["README.md", "CONTRIBUTING.md"]
    }
]


def log_update(message: str):
    """Log update to file and stdout."""
    timestamp = datetime.now().isoformat()
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)

    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")


def get_current_skills() -> set:
    """Get list of skills currently in catalog."""
    skills = set()
    if not SKILLS_DIR.exists():
        return skills
    for source_dir in SKILLS_DIR.iterdir():
        if source_dir.is_dir():
            for skill_dir in source_dir.iterdir():
                if skill_dir.is_dir():
                    skills.add(f"{source_dir.name}/{skill_dir.name}")
    return skills


def check_github_repo(repo: str, skills_path: str) -> list:
    """Check GitHub repo for available skills."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/contents/{skills_path}"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            return []

        contents = json.loads(result.stdout)
        return [item["name"] for item in contents if item["type"] == "dir"]
    except Exception as e:
        log_update(f"Error checking {repo}: {e}")
        return []


def get_repo_last_commit(repo: str) -> str:
    """Get last commit SHA for a repo."""
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{repo}/commits/main", "--jq", ".sha"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout.strip()[:7]
    except Exception:
        pass
    return ""


def sync_full_repo(config: dict) -> dict:
    """Sync a full repository to local catalog."""
    repo = config["repo"]
    local_dir = config["local_dir"]

    log_update(f"Syncing {repo}...")

    # Clone to temp
    temp_clone = TEMP_DIR / repo.replace("/", "-")
    if temp_clone.exists():
        shutil.rmtree(temp_clone)

    result = subprocess.run(
        ["git", "clone", "--depth", "1", f"https://github.com/{repo}.git", str(temp_clone)],
        capture_output=True,
        text=True,
        timeout=120
    )

    if result.returncode != 0:
        log_update(f"  ❌ Failed to clone {repo}")
        return {"repo": repo, "status": "error", "changes": []}

    changes = []

    # Sync directories
    for dir_name in config.get("dirs_to_sync", []):
        src = temp_clone / dir_name
        dst = local_dir / dir_name

        if src.exists():
            if dst.exists():
                # Compare and report changes
                src_files = set(f.name for f in src.rglob("*") if f.is_file())
                dst_files = set(f.name for f in dst.rglob("*") if f.is_file())
                new_files = src_files - dst_files
                if new_files:
                    changes.extend([f"{dir_name}/{f}" for f in new_files])

            # Remove old and copy new
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)

    # Sync individual files
    for file_name in config.get("files_to_sync", []):
        src = temp_clone / file_name
        dst = local_dir / file_name

        if src.exists():
            # Check if file changed
            if dst.exists():
                with open(src) as f1, open(dst) as f2:
                    if f1.read() != f2.read():
                        changes.append(file_name)
            else:
                changes.append(file_name)

            shutil.copy2(src, dst)

    # Cleanup temp
    shutil.rmtree(temp_clone, ignore_errors=True)

    commit = get_repo_last_commit(repo)

    if changes:
        log_update(f"  ✅ Synced {repo} ({commit}) - {len(changes)} changes")
        for change in changes[:10]:
            log_update(f"    + {change}")
        if len(changes) > 10:
            log_update(f"    ... and {len(changes) - 10} more")
    else:
        log_update(f"  ✅ {repo} ({commit}) - no changes")

    return {"repo": repo, "status": "synced", "commit": commit, "changes": changes}


def check_new_skills() -> list:
    """Check for new skills in skills repos."""
    current_skills = get_current_skills()
    new_skills_found = []

    for repo, path in SKILLS_REPOS:
        source_name = repo.split("/")[0]
        if source_name == "anthropics":
            source_name = "anthropic"
        elif source_name == "vercel-labs":
            source_name = "vercel"

        log_update(f"Checking {repo} for new skills...")
        remote_skills = check_github_repo(repo, path)

        for skill_name in remote_skills:
            catalog_key = f"{source_name}/{skill_name}"
            if catalog_key not in current_skills:
                new_skills_found.append({
                    "source": source_name,
                    "name": skill_name,
                    "repo": repo,
                    "url": f"https://github.com/{repo}/tree/main/{path}/{skill_name}"
                })

    return new_skills_found


def main():
    log_update("=" * 50)
    log_update("=== Daily Catalog Sync Started ===")
    log_update("=" * 50)

    results = {
        "timestamp": datetime.now().isoformat(),
        "new_skills": [],
        "synced_repos": []
    }

    # 1. Sync full repos (everything-claude-code)
    log_update("\n📦 Syncing full repositories...")
    for config in SYNC_REPOS:
        sync_result = sync_full_repo(config)
        results["synced_repos"].append(sync_result)

    # 2. Check for new skills
    log_update("\n🔍 Checking for new skills...")
    new_skills = check_new_skills()
    results["new_skills"] = new_skills

    if new_skills:
        log_update(f"\n🆕 Found {len(new_skills)} new skills:")
        for skill in new_skills:
            log_update(f"  - {skill['source']}/{skill['name']}")
            log_update(f"    URL: {skill['url']}")
    else:
        log_update("\n✅ No new skills found")

    # Save report
    report_file = CATALOG_DIR / "scripts" / "sync_report.json"
    with open(report_file, "w") as f:
        json.dump(results, f, indent=2)

    log_update(f"\n📄 Report saved to: {report_file}")
    log_update("=== Daily Catalog Sync Complete ===\n")

    # Return count of changes for exit code
    total_changes = len(new_skills) + sum(
        len(r.get("changes", [])) for r in results["synced_repos"]
    )
    return total_changes


if __name__ == "__main__":
    exit(main())
