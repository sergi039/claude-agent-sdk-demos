# Claude Agents Catalog - Project Status

## Description

Персональный каталог курированных Claude Code агентов для оптимизации разработки. Включает:
- Курированную коллекцию лучших субагентов из community репозиториев
- Адаптированные агенты под конкретные проекты (trading, Next.js, Python, DevOps)
- Документацию по источникам и использованию
- Workflows для структурированной разработки

## Goals

1. **Курация** — выбрать лучших агентов из 5+ community репозиториев
2. **Адаптация** — настроить агентов под личные проекты и стек
3. **Документация** — создать понятный каталог с описаниями
4. **Эволюция** — легко добавлять/убирать агентов по мере опыта

## Target Projects

| Категория | Проекты | Нужные агенты |
|-----------|---------|---------------|
| Email/Productivity | Inbox Zero, Mail Zero | nextjs-pro, react-architect, typescript-pro |
| Trading/Finance | Polymarket Arbitrage, Funding Screener, HighProb | python-pro, fastapi-expert, security-auditor, fintech-security |
| Data/AI | VSDB, VS Auto Fresh | database-optimizer, postgres-pro, neo4j-expert |
| DevOps | IdealistaRank, VSDB | docker-specialist, deployment-engineer |
| All | * | code-reviewer, test-automator, api-designer |

---

## Kanban

### TODO
- [ ] Execute iteration cycle quarterly
- [ ] Phase 3: Install shinpr/claude-code-workflows plugin
- [ ] Phase 3: Test /implement command on one project
- [ ] Phase 4: Add custom agents based on experience
- [ ] Phase 4: Remove unused agents
- [ ] Phase 4: Customize prompts for personal style

### IN PROGRESS
(none)

### DONE
- [x] Research agent ecosystem (100+ repos analyzed)
- [x] Analyze personal projects and development patterns
- [x] Design catalog structure
- [x] Create project plan and kanban
- [x] Phase 1: Create catalog structure (SOURCES.md, folders)
- [x] Phase 1: Curate 10-15 key agents (19 agents curated)
- [x] Phase 2: Install selected agents to ~/.claude/agents/ (19 agents installed)
- [x] Phase 2: Test agents on real tasks (see AGENT_TESTS.md)
- [x] Phase 3: Install shinpr/claude-code-workflows plugin (see PLUGIN_INSTALLATION.md)
- [x] Phase 3: Test /implement command (see IMPLEMENT_TEST.md)
- [x] Phase 4: Create iteration guidelines (see ITERATION_GUIDE.md)

---

## Phases

### Phase 1: Create Catalog
**Status:** Complete ✅

Tasks:
1. ✅ Create repository structure
2. ✅ Add SOURCES.md with all discovered repos
3. ✅ Select 10-15 key agents for personal projects (19 agents)
4. ✅ Document each agent's purpose and source

### Phase 2: Initial Installation
**Status:** Complete ✅

Tasks:
1. ✅ Copy selected agents to ~/.claude/agents/ (19 agents installed)
2. ✅ Test on real development tasks (see AGENT_TESTS.md)
3. ✅ Iterate based on results

### Phase 3: Workflows
**Status:** Complete ✅

Tasks:
1. ✅ Install shinpr/claude-code-workflows plugin (see PLUGIN_INSTALLATION.md)
2. ✅ Try /implement on one project (see IMPLEMENT_TEST.md)
3. ✅ Evaluate structured development approach

### Phase 4: Iteration (Ongoing)
**Status:** Guidelines Complete ✅

Tasks:
1. ✅ Add new agents as needed (see ITERATION_GUIDE.md)
2. ✅ Remove unused ones (see ITERATION_GUIDE.md)
3. ✅ Customize prompts (see ITERATION_GUIDE.md)
4. ✅ Share learnings (documentation complete)

---

## Agent Sources (Key Repositories)

| Repository | Agents | Focus | Quality |
|------------|--------|-------|---------|
| VoltAgent/awesome-claude-code-subagents | 100+ | Universal collection | ⭐⭐⭐⭐⭐ |
| lst97/claude-code-sub-agents | 33 | Full-stack + AI/ML | ⭐⭐⭐⭐⭐ |
| supatest-ai/awesome-claude-code-sub-agents | 50+ | Architect consultants | ⭐⭐⭐⭐ |
| shinpr/claude-code-workflows | 15+ | Structured workflows | ⭐⭐⭐⭐⭐ |
| anthropics/skills | 10+ | Official skills | ⭐⭐⭐⭐⭐ |
| 0xfurai/claude-code-subagents | 100+ | Alternative collection | ⭐⭐⭐⭐ |
| wshobson/agents | 100+ | Plugins + orchestrators | ⭐⭐⭐⭐ |

---

## Usage Scenarios

### Scenario 1: Code Review
```
"Review changes in polymarket-kalshi-btc-arbitrage-bot before commit"
→ code-reviewer + security-auditor
```

### Scenario 2: API Design
```
"Design API for new Binance-Bybit arbitrage endpoint"
→ backend-architect + api-designer
```

### Scenario 3: Database Optimization
```
"Optimize queries in VSDB for 50K documents"
→ database-optimizer + postgres-pro
```

### Scenario 4: Structured Development
```
/implement add webhook for new arbitrage opportunities
→ plan → TDD → implementation → quality fix
```

---

## Notes

- **Decision:** Catalog approach chosen over bulk install (avoid conflicts, better curation)
- **Key insight:** Only 15-20 agents needed from 100+ available
- **Next step:** Complete Phase 1, then test before Phase 2

---

*Last updated: 2026-01-23*
