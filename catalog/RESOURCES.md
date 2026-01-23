# Claude Code Resources Directory

Comprehensive guide to resources, tools, and communities for optimizing Claude Code workflow.

Last updated: 2026-01-23

---

## Quick Links

| Category | Top Resource | URL |
|----------|--------------|-----|
| **All-in-One** | everything-claude-code | [github.com/affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) |
| **Awesome Lists** | awesome-claude-code | [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) |
| **Skills** | Skills Marketplace | [skills.sh](https://skills.sh) |
| **MCP Servers** | Smithery | [smithery.ai](https://smithery.ai/) |
| **Learning** | DeepLearning.AI Course | [learn.deeplearning.ai](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant) |
| **Community** | Anthropic Discord | [discord.com/invite/prcdpx7qMm](https://discord.com/invite/prcdpx7qMm) |
| **Docs** | Official Docs | [code.claude.com/docs](https://code.claude.com/docs/en) |

---

## 1. Awesome Lists (Curated Collections)

### Primary Lists

| Repository | Stars | Focus | URL |
|------------|-------|-------|-----|
| **hesreallyhim/awesome-claude-code** | 18K+ | Skills, hooks, commands, plugins | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) |
| **jqueryscript/awesome-claude-code** | - | Tools, IDE integrations, frameworks | [GitHub](https://github.com/jqueryscript/awesome-claude-code) |
| **ComposioHQ/awesome-claude-skills** | 21K | Skills & workflow customization | [GitHub](https://github.com/ComposioHQ/awesome-claude-skills) |
| **travisvn/awesome-claude-skills** | - | Skills architecture patterns | [GitHub](https://github.com/travisvn/awesome-claude-skills) |
| **vincenthopf/claude-code** | - | Commands, CLAUDE.md, workflows | [GitHub](https://github.com/vincenthopf/claude-code) |

### Complete Configuration Bundles

| Repository | Stars | Description | URL |
|------------|-------|-------------|-----|
| **affaan-m/everything-claude-code** | 10.2K | Anthropic hackathon winner. All-in-one: agents, skills, commands, rules, hooks, MCP configs. 10+ months of production use. | [GitHub](https://github.com/affaan-m/everything-claude-code) |

**everything-claude-code** содержит:
- **Agents** (9): planner, architect, code-reviewer, security-reviewer, e2e-runner, build-error-resolver, doc-updater, refactor-cleaner, tdd-guide
- **Skills** (9): coding-standards, backend/frontend-patterns, clickhouse-io, continuous-learning, eval-harness, strategic-compact, verification-loop
- **Commands** (15): /tdd, /plan, /e2e, /code-review, /build-fix, /checkpoint, /eval, /orchestrate, /setup-pm, /verify, и др.
- **Rules**: security, coding style, testing, git workflows
- **Hooks**: PreToolUse, PostToolUse, Stop hooks, memory-persistence, strategic-compact
- **MCP Configs**: GitHub, Supabase, Vercel, Railway

### Subagent Collections

| Repository | Agents | Best For |
|------------|--------|----------|
| **VoltAgent/awesome-claude-code-subagents** | 100+ | Universal starter pack |
| **lst97/claude-code-sub-agents** | 33 | Full-stack + AI/ML |
| **supatest-ai/awesome-claude-code-sub-agents** | 50+ | Architecture consulting |

---

## 2. Skills & Plugins

### Skills Marketplaces

| Platform | Description | URL |
|----------|-------------|-----|
| **Skills.sh** | Vercel-hosted skills directory, 24K+ installs top skills | [skills.sh](https://skills.sh) |
| **Anthropic Skills** | Official skills (16 skills) | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| **Vercel Skills** | React best practices, web design, claude.ai | [github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |

### Top Skills by Installs

| Skill | Installs | Description |
|-------|----------|-------------|
| react-best-practices | 24.9K | 40+ React/Next.js optimization rules |
| web-design-guidelines | 18.7K | Web design patterns & accessibility |
| remotion-best-practices | 1.7K | Video generation with Remotion |

### Local Catalog Skills (catalog/skills/)

#### Anthropic Skills (15)

| Skill | Description | Features |
|-------|-------------|----------|
| **algorithmic-art** | Генерация алгоритмического искусства | JS templates, HTML viewer |
| **brand-guidelines** | Работа с брендбуками | Style guides |
| **canvas-design** | Canvas-based дизайн | 50+ шрифтов (.ttf) |
| **doc-coauthoring** | Совместное редактирование документов | Collaboration patterns |
| **docx** | Word документы | OOXML schemas, docx-js, Python scripts |
| **frontend-design** | Frontend дизайн паттерны | UI/UX guidelines |
| **internal-comms** | Внутренние коммуникации | 4 примера (newsletter, FAQ, updates) |
| **mcp-builder** | Создание MCP серверов | Python/Node templates, evaluation |
| **pdf** | PDF генерация и формы | 8 Python scripts, form filling |
| **pptx** | PowerPoint презентации | html2pptx, OOXML, thumbnails |
| **skill-creator** | Создание новых skills | Templates, validation |
| **theme-factory** | Темы оформления | 10 готовых тем (arctic, botanical, etc.) |
| **web-artifacts-builder** | Сборка веб-артефактов | shadcn components, bundler |
| **webapp-testing** | Тестирование веб-приложений | Playwright, automation examples |
| **xlsx** | Excel spreadsheets | Recalc formulas, Python |

#### Vercel Skills (3)

| Skill | Description | Features |
|-------|-------------|----------|
| **react-best-practices** | React/Next.js оптимизация | 40+ правил в 7 категориях |
| **web-design-guidelines** | Web design patterns | Accessibility, responsive |
| **claude.ai** | Деплой на Vercel | claimable deploy script |

#### everything-claude-code Skills (9)

| Skill | Description |
|-------|-------------|
| **backend-patterns** | Backend architecture patterns |
| **coding-standards** | Coding style & conventions |
| **frontend-patterns** | Frontend architecture patterns |
| **clickhouse-io** | ClickHouse database patterns |
| **continuous-learning** | Continuous learning methodology |
| **eval-harness** | Evaluation framework |
| **strategic-compact** | Strategic context compaction |
| **verification-loop** | Verification loop patterns |
| **project-guidelines-example** | Project guidelines template |

### Plugin Collections

| Repository | Features |
|------------|----------|
| **wshobson/agents** | 100 agents, 15 workflows, 110 skills, 76 tools |
| **CloudAI-X/claude-workflow-v2** | 17 commands, 10 skills, 9 hooks |

---

## 3. MCP Servers & Integrations

### MCP Directories

| Platform | Servers | Description | URL |
|----------|---------|-------------|-----|
| **Smithery** | 1000+ | Largest open MCP marketplace | [smithery.ai](https://smithery.ai/) |
| **MCP.so** | 17K+ | Community-driven directory | [mcp.so](https://mcp.so/) |
| **MCPcat** | - | Guides & best servers | [mcpcat.io](https://mcpcat.io/guides/best-mcp-servers-for-claude-code/) |
| **Glama** | 4700+ | AI workspace with MCP hosting | [glama.ai](https://glama.ai/) |

### Essential MCP Servers

| Server | Purpose |
|--------|---------|
| **GitHub MCP** | Repos, PRs, issues, CI/CD |
| **PostgreSQL MCP** | Natural language DB queries |
| **Notion MCP** | Workspace integration |
| **Brave Search MCP** | Web search during coding |
| **Figma Dev Mode MCP** | Design-to-code workflows |
| **Puppeteer MCP** | Browser automation |

### MCP Tools

| Tool | Description | URL |
|------|-------------|-----|
| **Smithery CLI** | Registry installer & manager | [mcpmarket.com](https://mcpmarket.com/server/smithery-cli) |
| **MCP Tool Search** | Dynamic tool loading (95% context reduction) | Built-in |

---

## 4. Hooks & Automation

### Hook Libraries

| Repository | Features | URL |
|------------|----------|-----|
| **decider/claude-hooks** | Clean code validation, quality checks | [GitHub](https://github.com/decider/claude-hooks) |
| **disler/claude-code-hooks-mastery** | All 8 hook lifecycle events | [GitHub](https://github.com/disler/claude-code-hooks-mastery) |
| **disler/claude-code-hooks-multi-agent-observability** | Real-time agent monitoring | [GitHub](https://github.com/disler/claude-code-hooks-multi-agent-observability) |
| **carlrannaberg/claudekit** | File protection, utilities | [GitHub](https://github.com/carlrannaberg/claudekit) |

### Popular Hooks

| Hook | Purpose |
|------|---------|
| **Britfix** | American → British spelling conversion |
| **CC Notify** | Desktop notifications |
| **cchooks** | Python SDK for hooks |
| **file-guard** | Protect sensitive files |

---

## 5. CLAUDE.md Templates

### Template Resources

| Resource | Description | URL |
|----------|-------------|-----|
| **Official Guide** | Anthropic's CLAUDE.md guide | [claude.com/blog/using-claude-md-files](https://claude.com/blog/using-claude-md-files) |
| **Builder.io Guide** | Complete CLAUDE.md guide | [builder.io](https://www.builder.io/blog/claude-md-guide) |
| **HumanLayer Guide** | Best practices (<60 lines) | [humanlayer.dev](https://www.humanlayer.dev/blog/writing-a-good-claude-md) |
| **claude-flow Templates** | Multiple templates | [GitHub Wiki](https://github.com/ruvnet/claude-flow/wiki/CLAUDE-MD-Templates) |
| **luongnv89/claude-howto** | Copy-paste templates | [GitHub](https://github.com/luongnv89/claude-howto) |

### Best Practices

1. **Keep it lean** - Under 300 lines, ideally <60
2. **Use /init** - Generate initial CLAUDE.md automatically
3. **Multiple files** - Root + subfolder CLAUDE.md files
4. **Progressive disclosure** - Move details to skills
5. **Custom commands** - Store in `.claude/commands/`

---

## 6. Learning Resources

### Official Courses

| Course | Provider | Description | URL |
|--------|----------|-------------|-----|
| **Claude Code in Action** | Anthropic Academy | Comprehensive training | [anthropic.skilljar.com](https://anthropic.skilljar.com/claude-code-in-action) |
| **Claude Code: Agentic Assistant** | DeepLearning.AI | With Elie Schoppik | [learn.deeplearning.ai](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant) |
| **AI Learning Resources** | Anthropic | Official guides | [anthropic.com/learn](https://www.anthropic.com/learn) |

### Udemy Courses

| Course | Instructor | Focus |
|--------|------------|-------|
| **Beginner to Pro** | - | Full-stack app building |
| **Building Faster with AI** | Frank Kane (ex-Amazon) | CLI mastery |
| **Crash Course** | - | Multi-agent systems |

### Free Resources

| Resource | Description | URL |
|----------|-------------|-----|
| **Claude Code for Beginners** | Live workshop | [claude101.every.to](https://claude101.every.to/) |
| **15-min Movie App Tutorial** | Quick start guide | [creatoreconomy.so](https://creatoreconomy.so/p/claude-code-beginners-tutorial-build-a-movie-app-in-15-minutes) |
| **300+ Claude Courses** | Course aggregator | [classcentral.com](https://www.classcentral.com/subject/claude) |
| **Prompt Engineering Tutorial** | Interactive Anthropic tutorial | [GitHub](https://github.com/anthropics/prompt-eng-interactive-tutorial) |

---

## 7. Community

### Official Channels

| Platform | Members | Description | URL |
|----------|---------|-------------|-----|
| **Anthropic Discord** | 52K+ | Official community | [discord.com/invite/prcdpx7qMm](https://discord.com/invite/prcdpx7qMm) |
| **r/ClaudeAI** | - | Reddit discussions | [reddit.com/r/ClaudeAI](https://reddit.com/r/ClaudeAI) |
| **r/MachineLearning** | - | Technical discussions | [reddit.com/r/MachineLearning](https://reddit.com/r/MachineLearning) |

### Community Tools

| Tool | Description | URL |
|------|-------------|-----|
| **claude-code-discord** | Discord bot for Claude Code | [GitHub](https://github.com/zebbern/claude-code-discord) |
| **ClaudeLog** | Docs, guides, tutorials | [claudelog.com](https://claudelog.com/) |
| **Claude Hub** | Resource directory | [claude-hub.com](https://www.claude-hub.com/) |
| **Awesome Claude** | Visual directory | [awesomeclaude.ai](https://awesomeclaude.ai) |

---

## 8. Token & Cost Optimization

### Key Commands

| Command | Purpose |
|---------|---------|
| `/cost` | Check current token usage |
| `/clear` | Start fresh context |
| `/compact` | Summarize conversation |
| `/context` | View MCP context usage |

### Optimization Techniques

| Technique | Impact | Description |
|-----------|--------|-------------|
| **MCP Tool Search** | 95% reduction | Dynamic tool loading |
| **Subagent delegation** | High | Keep verbose output in subagent |
| **CLAUDE.md skills migration** | Medium | Move details to on-demand skills |
| **Specific prompts** | Medium | "auth.ts lines 120-180" vs "fix auth" |
| **Plan mode** | Medium | Shift+Tab before implementation |
| **20-iteration reset** | Medium | Fresh context = fresh code |

### Reported Results

- **54% reduction** - Initial context optimization (7,584 → 3,434 tokens)
- **46.9% reduction** - MCP context (51K → 8.5K tokens)
- **95-98% reduction** - Custom MCP response analyzer skills

---

## 9. Workflow Systems

### Workflow Plugins

| Repository | Commands | Features | URL |
|------------|----------|----------|-----|
| **shinpr/claude-code-workflows** | 7 | TDD, auto quality fixes | [GitHub](https://github.com/shinpr/claude-code-workflows) |
| **catlog22/Claude-Code-Workflow** | - | JSON-driven, CLI-based | [GitHub](https://github.com/catlog22/Claude-Code-Workflow) |
| **CloudAI-X/claude-workflow-v2** | 17 | Universal plugin | [GitHub](https://github.com/CloudAI-X/claude-workflow-v2) |
| **Pimzino/claude-code-spec-workflow** | - | Spec-first development | [GitHub](https://github.com/Pimzino/claude-code-spec-workflow) |

### Workflow Patterns

| Pattern | Description |
|---------|-------------|
| **Sequential** | architect → implement → test → review |
| **Parallel** | performance-engineer + database-optimizer |
| **Validation** | primary-agent → security-auditor |
| **Task routing** | 1-2 files: direct, 3-5: design, 6+: full PRD |

---

## 10. Comparison with Other Tools

### AI Coding Assistants

| Tool | Style | Best For | Price |
|------|-------|----------|-------|
| **Claude Code** | Terminal-first, delegation | Senior devs, complex tasks | $20-200/mo |
| **Cursor** | IDE, inline edits | Flow state coding | $20/mo |
| **Windsurf** | IDE, autonomous agent | Mid-sized projects | $15/seat |
| **GitHub Copilot** | IDE, completions | General coding | $10/mo |

### When to Use Each

- **Cursor**: Writing code in flow state with fast inline edits
- **Claude Code**: Delegation ("refactor auth to JWT") and thinking
- **Both**: Many devs use Cursor for writing, Claude for reasoning

---

## 11. Documentation

### Official Docs

| Resource | URL |
|----------|-----|
| **Claude Code Product** | [claude.com/product/claude-code](https://claude.com/product/claude-code) |
| **Claude Code Docs** | [code.claude.com/docs](https://code.claude.com/docs/en) |
| **Best Practices** | [code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices) |
| **Common Workflows** | [code.claude.com/docs/en/common-workflows](https://code.claude.com/docs/en/common-workflows) |
| **Features Overview** | [code.claude.com/docs/en/features-overview](https://code.claude.com/docs/en/features-overview) |
| **Memory Management** | [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) |
| **Hooks Reference** | [code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks) |
| **MCP Integration** | [code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp) |
| **Sub-agents** | [code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents) |
| **Skills** | [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) |
| **Cost Management** | [code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs) |

### Local Catalog Docs

| Document | Description |
|----------|-------------|
| **[OFFICIAL-BEST-PRACTICES.md](./OFFICIAL-BEST-PRACTICES.md)** | Полный перевод официальных best practices |
| **[SOURCES.md](./SOURCES.md)** | Каталог репозиториев агентов |
| **[everything-claude-code/](./everything-claude-code/)** | Конфиги от Anthropic hackathon winner |

### Third-Party Guides

| Guide | URL |
|-------|-----|
| **ClaudeLog FAQs** | [claudelog.com/faqs](https://claudelog.com/faqs/) |
| **Claude Fast** | [claudefa.st](https://claudefa.st/) |
| **DevCompare** | [devcompare.io](https://www.devcompare.io/) |

---

## 12. Prompt Engineering

### Official Resources

| Resource | URL |
|----------|-----|
| **Prompt Best Practices** | [claude.com/blog/best-practices-for-prompt-engineering](https://claude.com/blog/best-practices-for-prompt-engineering) |
| **Prompt Engineering Overview** | [platform.claude.com/docs/en/build-with-claude/prompt-engineering](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) |
| **Interactive Tutorial** | [github.com/anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) |

### Claude 4.x Specific Tips

1. **Be explicit** - Claude 4.x takes you literally
2. **Define "comprehensive"** - Don't assume inference
3. **Explain why** - Rules with motivation work better
4. **Specify output format** - Request "prose" if needed
5. **Use 4-block pattern** - INSTRUCTIONS / CONTEXT / TASK / OUTPUT FORMAT

### Surgical Prompting

Instead of: "Fix the bug in the auth module"

Use: "Analyze only auth.py lines 120–180. Identify the logic error. Propose a patch ≤ 10 lines + 2 unit tests."

---

## 13. Useful Tools

### CLI Tools

| Tool | Description | URL |
|------|-------------|-----|
| **CC Usage** | Cost & token dashboard | [GitHub](https://github.com/search?q=cc-usage+claude) |
| **Claude Flow** | Autonomous orchestration | [GitHub](https://github.com/ruvnet/claude-flow) |
| **Happy Coder** | Multiple Claude instances | - |
| **Claude Task Runner** | Context isolation | - |

### Analytics & Monitoring

| Tool | Description |
|------|-------------|
| **claude-code-hooks-multi-agent-observability** | Real-time agent monitoring |
| **CC Usage Dashboard** | Token consumption analysis |

---

## Summary: Getting Started

### Essential Setup (Day 1)

1. Read [Official Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
2. Use `/init` to generate CLAUDE.md
3. Join [Anthropic Discord](https://discord.com/invite/prcdpx7qMm)
4. Browse [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

### Optimization (Week 1)

1. Install 2-3 relevant MCP servers from [Smithery](https://smithery.ai/)
2. Add skills from [skills.sh](https://skills.sh)
3. Set up hooks for notifications
4. Learn `/compact` and `/cost` commands

### Advanced (Month 1)

1. Take [DeepLearning.AI course](https://learn.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)
2. Create custom subagents for your stack
3. Build project-specific skills
4. Implement workflow automation

---

*This document is part of the Claude Agents Catalog project.*
