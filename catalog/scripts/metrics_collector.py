#!/usr/bin/env python3
"""
Metrics collector for Claude Code agent interactions.

This script can be called from hooks or manually to log feedback.

Usage:
  # Log accepted task
  python metrics_collector.py /path/to/project --agent python-pro --task "refactor auth" --outcome accepted

  # Log rejected task
  python metrics_collector.py /path/to/project --agent python-pro --task "add feature" --outcome rejected --reason "wrong approach"

  # Log iteration
  python metrics_collector.py /path/to/project --agent python-pro --task "fix bug" --outcome iteration

  # Show summary
  python metrics_collector.py /path/to/project --summary
"""

import argparse
import json
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path


def log_feedback(project_path: str, agent: str, task: str, outcome: str,
                 iterations: int = 1, reason: str = None, tokens: int = None):
    """Log feedback to project metrics."""
    path = Path(project_path).resolve()
    metrics_dir = path / ".claude" / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)

    log_file = metrics_dir / "feedback.jsonl"

    entry = {
        "ts": datetime.now().isoformat(),
        "agent": agent,
        "task": task[:200],  # truncate long tasks
        "outcome": outcome,  # accepted, rejected, iteration
        "iterations": iterations
    }

    if reason:
        entry["reason"] = reason
    if tokens:
        entry["tokens"] = tokens

    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")

    print(f"✅ Logged: {agent} | {outcome} | {task[:50]}...")


def load_feedback(project_path: str, days: int = 7) -> list:
    """Load feedback entries from the last N days."""
    path = Path(project_path).resolve()
    log_file = path / ".claude" / "metrics" / "feedback.jsonl"

    if not log_file.exists():
        return []

    cutoff = datetime.now() - timedelta(days=days)
    entries = []

    with open(log_file) as f:
        for line in f:
            if line.strip():
                entry = json.loads(line)
                entry_time = datetime.fromisoformat(entry["ts"])
                if entry_time > cutoff:
                    entries.append(entry)

    return entries


def calculate_stats(entries: list) -> dict:
    """Calculate statistics from feedback entries."""
    if not entries:
        return {"total": 0, "agents": {}}

    agent_stats = defaultdict(lambda: {
        "total": 0,
        "accepted": 0,
        "rejected": 0,
        "iterations": 0,
        "total_iterations": 0,
        "reasons": defaultdict(int)
    })

    for entry in entries:
        agent = entry["agent"]
        stats = agent_stats[agent]
        stats["total"] += 1
        stats["total_iterations"] += entry.get("iterations", 1)

        if entry["outcome"] == "accepted":
            stats["accepted"] += 1
        elif entry["outcome"] == "rejected":
            stats["rejected"] += 1
            if entry.get("reason"):
                stats["reasons"][entry["reason"]] += 1
        elif entry["outcome"] == "iteration":
            stats["iterations"] += 1

    # Calculate rates
    for agent, stats in agent_stats.items():
        if stats["total"] > 0:
            stats["acceptance_rate"] = round((stats["accepted"] / stats["total"]) * 100, 1)
            stats["avg_iterations"] = round(stats["total_iterations"] / stats["total"], 2)
        else:
            stats["acceptance_rate"] = 0
            stats["avg_iterations"] = 0

        # Convert reasons to regular dict
        stats["reasons"] = dict(stats["reasons"])

    return {
        "total": len(entries),
        "period_days": 7,
        "agents": dict(agent_stats)
    }


def print_summary(project_path: str, days: int = 7):
    """Print summary of feedback metrics."""
    path = Path(project_path).resolve()
    entries = load_feedback(str(path), days)
    stats = calculate_stats(entries)

    print(f"\n{'='*60}")
    print(f"  METRICS SUMMARY: {path.name}")
    print(f"  Period: Last {days} days | Total interactions: {stats['total']}")
    print(f"{'='*60}")

    if not stats["agents"]:
        print("\n  No feedback data found.")
        print(f"  Start logging with: python metrics_collector.py {path} --agent <name> --task <desc> --outcome <accepted|rejected>")
        print(f"\n{'='*60}\n")
        return

    print(f"\n  AGENT PERFORMANCE:")
    print(f"  {'Agent':<25} {'Accept%':>8} {'Tasks':>6} {'Avg Iter':>10}")
    print(f"  {'-'*25} {'-'*8} {'-'*6} {'-'*10}")

    for agent, agent_stats in sorted(stats["agents"].items(),
                                     key=lambda x: x[1]["acceptance_rate"],
                                     reverse=True):
        rate = agent_stats["acceptance_rate"]
        total = agent_stats["total"]
        avg_iter = agent_stats["avg_iterations"]

        # Color indicator
        if rate >= 80:
            indicator = "✅"
        elif rate >= 60:
            indicator = "⚠️"
        else:
            indicator = "❌"

        print(f"  {indicator} {agent:<23} {rate:>7.1f}% {total:>6} {avg_iter:>10.2f}")

    # Show rejection reasons if any
    all_reasons = defaultdict(int)
    for agent_stats in stats["agents"].values():
        for reason, count in agent_stats.get("reasons", {}).items():
            all_reasons[reason] += count

    if all_reasons:
        print(f"\n  REJECTION REASONS:")
        for reason, count in sorted(all_reasons.items(), key=lambda x: x[1], reverse=True):
            print(f"    • {reason}: {count}")

    print(f"\n{'='*60}\n")


def update_project_profile(project_path: str):
    """Update project profile with latest metrics."""
    path = Path(project_path).resolve()
    profile_file = path / ".claude" / "project-profile.yaml"

    if not profile_file.exists():
        return

    import yaml

    with open(profile_file) as f:
        profile = yaml.safe_load(f)

    entries = load_feedback(str(path), days=30)
    stats = calculate_stats(entries)

    # Update metrics
    total_accepted = sum(a["accepted"] for a in stats["agents"].values())
    total_tasks = stats["total"]

    profile["metrics"] = {
        "total_tasks": total_tasks,
        "accepted": total_accepted,
        "rejected": sum(a["rejected"] for a in stats["agents"].values()),
        "acceptance_rate": round((total_accepted / total_tasks * 100) if total_tasks > 0 else 0, 1),
        "last_updated": datetime.now().isoformat()
    }

    with open(profile_file, "w") as f:
        yaml.dump(profile, f, default_flow_style=False, sort_keys=False)

    print(f"✅ Updated project profile metrics")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect and analyze Claude Code metrics")
    parser.add_argument("project", help="Path to project")
    parser.add_argument("--agent", help="Agent name")
    parser.add_argument("--task", help="Task description")
    parser.add_argument("--outcome", choices=["accepted", "rejected", "iteration"],
                        help="Task outcome")
    parser.add_argument("--reason", help="Rejection reason")
    parser.add_argument("--iterations", type=int, default=1, help="Number of iterations")
    parser.add_argument("--tokens", type=int, help="Tokens used")
    parser.add_argument("--summary", action="store_true", help="Show metrics summary")
    parser.add_argument("--days", type=int, default=7, help="Days to include in summary")
    parser.add_argument("--update-profile", action="store_true", help="Update project profile")

    args = parser.parse_args()

    if args.summary:
        print_summary(args.project, args.days)
    elif args.update_profile:
        update_project_profile(args.project)
    elif args.agent and args.task and args.outcome:
        log_feedback(
            args.project,
            args.agent,
            args.task,
            args.outcome,
            args.iterations,
            args.reason,
            args.tokens
        )
    else:
        parser.print_help()
