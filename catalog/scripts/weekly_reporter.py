#!/usr/bin/env python3
"""
Generates weekly performance reports for Claude Code agent usage.

Usage:
  python weekly_reporter.py /path/to/project
  python weekly_reporter.py --all
  python weekly_reporter.py --all --output report.md
"""

import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import yaml

CATALOG_DIR = Path(__file__).parent.parent
TRACKED_PROJECTS_DIR = Path("/Users/ss")


def find_tracked_projects() -> list:
    """Find all projects with .claude/project-profile.yaml."""
    projects = []

    for item in TRACKED_PROJECTS_DIR.iterdir():
        if item.is_dir():
            profile = item / ".claude" / "project-profile.yaml"
            if profile.exists():
                projects.append(item)

    return sorted(projects, key=lambda x: x.name)


def load_feedback(project_path: Path, days: int = 7) -> list:
    """Load feedback entries from the last N days."""
    log_file = project_path / ".claude" / "metrics" / "feedback.jsonl"

    if not log_file.exists():
        return []

    cutoff = datetime.now() - timedelta(days=days)
    entries = []

    with open(log_file) as f:
        for line in f:
            if line.strip():
                try:
                    entry = json.loads(line)
                    entry_time = datetime.fromisoformat(entry["ts"])
                    if entry_time > cutoff:
                        entries.append(entry)
                except (json.JSONDecodeError, KeyError):
                    continue

    return entries


def load_project_profile(project_path: Path) -> dict:
    """Load project profile."""
    profile_file = project_path / ".claude" / "project-profile.yaml"

    if not profile_file.exists():
        return {}

    with open(profile_file) as f:
        return yaml.safe_load(f)


def calculate_agent_stats(entries: list) -> dict:
    """Calculate per-agent statistics."""
    stats = defaultdict(lambda: {
        "total": 0,
        "accepted": 0,
        "rejected": 0,
        "iterations": 0,
        "total_iterations": 0,
        "reasons": defaultdict(int)
    })

    for entry in entries:
        agent = entry["agent"]
        s = stats[agent]
        s["total"] += 1
        s["total_iterations"] += entry.get("iterations", 1)

        if entry["outcome"] == "accepted":
            s["accepted"] += 1
        elif entry["outcome"] == "rejected":
            s["rejected"] += 1
            if entry.get("reason"):
                s["reasons"][entry["reason"]] += 1
        elif entry["outcome"] == "iteration":
            s["iterations"] += 1

    # Calculate rates
    for agent, s in stats.items():
        if s["total"] > 0:
            s["acceptance_rate"] = round((s["accepted"] / s["total"]) * 100, 1)
            s["avg_iterations"] = round(s["total_iterations"] / s["total"], 2)
        s["reasons"] = dict(s["reasons"])

    return dict(stats)


def generate_project_report(project_path: Path, days: int = 7) -> dict:
    """Generate report for a single project."""
    profile = load_project_profile(project_path)
    entries = load_feedback(project_path, days)
    agent_stats = calculate_agent_stats(entries)

    # Overall stats
    total_tasks = len(entries)
    total_accepted = sum(s["accepted"] for s in agent_stats.values())
    total_rejected = sum(s["rejected"] for s in agent_stats.values())

    return {
        "project": project_path.name,
        "path": str(project_path),
        "profile": profile.get("profile", "unknown"),
        "period_days": days,
        "period_start": (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d"),
        "period_end": datetime.now().strftime("%Y-%m-%d"),
        "total_tasks": total_tasks,
        "total_accepted": total_accepted,
        "total_rejected": total_rejected,
        "overall_acceptance_rate": round((total_accepted / total_tasks * 100) if total_tasks > 0 else 0, 1),
        "agent_stats": agent_stats,
        "deployed_agents": profile.get("deployed_agents", []),
        "deployed_skills": profile.get("deployed_skills", [])
    }


def format_report_text(report: dict) -> str:
    """Format report as text."""
    lines = []

    lines.append("═" * 70)
    lines.append(f"  WEEKLY PERFORMANCE REPORT: {report['project']}")
    lines.append(f"  Profile: {report['profile']}")
    lines.append(f"  Period: {report['period_start']} to {report['period_end']}")
    lines.append("═" * 70)

    if report["total_tasks"] == 0:
        lines.append("\n  📊 No activity recorded in this period.")
        lines.append("\n  To log feedback, use:")
        lines.append(f"    python metrics_collector.py {report['path']} --agent <name> --task <desc> --outcome accepted")
        lines.append("═" * 70)
        return "\n".join(lines)

    lines.append(f"\n  SUMMARY")
    lines.append(f"  ─────────────────────────────────────────")
    lines.append(f"  Total Tasks:      {report['total_tasks']}")
    lines.append(f"  Accepted:         {report['total_accepted']} ({report['overall_acceptance_rate']}%)")
    lines.append(f"  Rejected:         {report['total_rejected']}")

    lines.append(f"\n  AGENT PERFORMANCE")
    lines.append(f"  ─────────────────────────────────────────")
    lines.append(f"  {'Agent':<25} {'Accept%':>8} {'Tasks':>6} {'Avg Iter':>10}")
    lines.append(f"  {'-'*25} {'-'*8} {'-'*6} {'-'*10}")

    for agent, stats in sorted(report["agent_stats"].items(),
                               key=lambda x: x[1]["acceptance_rate"],
                               reverse=True):
        rate = stats["acceptance_rate"]
        total = stats["total"]
        avg_iter = stats["avg_iterations"]

        if rate >= 80:
            indicator = "✅"
        elif rate >= 60:
            indicator = "⚠️ "
        else:
            indicator = "❌"

        lines.append(f"  {indicator}{agent:<23} {rate:>7.1f}% {total:>6} {avg_iter:>10.2f}")

    # Rejection reasons
    all_reasons = defaultdict(int)
    for stats in report["agent_stats"].values():
        for reason, count in stats.get("reasons", {}).items():
            all_reasons[reason] += count

    if all_reasons:
        lines.append(f"\n  REJECTION REASONS")
        lines.append(f"  ─────────────────────────────────────────")
        for reason, count in sorted(all_reasons.items(), key=lambda x: x[1], reverse=True):
            lines.append(f"    • {reason}: {count}")

    # Recommendations
    lines.append(f"\n  RECOMMENDATIONS")
    lines.append(f"  ─────────────────────────────────────────")

    recommendations = []
    for agent, stats in report["agent_stats"].items():
        if stats["total"] >= 3:
            rate = stats["acceptance_rate"]
            if rate < 60:
                recommendations.append(f"  ❌ {agent}: Very low acceptance ({rate}%) - consider reviewing task specifications or agent configuration")
            elif rate < 80:
                recommendations.append(f"  ⚠️  {agent}: Below target ({rate}%) - may need clearer prompts")
            elif rate >= 90:
                recommendations.append(f"  ✅ {agent}: Excellent performance ({rate}%)")

    if recommendations:
        lines.extend(recommendations)
    else:
        lines.append("  No specific recommendations - keep monitoring for more data")

    # Unused agents
    used_agents = set(report["agent_stats"].keys())
    deployed_agents = set(report["deployed_agents"])
    unused = deployed_agents - used_agents - {"agent-organizer"}

    if unused:
        lines.append(f"\n  UNUSED AGENTS (consider removing or training)")
        lines.append(f"  ─────────────────────────────────────────")
        for agent in sorted(unused):
            lines.append(f"    • {agent}")

    lines.append("\n" + "═" * 70)

    return "\n".join(lines)


def format_report_markdown(report: dict) -> str:
    """Format report as Markdown."""
    lines = []

    lines.append(f"# Weekly Report: {report['project']}")
    lines.append(f"\n**Profile:** {report['profile']}")
    lines.append(f"**Period:** {report['period_start']} to {report['period_end']}")
    lines.append("")

    if report["total_tasks"] == 0:
        lines.append("*No activity recorded in this period.*")
        return "\n".join(lines)

    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total Tasks | {report['total_tasks']} |")
    lines.append(f"| Accepted | {report['total_accepted']} ({report['overall_acceptance_rate']}%) |")
    lines.append(f"| Rejected | {report['total_rejected']} |")
    lines.append("")

    lines.append("## Agent Performance")
    lines.append("")
    lines.append("| Agent | Acceptance | Tasks | Avg Iterations |")
    lines.append("|-------|------------|-------|----------------|")

    for agent, stats in sorted(report["agent_stats"].items(),
                               key=lambda x: x[1]["acceptance_rate"],
                               reverse=True):
        rate = stats["acceptance_rate"]
        total = stats["total"]
        avg_iter = stats["avg_iterations"]
        emoji = "✅" if rate >= 80 else "⚠️" if rate >= 60 else "❌"
        lines.append(f"| {emoji} {agent} | {rate}% | {total} | {avg_iter:.2f} |")

    lines.append("")

    return "\n".join(lines)


def generate_all_reports(days: int = 7, output_format: str = "text") -> str:
    """Generate reports for all tracked projects."""
    projects = find_tracked_projects()

    if not projects:
        return "No tracked projects found."

    all_lines = []
    all_lines.append("\n" + "═" * 70)
    all_lines.append("  CLAUDE AGENTS CATALOG - WEEKLY REPORT")
    all_lines.append(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    all_lines.append(f"  Projects tracked: {len(projects)}")
    all_lines.append("═" * 70 + "\n")

    for project in projects:
        report = generate_project_report(project, days)
        if output_format == "markdown":
            all_lines.append(format_report_markdown(report))
        else:
            all_lines.append(format_report_text(report))
        all_lines.append("")

    return "\n".join(all_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate weekly performance reports")
    parser.add_argument("project", nargs="?", help="Path to project (or use --all)")
    parser.add_argument("--all", action="store_true", help="Generate reports for all tracked projects")
    parser.add_argument("--days", type=int, default=7, help="Number of days to include")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--format", choices=["text", "markdown", "json"], default="text",
                        help="Output format")

    args = parser.parse_args()

    if args.all:
        output = generate_all_reports(args.days, args.format)
    elif args.project:
        project_path = Path(args.project).resolve()
        report = generate_project_report(project_path, args.days)

        if args.format == "json":
            output = json.dumps(report, indent=2, default=str)
        elif args.format == "markdown":
            output = format_report_markdown(report)
        else:
            output = format_report_text(report)
    else:
        parser.print_help()
        exit(1)

    if args.output:
        Path(args.output).write_text(output)
        print(f"Report saved to: {args.output}")
    else:
        print(output)
