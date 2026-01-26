# Claude Code Agent Sources

Comprehensive catalog of Claude Code agent repositories, workflows, and skills.

Last updated: 2026-01-26

---

## Quick Reference

| Priority | Repository | Agents | Best For |
|----------|------------|--------|----------|
| **1** | VoltAgent/awesome-claude-code-subagents | 100+ | Universal starter pack |
| **2** | lst97/claude-code-sub-agents | 33 | Full-stack + AI/ML focus |
| **3** | shinpr/claude-code-workflows | 15+ | Structured dev workflows |
| **4** | anthropics/skills | 10+ | Official document skills |
| **5** | supatest-ai/awesome-claude-code-sub-agents | 50+ | Architecture consulting |

---

## 1. Subagent Collections

### VoltAgent/awesome-claude-code-subagents
**URL:** https://github.com/VoltAgent/awesome-claude-code-subagents

**Overview:**
- 100+ production-ready subagents
- Best organized collection with 10 major categories
- Multiple installation methods (plugin, script, manual)

**Categories:**
1. Core Development (API, backend, frontend, fullstack)
2. Language Specialists (20+ languages)
3. Infrastructure (DevOps, K8s, Terraform, cloud)
4. Quality & Security (reviewers, auditors, testers)
5. Data & AI (ML, data science, prompt engineering)
6. Developer Experience (docs, refactoring, builds)
7. Specialized Domains (blockchain, fintech, gaming)
8. Business & Product (PMs, analysts)
9. Meta & Orchestration (coordinators)
10. Research & Analysis

**Installation:**
```bash
# Plugin method (recommended)
claude plugin marketplace add VoltAgent/awesome-claude-code-subagents
claude plugin install voltagent-lang
claude plugin install voltagent-infra
claude plugin install voltagent-quality

# Manual
git clone https://github.com/VoltAgent/awesome-claude-code-subagents.git
./install-agents.sh
```

**Key Agents for Our Projects:**
- `code-reviewer` - Code quality analysis
- `python-pro` - Python expertise
- `typescript-pro` - TypeScript expertise
- `security-auditor` - Security review
- `database-optimizer` - DB performance

---

### lst97/claude-code-sub-agents
**URL:** https://github.com/lst97/claude-code-sub-agents

**Overview:**
- 33 specialized agents
- Strong full-stack and AI/ML focus
- Well-documented orchestration patterns

**Categories:**
- Development (11): frontend, backend, fullstack, mobile, platform
- Infrastructure (5): cloud, DevOps, deployment
- Quality (5): code-reviewer, QA, testing
- Data & AI (8): data science, ML, prompt engineering
- Security: security-auditor

**Installation:**
```bash
# Clone to Claude directory
cd ~/.claude
git clone https://github.com/lst97/claude-code-sub-agents.git

# Or manual copy
mkdir -p ~/.claude/agents/lst97
cp /path/to/agents/*.md ~/.claude/agents/lst97/
```

**Orchestration Patterns:**
```
Sequential: architect → implement → test → review
Parallel: performance-engineer + database-optimizer
Validation: primary-agent → security-auditor
```

**Key Agents for Our Projects:**
- `backend-architect` - API design
- `fastapi-expert` - FastAPI patterns (inferred)
- `ai-engineer` - AI/ML tasks
- `prompt-engineer` - LLM optimization

---

### supatest-ai/awesome-claude-code-sub-agents
**URL:** https://github.com/supatest-ai/awesome-claude-code-sub-agents

**Overview:**
- 50+ architect/consultant agents
- Guidance-first approach (not code generation)
- Strong on decision frameworks

**Categories:**
- Languages (Python, JS/TS, Java, Go, Rust, Haskell, Clojure)
- Frameworks (React, Vue, Angular, Django, Spring Boot)
- Architecture (design patterns, microservices, clean arch)
- Testing & Quality
- DevOps (Docker, K8s, AWS, Terraform)
- LLM Engineering (RAG, multi-agent, fine-tuning)
- Industries (FinTech, Healthcare)

**Installation:**
```bash
git clone https://github.com/supatest-ai/awesome-claude-code-sub-agents.git
cp */*.md ~/.config/claude-code/agents/
```

**Philosophy:**
- Help make decisions, not just write code
- Technology selection frameworks
- Architecture pattern guidance
- Production best practices

**Key Agents for Our Projects:**
- `fintech-security-expert` - Trading app security
- `microservices-architect` - Service design
- `react-architect` - React patterns

---

### 0xfurai/claude-code-subagents
**URL:** https://github.com/0xfurai/claude-code-subagents

**Overview:**
- 100+ agents
- Alternative formulations to VoltAgent
- Different prompt styles

**Use Case:**
Backup source when VoltAgent agents don't fit your style.

---

### valllabh/claude-agents
**URL:** https://github.com/valllabh/claude-agents

**Overview:**
- 8 focused agents
- Covers full software development lifecycle
- Compact, coherent set

**Use Case:**
When you want a minimal, well-integrated agent set rather than 100+ options.

---

## 2. Workflow Systems

### shinpr/claude-code-workflows
**URL:** https://github.com/shinpr/claude-code-workflows

**Overview:**
- Structured development pipelines
- TDD-focused implementation
- Auto quality fixes
- Smart task routing by complexity

**Commands:**
| Command | Purpose |
|---------|---------|
| `/implement <feature>` | End-to-end development |
| `/design` | Design documentation |
| `/plan` | Work planning |
| `/build` | Execute from plans |
| `/task` | Single task execution |
| `/diagnose` | Problem investigation |
| `/reverse-engineer` | PRD from existing code |

**Task Routing:**
- 1-2 files → Direct implementation
- 3-5 files → Technical design phase
- 6+ files → Full PRD + design

**Installation:**
```bash
claude
/plugin marketplace add shinpr/claude-code-workflows
/plugin install dev-workflows@claude-code-workflows
# Restart session
/implement <your feature>
```

**Agents Included:**
- requirement-analyzer
- work-planner
- task-decomposer
- task-executor
- quality-fixer
- code-reviewer
- document-reviewer

---

### catlog22/Claude-Code-Workflow
**URL:** https://github.com/catlog22/Claude-Code-Workflow

**Overview:**
- JSON-driven workflow definitions
- 4-level workflow system
- CLI-based execution

**Installation:**
```bash
npm install -g claude-code-workflow
ccw install -m ...
```

**Use Case:**
CI/CD integration, repeatable scenarios.

---

### CloudAI-X/claude-workflow-v2
**URL:** https://github.com/CloudAI-X/claude-workflow-v2

**Overview:**
- Universal workflow plugin
- Includes agents, skills, hooks, output styles
- Works with any project type

**Use Case:**
All-in-one workflow solution.

---

### Pimzino/claude-code-spec-workflow
**URL:** https://github.com/Pimzino/claude-code-spec-workflow

**Overview:**
- Spec-first development
- Specification → Implementation → Verification
- MCP version available

**Use Case:**
When you prefer writing specs before code.

---

### breaking-brake/cc-wf-studio
**URL:** https://github.com/breaking-brake/cc-wf-studio

**Overview:**
- Visual workflow editor
- Drag-and-drop agent design
- Export to .claude/agents/*.md

**Use Case:**
Visual design of multi-agent workflows.

---

## 3. Official Resources

### anthropics/skills
**URL:** https://github.com/anthropics/skills

**Overview:**
- Official Anthropic skills
- Document handling (docx, pdf, xlsx, pptx)
- Skill specification reference

**Installation:**
```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

**Available Skills:**
- `docx` - Word documents
- `pdf` - PDF handling
- `xlsx` - Excel spreadsheets
- `pptx` - PowerPoint presentations

**Skill Structure:**
```yaml
---
name: my-skill-name
description: What this skill does
---

# Skill Name

[Instructions for Claude]

## Examples
## Guidelines
```

---

### anthropics/claude-agent-sdk-demos
**URL:** https://github.com/anthropics/claude-agent-sdk-demos

**Overview:**
- Official SDK demos
- Reference implementations
- Multi-agent patterns

**Demos:**
- hello-world (V1 API)
- hello-world-v2 (Session API)
- simple-chatapp (WebSocket + React)
- research-agent (Multi-agent orchestration)
- resume-generator (Skills + WebSearch)
- excel-demo (Electron + Skills)
- email-agent (IMAP integration)

---

## 4. Plugin Collections

### wshobson/agents
**URL:** https://github.com/wshobson/agents

**Overview:**
- 100 specialized agents
- 15 workflow orchestrators
- 110 agent skills
- 76 development tools

**Use Case:**
Comprehensive plugin bundle for everything at once.

---

## 5. Selection Strategy

### For Trading/Finance Projects
**Priority agents:**
1. `security-auditor` (VoltAgent or lst97)
2. `fintech-security` (supatest-ai)
3. `python-pro` (VoltAgent)
4. `api-designer` (lst97)

### For Next.js/React Projects
**Priority agents:**
1. `nextjs-pro` (VoltAgent or lst97)
2. `react-architect` (supatest-ai)
3. `typescript-pro` (VoltAgent)

### For Data/AI Projects
**Priority agents:**
1. `database-optimizer` (VoltAgent)
2. `postgres-pro` (lst97)
3. `ai-engineer` (lst97)

### For DevOps
**Priority agents:**
1. `docker-specialist` (VoltAgent)
2. `deployment-engineer` (lst97)

### Universal (All Projects)
**Must-have agents:**
1. `code-reviewer` (any source)
2. `test-automator` (VoltAgent)

---

## 6. Agent Format Reference

Standard subagent structure:

```markdown
---
name: agent-name
description: When to invoke this agent
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet  # or opus, haiku, inherit
---

# Agent Name

**Role**: What this agent does
**Expertise**: Technologies and domains

## Capabilities
- Capability 1
- Capability 2

## Instructions
[Detailed system prompt]

## Constraints
- What NOT to do
```

**Tool Permissions:**
- Read-only: `Read, Grep, Glob`
- Write: `Read, Write, Edit, Bash`
- Full: `Read, Write, Edit, Bash, WebSearch, WebFetch`

---

## 7. Links

### Documentation
- [Claude Code Subagents Docs](https://code.claude.com/docs/en/sub-agents)
- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Swarm Orchestration Skill](https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea) - Complete guide to multi-agent coordination with TeammateTool, Task system, and orchestration patterns

### Community
- [GitHub Topic: claudecode-subagents](https://github.com/topics/claudecode-subagents)
- [Claude Code Subreddit](https://www.reddit.com/r/ClaudeAI/)

### Tools
- [SubAgents Directory](https://subagents.app)
- [Skills Marketplace](https://skills.sh) (also skillsmp.com)
- [Claude Code Templates](https://www.aitmpl.com) - Ready-to-use agents, skills, and components with cloud sandbox execution

---

## 8. Skills Collection

Skills are reusable capabilities that extend Claude Code with specialized procedural knowledge.

### Included Skills (catalog/skills/)

#### Vercel Skills
| Skill | Installs | Description |
|-------|----------|-------------|
| **react-best-practices** | 24.9K | 40+ React/Next.js performance rules from Vercel Engineering |
| **web-design-guidelines** | 18.7K | Web design patterns and accessibility |

#### Anthropic Skills
| Skill | Description |
|-------|-------------|
| **skill-creator** | Meta-skill for creating custom skills |
| **mcp-builder** | Guide for building MCP servers (Python/TypeScript) |
| **webapp-testing** | Web application testing workflows |

### Installation

Skills can be installed globally or per-project:

```bash
# Global installation
cp -r catalog/skills/vercel/react-best-practices ~/.claude/skills/

# Project-specific
cp -r catalog/skills/anthropic/mcp-builder /path/to/project/.claude/skills/
```

### External Skills Sources

| Source | URL | Description |
|--------|-----|-------------|
| Vercel Skills | github.com/vercel-labs/agent-skills | Official Vercel skills |
| Anthropic Skills | github.com/anthropics/skills | Official Anthropic skills |
| Skills Marketplace | skills.sh | Community skill directory |
| Claude Code Templates | aitmpl.com | Components with cloud sandbox (E2B, Cloudflare, Docker) |

### Creating Custom Skills

Use the `skill-creator` skill from Anthropic to create custom skills:

1. Understand the skill with concrete examples
2. Plan reusable contents (scripts, references, assets)
3. Initialize with `init_skill.py`
4. Write SKILL.md with clear frontmatter
5. Package with `package_skill.py`
