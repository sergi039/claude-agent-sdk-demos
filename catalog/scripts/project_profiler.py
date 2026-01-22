#!/usr/bin/env python3
"""
Analyzes a project and recommends the best profile/agents.

Usage:
  python project_profiler.py /path/to/project
  python project_profiler.py /path/to/project --json
"""

import json
import sys
from pathlib import Path
from typing import Optional
import yaml

CATALOG_DIR = Path(__file__).parent.parent


def load_profiles() -> dict:
    """Load all profile configurations."""
    profiles = {}
    profiles_dir = CATALOG_DIR / "profiles"

    if not profiles_dir.exists():
        return profiles

    for profile_file in profiles_dir.glob("*.yaml"):
        with open(profile_file) as f:
            profile = yaml.safe_load(f)
            profiles[profile["name"]] = profile

    return profiles


def read_dependencies(project_path: Path) -> set:
    """Read all dependencies from project files."""
    deps = set()

    # Python: requirements.txt
    req_file = project_path / "requirements.txt"
    if req_file.exists():
        content = req_file.read_text().lower()
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                # Extract package name (before ==, >=, etc.)
                pkg = line.split("==")[0].split(">=")[0].split("<=")[0].split("[")[0].strip()
                if pkg:
                    deps.add(pkg)
                    # Also add normalized names (py-clob-client -> clob, polymarket)
                    if "clob" in pkg or "polymarket" in pkg:
                        deps.add("polymarket")
                    if "kalshi" in pkg:
                        deps.add("kalshi")

    # Python: pyproject.toml
    pyproject = project_path / "pyproject.toml"
    if pyproject.exists():
        content = pyproject.read_text().lower()
        deps.add("__pyproject__")
        # Simple extraction of common packages
        for pkg in ["fastapi", "flask", "django", "sqlalchemy", "anthropic", "openai",
                    "langchain", "pytest", "ccxt", "alpaca", "telethon", "streamlit",
                    "polymarket", "kalshi", "binance", "trading"]:
            if pkg in content:
                deps.add(pkg)

    # Node.js: package.json
    pkg_json = project_path / "package.json"
    if pkg_json.exists():
        try:
            pkg = json.loads(pkg_json.read_text())
            all_deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
            deps.update(k.lower() for k in all_deps.keys())
        except json.JSONDecodeError:
            pass

    return deps


def scan_source_for_trading_indicators(project_path: Path) -> set:
    """Scan source files for trading-related keywords."""
    indicators = set()

    trading_keywords = {
        "polymarket": ["polymarket", "clob", "condition_id", "token_id"],
        "kalshi": ["kalshi", "kalshi_", "trade-api"],
        "arbitrage": ["arbitrage", "edge", "kelly", "position_size"],
        "trading": ["buy_yes", "buy_no", "place_order", "execute_trade"],
        "crypto": ["private_key", "wallet", "polygon", "ethereum"],
    }

    # Scan Python files
    for py_file in list(project_path.rglob("*.py"))[:50]:  # Limit to 50 files
        try:
            content = py_file.read_text().lower()
            for category, keywords in trading_keywords.items():
                if any(kw in content for kw in keywords):
                    indicators.add(category)
        except (UnicodeDecodeError, PermissionError):
            continue

    return indicators


def analyze_structure(project_path: Path) -> dict:
    """Analyze project structure."""
    structure = {
        "has_api": False,
        "has_tests": False,
        "has_docker": False,
        "has_db": False,
        "has_frontend": False,
        "has_backend": False,
        "file_types": set()
    }

    # Check for common directories/files
    if (project_path / "src" / "api").exists() or \
       (project_path / "app" / "api").exists() or \
       (project_path / "pages" / "api").exists() or \
       (project_path / "api").exists():
        structure["has_api"] = True

    if (project_path / "tests").exists() or \
       (project_path / "test").exists() or \
       (project_path / "__tests__").exists():
        structure["has_tests"] = True

    if (project_path / "Dockerfile").exists() or \
       (project_path / "docker-compose.yml").exists() or \
       (project_path / "docker-compose.yaml").exists():
        structure["has_docker"] = True

    if (project_path / "src" / "db").exists() or \
       (project_path / "migrations").exists() or \
       (project_path / "alembic").exists() or \
       (project_path / "prisma").exists():
        structure["has_db"] = True

    if (project_path / "src" / "components").exists() or \
       (project_path / "components").exists() or \
       (project_path / "app").exists():
        structure["has_frontend"] = True

    # Check file types
    for ext in ["py", "ts", "tsx", "js", "jsx"]:
        if list(project_path.rglob(f"*.{ext}"))[:1]:
            structure["file_types"].add(ext)

    structure["file_types"] = list(structure["file_types"])

    return structure


def analyze_project(project_path: Path) -> dict:
    """Full project analysis."""
    result = {
        "path": str(project_path),
        "name": project_path.name,
        "tech_stack": [],
        "frameworks": [],
        "dependencies": [],
        "structure": {},
        "indicators": []
    }

    deps = read_dependencies(project_path)
    result["dependencies"] = sorted(deps)

    # Detect tech stack
    if (project_path / "requirements.txt").exists() or \
       (project_path / "pyproject.toml").exists() or \
       (project_path / "setup.py").exists():
        result["tech_stack"].append("Python")

    if (project_path / "package.json").exists():
        result["tech_stack"].append("Node.js")
        if "typescript" in deps:
            result["tech_stack"].append("TypeScript")

    # Detect frameworks
    framework_map = {
        "fastapi": "FastAPI",
        "flask": "Flask",
        "django": "Django",
        "next": "Next.js",
        "react": "React",
        "vue": "Vue",
        "express": "Express",
        "streamlit": "Streamlit"
    }

    for dep, framework in framework_map.items():
        if dep in deps:
            result["frameworks"].append(framework)

    # Detect indicators from dependencies
    indicator_keywords = [
        "anthropic", "openai", "langchain", "llm", "embedding",
        "ccxt", "alpaca", "trading", "arbitrage", "kalshi", "polymarket",
        "sqlalchemy", "prisma", "drizzle", "postgresql", "mongodb",
        "telethon", "telegram", "discord", "binance", "crypto"
    ]

    for kw in indicator_keywords:
        if kw in deps or any(kw in str(d) for d in deps):
            result["indicators"].append(kw)

    # Scan source code for trading indicators
    source_indicators = scan_source_for_trading_indicators(project_path)
    for ind in source_indicators:
        if ind not in result["indicators"]:
            result["indicators"].append(ind)

    # Analyze structure
    result["structure"] = analyze_structure(project_path)

    return result


def match_profiles(analysis: dict, profiles: dict) -> list:
    """Match project analysis to profiles."""
    matches = []
    deps_set = set(analysis["dependencies"])
    indicators = set(analysis["indicators"])

    for name, profile in profiles.items():
        score = 0
        reasons = []

        # Check required patterns
        required_any = profile.get("tech_patterns", {}).get("required_any", [])
        if required_any:
            # Check if any required file exists
            pass  # Already detected via tech_stack

        # Check indicators
        profile_indicators = set(profile.get("tech_patterns", {}).get("indicators", []))
        matched_indicators = indicators & profile_indicators

        if matched_indicators:
            score += len(matched_indicators) * 20
            reasons.append(f"indicators: {', '.join(matched_indicators)}")

        # Check dependencies
        for ind in profile_indicators:
            if ind in deps_set:
                score += 15

        # Framework bonuses
        if name == "nextjs-frontend" and "Next.js" in analysis["frameworks"]:
            score += 50
            reasons.append("Next.js detected")
        elif name == "python-backend" and "Python" in analysis["tech_stack"]:
            if any(f in analysis["frameworks"] for f in ["FastAPI", "Flask", "Django"]):
                score += 40
                reasons.append("Python web framework")
            else:
                score += 20
                reasons.append("Python project")
        elif name == "trading-fintech":
            trading_indicators = {"ccxt", "alpaca", "trading", "arbitrage", "kalshi", "polymarket", "crypto"}
            matched_trading = indicators & trading_indicators
            if matched_trading:
                # Strong match for trading projects
                score += 30 * len(matched_trading)
                reasons.append(f"trading: {', '.join(matched_trading)}")
        elif name == "ai-ml":
            ai_indicators = {"anthropic", "openai", "langchain", "llm", "embedding"}
            if indicators & ai_indicators:
                score += 50
                reasons.append("AI/ML indicators")
        elif name == "fullstack":
            if "Next.js" in analysis["frameworks"] and analysis["structure"].get("has_db"):
                score += 45
                reasons.append("fullstack patterns")

        if score > 0:
            matches.append({
                "profile": name,
                "score": min(score, 100),
                "reasons": reasons
            })

    return sorted(matches, key=lambda x: x["score"], reverse=True)


def recommend(project_path: str) -> dict:
    """Generate recommendations for a project."""
    path = Path(project_path).resolve()

    if not path.exists():
        return {"error": f"Project path does not exist: {path}"}

    profiles = load_profiles()
    analysis = analyze_project(path)
    matches = match_profiles(analysis, profiles)

    # Get recommended agents from top profile
    recommended_agents = []
    recommended_skills = []

    if matches:
        top_profile = profiles.get(matches[0]["profile"], {})
        agents = top_profile.get("agents", {})
        recommended_agents = agents.get("core", []) + agents.get("optional", [])
        recommended_skills = top_profile.get("skills", [])

    return {
        "project": str(path),
        "name": path.name,
        "analysis": analysis,
        "profile_matches": matches,
        "primary_profile": matches[0]["profile"] if matches else None,
        "confidence": matches[0]["score"] if matches else 0,
        "recommended_agents": recommended_agents,
        "recommended_skills": recommended_skills
    }


def print_report(result: dict):
    """Print human-readable report."""
    print(f"\n{'='*60}")
    print(f"  PROJECT ANALYSIS: {result['name']}")
    print(f"{'='*60}")

    analysis = result["analysis"]

    print(f"\n📁 Path: {result['project']}")
    print(f"\n🔧 Tech Stack: {', '.join(analysis['tech_stack']) or 'Unknown'}")
    print(f"📦 Frameworks: {', '.join(analysis['frameworks']) or 'None detected'}")
    print(f"🔍 Indicators: {', '.join(analysis['indicators'][:5]) or 'None'}")

    structure = analysis["structure"]
    print(f"\n📊 Structure:")
    print(f"   Has API: {'✅' if structure.get('has_api') else '❌'}")
    print(f"   Has Tests: {'✅' if structure.get('has_tests') else '❌'}")
    print(f"   Has Docker: {'✅' if structure.get('has_docker') else '❌'}")
    print(f"   Has Database: {'✅' if structure.get('has_db') else '❌'}")

    print(f"\n🎯 PROFILE RECOMMENDATIONS:")
    print(f"{'─'*60}")

    if result["profile_matches"]:
        for i, match in enumerate(result["profile_matches"][:3]):
            marker = "▶" if i == 0 else " "
            print(f" {marker} {match['profile']:20} {match['score']:3}% - {', '.join(match['reasons'])}")
    else:
        print("   No matching profiles found")

    if result["primary_profile"]:
        print(f"\n✅ Recommended Profile: {result['primary_profile']} ({result['confidence']}% match)")
        print(f"\n📋 Agents to deploy:")
        for agent in result["recommended_agents"]:
            print(f"   • {agent}")
        print(f"\n📚 Skills to deploy:")
        for skill in result["recommended_skills"]:
            print(f"   • {skill}")

    print(f"\n{'='*60}")
    print(f"To deploy: python deployer.py {result['project']} --profile {result['primary_profile']}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python project_profiler.py /path/to/project [--json]")
        sys.exit(1)

    project_path = sys.argv[1]
    output_json = "--json" in sys.argv

    result = recommend(project_path)

    if "error" in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    if output_json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print_report(result)
