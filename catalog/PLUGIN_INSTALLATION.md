# Plugin Installation Guide

> Documentation for Issue #6: Install shinpr/claude-code-workflows plugin

## Prerequisites

- Claude Code CLI installed and configured
- GitHub access for plugin repositories

---

## Plugin: shinpr/claude-code-workflows

This plugin provides structured development workflows for Claude Code.

### Installation Steps

#### Step 1: Add the Marketplace

Open Claude Code interactive mode and run:

```
claude
```

Then add the marketplace:

```
/plugin marketplace add shinpr/claude-code-workflows
```

#### Step 2: Install Development Workflows

```
/plugin install dev-workflows@claude-code-workflows
```

### Available Commands After Installation

| Command | Description | Use Case |
|---------|-------------|----------|
| `/implement` | End-to-end feature development | Full feature implementation with planning |
| `/design` | Create design documentation | Architecture and design docs |
| `/diagnose` | Problem investigation | Debug and root cause analysis |
| `/reverse-engineer` | Generate PRD from code | Document existing features |

---

## Usage Examples

### Example 1: Implement a Feature

```
/implement add webhook notification for new arbitrage opportunities in Polymarket bot
```

**Expected Workflow:**
1. Strategy formulation
2. Test-driven development approach
3. Implementation
4. Quality improvements
5. Evaluation

### Example 2: Design a System

```
/design real-time price feed aggregation system
```

### Example 3: Diagnose an Issue

```
/diagnose why orders are failing on the Kalshi API
```

### Example 4: Reverse Engineer

```
/reverse-engineer the authentication flow in email-agent
```

---

## Verification

After installation, verify the commands are available:

```
/help implement
```

Or list installed plugins:

```
/plugin list
```

---

## Manual Installation Alternative

If plugin commands are not available, you can manually clone the workflows:

```bash
# Clone the repository
git clone https://github.com/shinpr/claude-code-workflows.git ~/claude-code-workflows

# Copy commands to Claude Code
cp -r ~/claude-code-workflows/commands/* ~/.claude/commands/
```

---

## Plugin Structure Reference

```
~/.claude/plugins/
├── known_marketplaces.json
└── marketplaces/
    ├── claude-plugins-official/
    └── claude-code-workflows/  # After installation
        └── dev-workflows/
            ├── implement.md
            ├── design.md
            ├── diagnose.md
            └── reverse-engineer.md
```

---

## Troubleshooting

### Plugin not found
- Ensure the marketplace is added first
- Check GitHub repository availability

### Commands not available
- Restart Claude Code after installation
- Verify with `/plugin list`

### Permission errors
- Run Claude Code with appropriate permissions
- Check ~/.claude directory ownership

---

*Generated: 2026-01-23*
