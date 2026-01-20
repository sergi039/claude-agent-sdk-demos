# Claude Agents Catalog

Personal curated collection of Claude Code agents optimized for:
- Trading/Finance applications (Polymarket, Funding Screener, HighProb)
- Next.js/React apps (Inbox Zero, Mail Zero)
- Python backends (FastAPI, Flask)
- Data systems (VSDB, PostgreSQL, Neo4j)
- DevOps (Docker, deployment)

## Structure

```
catalog/
├── SOURCES.md              # All source repositories documented
├── README.md               # This file
│
├── agents/                 # Curated agent files
│   ├── code-quality/       # Reviewers, auditors, testers
│   ├── backend/            # Python, FastAPI, API design
│   ├── frontend/           # Next.js, React, TypeScript
│   ├── data/               # Database, PostgreSQL, Neo4j
│   ├── devops/             # Docker, deployment
│   └── finance/            # FinTech security, trading
│
├── workflows/              # Workflow definitions
└── skills/                 # Custom skills
```

## Quick Start

### View All Sources
See [SOURCES.md](./SOURCES.md) for comprehensive documentation of 12+ repositories.

### Install Agents (Phase 2)
```bash
# Copy all curated agents
cp agents/*/*.md ~/.claude/agents/

# Or selective install
cp agents/code-quality/*.md ~/.claude/agents/
cp agents/backend/*.md ~/.claude/agents/
```

### Install Workflows (Phase 3)
```bash
claude
/plugin marketplace add shinpr/claude-code-workflows
/plugin install dev-workflows@claude-code-workflows
```

## Selected Agents

### Code Quality (Universal)
| Agent | Source | Purpose |
|-------|--------|---------|
| code-reviewer | VoltAgent | Code review before commits |
| security-auditor | VoltAgent | Security vulnerability detection |
| test-automator | VoltAgent | Test generation and coverage |

### Backend (Python)
| Agent | Source | Purpose |
|-------|--------|---------|
| python-pro | VoltAgent | Python best practices |
| fastapi-expert | lst97 | FastAPI patterns |
| api-designer | lst97 | API architecture |

### Frontend (Next.js)
| Agent | Source | Purpose |
|-------|--------|---------|
| nextjs-pro | VoltAgent | Next.js App Router |
| react-architect | supatest-ai | React patterns |
| typescript-pro | VoltAgent | TypeScript typing |

### Data
| Agent | Source | Purpose |
|-------|--------|---------|
| database-optimizer | VoltAgent | Query optimization |
| postgres-pro | lst97 | PostgreSQL expertise |

### DevOps
| Agent | Source | Purpose |
|-------|--------|---------|
| docker-specialist | VoltAgent | Docker/compose |

### Finance
| Agent | Source | Purpose |
|-------|--------|---------|
| fintech-security | supatest-ai | Trading app security |

## Usage Examples

### Code Review
```
"Review my changes in polymarket-kalshi-btc-arbitrage-bot before I commit"
→ Uses code-reviewer + security-auditor
```

### API Design
```
"Design REST API for new arbitrage endpoint between Binance and Bybit"
→ Uses api-designer + backend-architect
```

### Database Optimization
```
"Optimize VSDB queries for searching 50K documents"
→ Uses database-optimizer + postgres-pro
```

### Structured Development (with workflows)
```
/implement add webhook notification for arbitrage alerts
→ Plan → TDD → Implementation → Quality Fix → Review
```

## Customization

### Modify an Agent
1. Copy agent to `~/.claude/agents/`
2. Edit the markdown file
3. Adjust: description, tools, model, prompt

### Create New Agent
```markdown
---
name: my-custom-agent
description: When to use this agent
tools: Read, Write, Edit, Bash
model: sonnet
---

# My Custom Agent

**Role**: What it does
**Expertise**: Technologies

## Instructions
[Your custom prompt]
```

## Project Mapping

| Project | Primary Agents |
|---------|---------------|
| Inbox Zero | nextjs-pro, react-architect, typescript-pro |
| Mail Zero | nextjs-pro, typescript-pro |
| Polymarket Arbitrage | python-pro, security-auditor, fintech-security |
| Funding Screener | python-pro, api-designer |
| HighProb Scanner | python-pro, fastapi-expert |
| VSDB | database-optimizer, postgres-pro |
| IdealistaRank | docker-specialist, postgres-pro |

## Status

- [x] Phase 1: Catalog structure created
- [x] Phase 1: Sources documented
- [ ] Phase 1: Agents curated (in progress)
- [ ] Phase 2: Installation
- [ ] Phase 3: Workflows
- [ ] Phase 4: Iteration
