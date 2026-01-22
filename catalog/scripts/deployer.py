#!/usr/bin/env python3
"""
Deploys agents and skills from catalog to a project.

Usage:
  python deployer.py /path/to/project --profile python-backend
  python deployer.py /path/to/project --auto
  python deployer.py /path/to/project --sync
  python deployer.py /path/to/project --list
"""

import argparse
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path
import yaml

CATALOG_DIR = Path(__file__).parent.parent


def load_profile(profile_name: str) -> dict:
    """Load profile configuration."""
    profile_path = CATALOG_DIR / "profiles" / f"{profile_name}.yaml"
    if not profile_path.exists():
        raise ValueError(f"Profile not found: {profile_name}")
    with open(profile_path) as f:
        return yaml.safe_load(f)


def find_agent(agent_name: str) -> Path:
    """Find agent file in catalog."""
    # Check curated agents by category
    agents_dir = CATALOG_DIR / "agents"
    if agents_dir.exists():
        for category_dir in agents_dir.iterdir():
            if category_dir.is_dir():
                agent_file = category_dir / f"{agent_name}.md"
                if agent_file.exists():
                    return agent_file

    # Check everything-claude-code agents
    ecc_agent = CATALOG_DIR / "everything-claude-code" / "agents" / f"{agent_name}.md"
    if ecc_agent.exists():
        return ecc_agent

    return None


def find_skill(skill_name: str) -> Path:
    """Find skill directory in catalog."""
    # Check skills by source
    skills_dir = CATALOG_DIR / "skills"
    if skills_dir.exists():
        for source in ["vercel", "anthropic"]:
            skill_dir = skills_dir / source / skill_name
            if skill_dir.exists():
                return skill_dir

    # Check everything-claude-code skills
    ecc_skill = CATALOG_DIR / "everything-claude-code" / "skills" / skill_name
    if ecc_skill.exists():
        return ecc_skill

    return None


def deploy_agents(project_path: Path, profile: dict, force: bool = False) -> list:
    """Deploy agents from profile to project."""
    agents_dir = project_path / ".claude" / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)

    deployed = []
    skipped = []

    all_agents = profile["agents"]["core"] + profile["agents"].get("optional", [])

    for agent_name in all_agents:
        src = find_agent(agent_name)
        if src:
            dst = agents_dir / f"{agent_name}.md"
            if not dst.exists() or force:
                shutil.copy(src, dst)
                deployed.append(agent_name)
            else:
                skipped.append(agent_name)
        else:
            print(f"  ⚠️  Agent not found: {agent_name}")

    return deployed, skipped


def deploy_skills(project_path: Path, profile: dict, force: bool = False) -> list:
    """Deploy skills from profile to project."""
    skills_dir = project_path / ".claude" / "skills"
    skills_dir.mkdir(parents=True, exist_ok=True)

    deployed = []
    skipped = []

    for skill_name in profile.get("skills", []):
        src = find_skill(skill_name)
        if src and src.is_dir():
            dst = skills_dir / skill_name
            if not dst.exists() or force:
                if dst.exists():
                    shutil.rmtree(dst)
                shutil.copytree(src, dst)
                deployed.append(skill_name)
            else:
                skipped.append(skill_name)
        else:
            print(f"  ⚠️  Skill not found: {skill_name}")

    return deployed, skipped


def generate_organizer(project_path: Path, profile: dict, deployed_agents: list):
    """Generate customized agent-organizer for project."""
    template = '''---
name: agent-organizer
description: Master orchestrator for {project_name}. Analyzes requests and delegates to specialist agents.
tools: Read, Glob, Grep, Bash, TodoWrite
model: sonnet
---

# Agent Organizer for {project_name}

**Role**: Analyze incoming requests and delegate to the most appropriate specialist agent.

## Project Context

{organizer_context}

## Available Agents

{agents_table}

## Dispatch Protocol

1. **Analyze** the user's request to understand the domain and complexity
2. **Select** the most appropriate agent(s) for the task
3. **Plan** for complex tasks requiring multiple agents
4. **Delegate** using: "Use <agent-name> to <specific task>"
5. **Coordinate** results from multiple agents if needed

## Agent Selection Guide

{selection_guide}

## Rules

{rules}

## Examples

**User**: "Add rate limiting to the API"
**Action**: Use backend-architect to design the approach, then python-pro to implement

**User**: "Why is this query slow?"
**Action**: Use database-optimizer to analyze and suggest improvements

**User**: "Review my changes before I commit"
**Action**: Use code-reviewer for quality, security-auditor for security concerns
'''

    # Build agents table
    agents_table = "| Agent | Expertise |\n|-------|-----------|"
    for agent in deployed_agents:
        agents_table += f"\n| **{agent}** | {agent.replace('-', ' ').title()} |"

    # Build selection guide
    selection_guide = ""
    agent_descriptions = {
        "python-pro": "Python code, refactoring, debugging, new features",
        "backend-architect": "API design, architecture decisions, system design",
        "database-optimizer": "SQL queries, schema design, performance tuning",
        "security-auditor": "Security review, vulnerability detection",
        "code-reviewer": "Code quality, best practices, review",
        "test-automator": "Writing tests, test coverage, TDD",
        "ai-engineer": "LLM integration, prompts, AI pipelines",
        "prompt-engineer": "Prompt optimization, token efficiency",
        "nextjs-pro": "Next.js features, React patterns, App Router",
        "react-pro": "React components, hooks, state management",
        "typescript-pro": "TypeScript types, generics, strict mode",
        "fintech-security": "Financial security, trading safety, API key protection"
    }

    for agent in deployed_agents:
        desc = agent_descriptions.get(agent, f"{agent.replace('-', ' ').title()} tasks")
        selection_guide += f"- **{agent}**: {desc}\n"

    # Build rules
    rules = ""
    for rule in profile.get("rules", []):
        rules += f"- {rule}\n"

    content = template.format(
        project_name=project_path.name,
        organizer_context=profile.get("organizer_context", "General development project."),
        agents_table=agents_table,
        selection_guide=selection_guide,
        rules=rules or "- Follow project conventions\n- Verify work with tests when possible"
    )

    organizer_path = project_path / ".claude" / "agents" / "agent-organizer.md"
    organizer_path.write_text(content)


def create_project_profile(project_path: Path, profile_name: str,
                           deployed_agents: list, deployed_skills: list):
    """Create project profile file for tracking."""
    profile_data = {
        "project": project_path.name,
        "profile": profile_name,
        "created": datetime.now().isoformat(),
        "last_sync": datetime.now().isoformat(),
        "catalog_version": "1.0",
        "deployed_agents": deployed_agents,
        "deployed_skills": deployed_skills,
        "metrics": {
            "total_tasks": 0,
            "accepted": 0,
            "rejected": 0,
            "iterations": 0
        }
    }

    claude_dir = project_path / ".claude"
    claude_dir.mkdir(parents=True, exist_ok=True)

    profile_path = claude_dir / "project-profile.yaml"
    with open(profile_path, "w") as f:
        yaml.dump(profile_data, f, default_flow_style=False, sort_keys=False)


def setup_metrics_directory(project_path: Path):
    """Create metrics directory structure."""
    metrics_dir = project_path / ".claude" / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)

    # Create empty feedback log
    feedback_log = metrics_dir / "feedback.jsonl"
    if not feedback_log.exists():
        feedback_log.touch()


def deploy(project_path: str, profile_name: str, force: bool = False):
    """Main deployment function."""
    path = Path(project_path).resolve()

    if not path.exists():
        print(f"❌ Project path does not exist: {path}")
        return False

    profile = load_profile(profile_name)

    print(f"\n{'='*60}")
    print(f"  DEPLOYING: {profile_name} → {path.name}")
    print(f"{'='*60}")

    # Deploy agents
    print(f"\n📦 Deploying agents...")
    deployed_agents, skipped_agents = deploy_agents(path, profile, force)
    for agent in deployed_agents:
        print(f"   ✅ {agent}")
    for agent in skipped_agents:
        print(f"   ⏭️  {agent} (exists, use --force to overwrite)")

    # Deploy skills
    print(f"\n📚 Deploying skills...")
    deployed_skills, skipped_skills = deploy_skills(path, profile, force)
    for skill in deployed_skills:
        print(f"   ✅ {skill}")
    for skill in skipped_skills:
        print(f"   ⏭️  {skill} (exists, use --force to overwrite)")

    # Generate organizer
    print(f"\n🎯 Generating agent-organizer...")
    all_deployed_agents = deployed_agents + skipped_agents
    generate_organizer(path, profile, all_deployed_agents)
    print(f"   ✅ agent-organizer.md")

    # Create project profile
    print(f"\n📋 Creating project profile...")
    create_project_profile(path, profile_name, all_deployed_agents, deployed_skills + skipped_skills)
    print(f"   ✅ project-profile.yaml")

    # Setup metrics
    print(f"\n📊 Setting up metrics...")
    setup_metrics_directory(path)
    print(f"   ✅ metrics/feedback.jsonl")

    print(f"\n{'='*60}")
    print(f"  ✅ DEPLOYMENT COMPLETE")
    print(f"{'='*60}")
    print(f"\n   Profile: {profile_name}")
    print(f"   Agents:  {len(all_deployed_agents)}")
    print(f"   Skills:  {len(deployed_skills + skipped_skills)}")
    print(f"\n   Location: {path / '.claude'}")
    print(f"\n   Next: Start Claude Code in {path.name} and use agent-organizer")
    print(f"{'='*60}\n")

    return True


def sync_project(project_path: str):
    """Sync existing project with latest catalog."""
    path = Path(project_path).resolve()
    profile_file = path / ".claude" / "project-profile.yaml"

    if not profile_file.exists():
        print(f"❌ No project profile found. Run with --profile first.")
        return False

    with open(profile_file) as f:
        project_profile = yaml.safe_load(f)

    profile_name = project_profile["profile"]
    print(f"🔄 Syncing {path.name} with profile: {profile_name}")

    return deploy(str(path), profile_name, force=True)


def list_available():
    """List available profiles and agents."""
    print(f"\n{'='*60}")
    print(f"  AVAILABLE PROFILES")
    print(f"{'='*60}\n")

    profiles_dir = CATALOG_DIR / "profiles"
    for profile_file in sorted(profiles_dir.glob("*.yaml")):
        with open(profile_file) as f:
            profile = yaml.safe_load(f)
        print(f"  📁 {profile['name']}")
        print(f"     {profile['description']}")
        print(f"     Agents: {', '.join(profile['agents']['core'][:4])}...")
        print()

    print(f"{'='*60}")
    print(f"  AVAILABLE AGENTS")
    print(f"{'='*60}\n")

    agents_dir = CATALOG_DIR / "agents"
    if agents_dir.exists():
        for category_dir in sorted(agents_dir.iterdir()):
            if category_dir.is_dir():
                agents = [f.stem for f in category_dir.glob("*.md")]
                if agents:
                    print(f"  📂 {category_dir.name}/")
                    for agent in sorted(agents):
                        print(f"     • {agent}")
                    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Deploy Claude agents from catalog to project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deployer.py /path/to/project --profile python-backend
  python deployer.py /path/to/project --auto
  python deployer.py /path/to/project --sync
  python deployer.py --list
        """
    )
    parser.add_argument("project", nargs="?", help="Path to project")
    parser.add_argument("--profile", help="Profile name to deploy")
    parser.add_argument("--auto", action="store_true", help="Auto-detect profile")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--sync", action="store_true", help="Sync with latest catalog")
    parser.add_argument("--list", action="store_true", help="List available profiles and agents")

    args = parser.parse_args()

    if args.list:
        list_available()
        sys.exit(0)

    if not args.project:
        parser.print_help()
        sys.exit(1)

    if args.sync:
        success = sync_project(args.project)
        sys.exit(0 if success else 1)

    if args.auto:
        from project_profiler import recommend
        result = recommend(args.project)
        if "error" in result:
            print(f"❌ {result['error']}")
            sys.exit(1)
        profile_name = result["primary_profile"]
        if not profile_name:
            print("❌ Could not auto-detect profile. Specify --profile manually.")
            sys.exit(1)
        print(f"🔍 Auto-detected profile: {profile_name} ({result['confidence']}% match)")
    else:
        profile_name = args.profile

    if not profile_name:
        print("❌ Specify --profile or use --auto")
        parser.print_help()
        sys.exit(1)

    success = deploy(args.project, profile_name, args.force)
    sys.exit(0 if success else 1)
