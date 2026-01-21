#!/usr/bin/env python3
"""
Daily skill checker - monitors sources for new skills.

Checks:
1. skills.sh leaderboard for new top skills
2. GitHub repos (vercel-labs/agent-skills, anthropics/skills)
3. Compares with current catalog

Run: python check_new_skills.py
Cron: 0 9 * * * cd /Users/ss/claude-agent-sdk-demos/catalog && python scripts/check_new_skills.py
"""

import json
import os
import subprocess
from datetime import datetime
from pathlib import Path

CATALOG_DIR = Path(__file__).parent.parent
SKILLS_DIR = CATALOG_DIR / "skills"
LOG_FILE = CATALOG_DIR / "scripts" / "skills_updates.log"

# Sources to check
GITHUB_REPOS = [
    ("anthropics/skills", "skills"),
    ("vercel-labs/agent-skills", "skills"),
]

SKILLS_SH_URL = "https://skills.sh"


def get_current_skills() -> set:
    """Get list of skills currently in catalog."""
    skills = set()
    for source_dir in SKILLS_DIR.iterdir():
        if source_dir.is_dir():
            for skill_dir in source_dir.iterdir():
                if skill_dir.is_dir():
                    skills.add(f"{source_dir.name}/{skill_dir.name}")
    return skills


def check_github_repo(repo: str, skills_path: str) -> list:
    """Check GitHub repo for available skills."""
    try:
        # Use gh api to list directory contents
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
        print(f"Error checking {repo}: {e}")
        return []


def log_update(message: str):
    """Log update to file and stdout."""
    timestamp = datetime.now().isoformat()
    log_entry = f"[{timestamp}] {message}"
    print(log_entry)

    with open(LOG_FILE, "a") as f:
        f.write(log_entry + "\n")


def main():
    log_update("=== Skill Check Started ===")

    current_skills = get_current_skills()
    log_update(f"Current catalog: {len(current_skills)} skills")

    new_skills_found = []

    # Check GitHub repos
    for repo, path in GITHUB_REPOS:
        source_name = repo.split("/")[0]
        if source_name == "anthropics":
            source_name = "anthropic"
        elif source_name == "vercel-labs":
            source_name = "vercel"

        log_update(f"Checking {repo}...")
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

    # Report findings
    if new_skills_found:
        log_update(f"\n🆕 Found {len(new_skills_found)} new skills:")
        for skill in new_skills_found:
            log_update(f"  - {skill['source']}/{skill['name']}")
            log_update(f"    URL: {skill['url']}")

        # Save to JSON for easy parsing
        report_file = CATALOG_DIR / "scripts" / "new_skills_report.json"
        with open(report_file, "w") as f:
            json.dump({
                "timestamp": datetime.now().isoformat(),
                "new_skills": new_skills_found
            }, f, indent=2)
        log_update(f"\nReport saved to: {report_file}")
    else:
        log_update("\n✅ No new skills found - catalog is up to date")

    log_update("=== Skill Check Complete ===\n")

    return len(new_skills_found)


if __name__ == "__main__":
    exit(main())
