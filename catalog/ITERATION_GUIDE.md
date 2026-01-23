# Agent Iteration Guidelines

> Documentation for Issue #8: Phase 4 - Add/remove agents based on usage

## Overview

This guide provides data-driven criteria for managing your Claude agents inventory. The goal is to maintain an optimal set of agents that maximize productivity while minimizing cognitive overhead.

---

## When to Add Agents

### Criteria

| Trigger | Example | Action |
|---------|---------|--------|
| New project type requires expertise | Starting a Rust project | Add `rust-pro` agent |
| Repetitive tasks could be automated | Manual security reviews | Add `security-auditor` |
| Better agent found in community | Higher quality code-reviewer | Replace existing agent |
| Specific domain expertise needed | ML pipeline work | Add `ml-engineer` |
| Team feedback requests capability | Need better docs | Add `doc-writer` |

### Discovery Sources

1. **Community Repositories:**
   - VoltAgent/awesome-claude-code-subagents
   - lst97/claude-code-sub-agents
   - shinpr/claude-code-workflows

2. **Official Sources:**
   - anthropics/skills
   - Claude Code marketplace

3. **Team Contributions:**
   - Internal agent sharing
   - Project-specific customizations

### Adding Process

```bash
# 1. Review agent quality
cat ~/path/to/new-agent.md

# 2. Test in sandbox project first
# 3. If successful, add to collection
cp new-agent.md ~/.claude/agents/

# 4. Document in SOURCES.md
echo "- new-agent: source_url" >> catalog/SOURCES.md
```

---

## When to Remove Agents

### Criteria

| Trigger | Threshold | Action |
|---------|-----------|--------|
| Unused for extended period | > 2 weeks | Consider removal |
| Duplicates another agent | 80%+ overlap | Remove duplicate |
| Quality doesn't meet expectations | < 3/5 rating | Replace or remove |
| Causes confusion with similar agents | User feedback | Consolidate |
| Outdated for current tech stack | Tech migration | Remove |

### Removal Process

```bash
# 1. Check last usage (if tracking enabled)
grep "agent-name" ~/.claude/logs/*.log

# 2. Verify no dependencies
grep -r "agent-name" ~/.claude/

# 3. Archive before removal
mv ~/.claude/agents/old-agent.md ~/.claude/agents/archive/

# 4. Update documentation
# Remove from SOURCES.md, update PROJECT_STATUS.md
```

### Archival Policy

- Keep removed agents for 30 days in `~/.claude/agents/archive/`
- Document removal reason
- Easy restoration if needed later

---

## When to Customize Agents

### Criteria

| Trigger | Example | Customization |
|---------|---------|---------------|
| Default prompts don't match style | Different code conventions | Modify style guidelines |
| Project-specific requirements | Company security policies | Add custom rules |
| Combine multiple agent capabilities | Need reviewer + security | Create hybrid agent |
| Language/framework specific needs | TypeScript strict mode | Add language rules |
| Team workflow integration | PR template requirements | Add process steps |

### Customization Patterns

#### Pattern 1: Style Overrides

```markdown
# In agent file, add project-specific section:

## Project Overrides

When working on {project_name}:
- Use 2-space indentation
- Prefer functional style
- Follow existing patterns in codebase
```

#### Pattern 2: Additional Rules

```markdown
## Additional Requirements

- All functions must have JSDoc comments
- No console.log in production code
- Tests required for public APIs
```

#### Pattern 3: Agent Composition

```markdown
# hybrid-reviewer.md
---
name: hybrid-reviewer
description: Combined code reviewer and security auditor
tools: Read, Grep, Glob
---

You combine the expertise of:
1. Code Reviewer - quality, maintainability, patterns
2. Security Auditor - vulnerabilities, best practices

Review all code changes for BOTH quality AND security.
```

---

## Usage Tracking

### Metrics to Track

| Metric | How to Measure | Target |
|--------|----------------|--------|
| Invocation frequency | Log analysis | > 1/week for core agents |
| Success rate | User feedback | > 80% helpful |
| Time saved | Self-reported | > 10 min/use |
| Quality impact | Code review feedback | Measurable improvement |

### Simple Tracking Script

```bash
#!/bin/bash
# track_agent_usage.sh

AGENT=$1
DATE=$(date +%Y-%m-%d)
echo "$DATE,$AGENT" >> ~/.claude/agent_usage.csv
```

### Weekly Review

```bash
# Generate usage report
cut -d',' -f2 ~/.claude/agent_usage.csv | sort | uniq -c | sort -rn
```

---

## Decision Matrix

### Keep vs Remove Decision Tree

```
Agent unused for 2+ weeks?
├── Yes → Is it for rare but critical tasks?
│   ├── Yes → Keep (mark as "specialist")
│   └── No → Consider removal
└── No → Keep using

Agent quality < 3/5?
├── Yes → Is there a better alternative?
│   ├── Yes → Replace
│   └── No → Customize or remove
└── No → Keep as-is
```

### Customization vs New Agent

```
Need project-specific behavior?
├── Yes → Is change < 20% of agent?
│   ├── Yes → Customize existing
│   └── No → Create new specialized agent
└── No → Use default agent
```

---

## Current Agent Inventory

### Core Agents (Always Keep)

| Agent | Purpose | Last Updated |
|-------|---------|--------------|
| code-reviewer | Code quality | 2026-01-23 |
| security-auditor | Security review | 2026-01-23 |
| test-automator | Test suggestions | 2026-01-23 |

### Project-Specific Agents

| Agent | Projects | Status |
|-------|----------|--------|
| python-pro | Polymarket, Funding Screener | Active |
| nextjs-pro | Inbox Zero | Active |
| postgres-pro | VSDB | Active |
| trading-bot-specialist | Trading projects | Active |

### Specialist Agents (Rare Use OK)

| Agent | Use Case | Keep Reason |
|-------|----------|-------------|
| docker-specialist | Deployments | Critical when needed |
| fintech-security-expert | Trading security | High stakes |

---

## Quarterly Review Checklist

- [ ] Review usage metrics for all agents
- [ ] Identify unused agents (> 4 weeks)
- [ ] Check for new community agents
- [ ] Update customizations for project changes
- [ ] Archive deprecated agents
- [ ] Update this documentation

---

## Next Actions

Based on Phase 4 guidelines:

1. **Add** agents when new project types emerge
2. **Remove** agents unused for 2+ weeks (after archival)
3. **Customize** agents that don't match project style
4. **Track** usage to make data-driven decisions

---

*Generated: 2026-01-23*
