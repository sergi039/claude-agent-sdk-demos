# Claude Code Official Best Practices

Извлечено из официальной документации: [code.claude.com/docs](https://code.claude.com/docs/en)

Last updated: 2026-01-21

---

## Quick Reference

| Практика | Влияние | Описание |
|----------|---------|----------|
| **Верификация работы** | Критическое | Давать тесты, скриншоты, ожидаемый результат |
| **Explore → Plan → Code** | Высокое | Разделять исследование, планирование, реализацию |
| **Управление контекстом** | Высокое | `/clear` между задачами, subagents для изоляции |
| **Специфичные промпты** | Среднее | Указывать scope, файлы, паттерны |
| **CLAUDE.md < 500 строк** | Среднее | Короткий, специфичный, version-controlled |

---

## 1. Верификация работы (Highest Leverage)

**Самая важная практика**: давать Claude способ проверить свою работу.

### Стратегии:

```markdown
# Плохо
"write a validateEmail function"

# Хорошо
"write a validateEmail function. example test cases:
user@example.com is true, invalid is false.
Run the tests after implementing"
```

### Методы верификации:

| Метод | Применение |
|-------|------------|
| **Тесты** | Функции, API, бизнес-логика |
| **Скриншоты** | UI изменения, Chrome extension |
| **Build check** | После изменений кода |
| **Lint check** | После рефакторинга |

---

## 2. Explore → Plan → Code

Разделять исследование и реализацию через **Plan Mode**.

### 4-фазный workflow:

```
1. Explore (Plan Mode)  → Claude читает файлы, отвечает на вопросы
2. Plan (Plan Mode)     → Детальный план реализации
3. Implement (Normal)   → Код + верификация
4. Commit               → PR с описанием
```

### Когда пропускать планирование:

- Scope понятен, fix маленький (typo, переменная)
- Можно описать diff одним предложением
- Изменения в 1-2 файлах

### Переключение режимов:

- **Shift+Tab** - циклически переключает режимы
- **Shift+Tab ×1** - Auto-Accept Mode
- **Shift+Tab ×2** - Plan Mode

---

## 3. Специфичные промпты

| До | После |
|----|-------|
| "add tests for foo.py" | "write a test for foo.py covering edge case where user is logged out. avoid mocks." |
| "fix the login bug" | "users report login fails after session timeout. check auth flow in src/auth/, especially token refresh. write failing test, then fix" |
| "add a calendar widget" | "look at how existing widgets are implemented. HotDogWidget.php is good example. follow pattern for calendar widget" |

### Способы предоставления контекста:

```bash
# Ссылка на файлы
@src/auth.ts

# Вставка изображений
Drag-drop или Ctrl+V

# URLs документации
"see https://docs.example.com/api"

# Pipe данных
cat error.log | claude

# Claude сам достаёт контекст
"Use gh issue view to get details"
```

---

## 4. CLAUDE.md Configuration

### Генерация:

```bash
/init  # Создаёт базовый CLAUDE.md
```

### Что включать ✅:

```markdown
# Code style
- Use ES modules (import/export), not CommonJS (require)
- Destructure imports when possible

# Workflow
- Typecheck after code changes
- Run single tests, not full suite

# Build commands
npm run test
npm run build
npm run lint
```

### Что НЕ включать ❌:

- То, что Claude поймёт из кода
- Стандартные конвенции языка
- Детальная API документация (лучше ссылка)
- Информация, которая часто меняется
- Длинные объяснения
- Очевидные практики ("write clean code")

### Структура файлов:

```
~/.claude/CLAUDE.md          # Все сессии
./CLAUDE.md                  # В git, для команды
./CLAUDE.local.md            # Личный, в .gitignore
./.claude/rules/*.md         # Модульные правила
```

### Импорты:

```markdown
See @README.md for project overview
See @package.json for npm commands

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal: @~/.claude/my-project-instructions.md
```

---

## 5. Управление контекстом

### Ключевой принцип:

> Context Window - главный ограничивающий ресурс. Performance деградирует по мере заполнения.

### Команды:

| Команда | Действие |
|---------|----------|
| `/clear` | Сброс контекста между задачами |
| `/compact` | Сжатие истории с сохранением важного |
| `/compact <instructions>` | Сжатие с указаниями ("Focus on API changes") |
| `/cost` | Проверка использования токенов |
| `/context` | Просмотр MCP context usage |

### Anti-pattern "Kitchen Sink Session":

```
❌ Задача 1 → Несвязанный вопрос → Вернуться к задаче 1
   Контекст забит нерелевантной информацией

✅ Задача 1 → /clear → Задача 2 → /clear → Задача 3
```

### Правило 20 итераций:

> "Reset context every 20 iterations. Performance craters after 20."

---

## 6. Subagents для изоляции

### Использование:

```bash
# Исследование в изолированном контексте
"use subagents to investigate how auth handles token refresh"

# Верификация работы
"use a subagent to review this code for edge cases"

# Параллельные задачи
"use subagents to check security, performance, and style in parallel"
```

### Преимущества:

- Свежий изолированный контекст
- Только summary возвращается
- Не загрязняет основной разговор
- Можно специфицировать skills

### Определение (.claude/agents/security-reviewer.md):

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities
- Auth/authz flaws
- Secrets in code
- Insecure data handling
```

---

## 7. Коррекция курса

### Инструменты:

| Действие | Команда |
|----------|---------|
| Остановить mid-action | `Esc` |
| Rewind к checkpoint | `Esc + Esc` или `/rewind` |
| Откатить изменения | `"Undo that"` |
| Сбросить контекст | `/clear` |

### Правило двух коррекций:

> После 2 неудачных коррекций в одной сессии: `/clear` и начать с лучшим промптом.

---

## 8. Hooks для автоматизации

### События:

| Event | Trigger | Use Case |
|-------|---------|----------|
| **SessionStart** | Начало сессии | Загрузка контекста, env vars |
| **PreToolUse** | Перед tool | Валидация, модификация |
| **PostToolUse** | После tool | Проверка результата |
| **Stop** | Завершение ответа | Решить продолжать ли |

### Когда hooks vs CLAUDE.md:

| Hooks | CLAUDE.md |
|-------|-----------|
| Formatting после каждого edit | Code style preferences |
| Linting изменённых файлов | Architectural patterns |
| Блокировка .env файлов | Когда нужно суждение |
| Zero exceptions | Guidance |

### Пример конфигурации:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{
          "type": "command",
          "command": "bash -c 'if [[ \"$@\" =~ \\.(env|key|secret)$ ]]; then echo \"Protected\" >&2; exit 2; fi'"
        }]
      }
    ]
  }
}
```

---

## 9. Memory System

### Иерархия (по приоритету):

| Тип | Путь | Scope |
|-----|------|-------|
| Managed policy | `/Library/Application Support/ClaudeCode/CLAUDE.md` | Организация |
| Project memory | `./CLAUDE.md` | Команда (git) |
| Project rules | `.claude/rules/*.md` | Команда (git) |
| User memory | `~/.claude/CLAUDE.md` | Все проекты |
| Project local | `./CLAUDE.local.md` | Личный |

### Path-specific rules:

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "src/**/*.{ts,tsx}"
---

# API Development Rules
- All API endpoints must include input validation
```

---

## 10. Headless & Automation

### CLI usage:

```bash
# Одиночный запрос
claude -p "Explain what this project does"

# Structured output
claude -p "List all API endpoints" --output-format json

# Streaming
claude -p "Analyze this log file" --output-format stream-json

# В скриптах
cat build-error.txt | claude -p 'explain root cause' > output.txt
```

### Fan-out паттерн:

```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue" \
    --allowedTools "Edit,Bash(git commit:*)"
done
```

### Writer/Reviewer паттерн:

| Session A (Writer) | Session B (Reviewer) |
|-------------------|---------------------|
| Implement rate limiter | Review for edge cases, race conditions |
| Address feedback | |

---

## 11. Extension Points

### Сравнение:

| Feature | Загрузка | Context Cost | Best For |
|---------|----------|--------------|----------|
| **CLAUDE.md** | Session start | Full content | Conventions |
| **Skills** | On-demand | Descriptions only | Reference, workflows |
| **Subagents** | On-spawn | Isolated | Parallel, specialized |
| **MCP** | Session start | Tool definitions | External services |
| **Hooks** | On-trigger | Zero | Automation |

### Skills vs Commands:

```markdown
# Skill (автоматически по контексту)
.claude/skills/api-conventions.md

# Command (явный вызов)
.claude/commands/deploy.md
→ /deploy
```

---

## 12. Common Failure Patterns

| Pattern | Problem | Fix |
|---------|---------|-----|
| **Kitchen sink** | Несвязанные задачи в одной сессии | `/clear` между задачами |
| **Correcting loop** | 3+ коррекции подряд | `/clear` + лучший промпт |
| **Over-specified CLAUDE.md** | Слишком длинный, игнорируется | Ruthlessly prune |
| **Trust-then-verify gap** | Plausible но неполный код | Всегда давать верификацию |
| **Infinite exploration** | "investigate" без scope | Scope или subagents |

---

## 13. Полезные команды

### Навигация:

```bash
/init           # Генерация CLAUDE.md
/memory         # Редактирование memory файлов
/permissions    # Настройка permissions
/sandbox        # OS-level isolation
/hooks          # Настройка hooks
/plugin         # Browse marketplace
/agents         # Список subagents
/mcp            # MCP статус и token costs
```

### Сессии:

```bash
claude --continue      # Продолжить последнюю
claude --resume        # Выбрать из списка
/rename <name>         # Переименовать сессию
/rewind                # Checkpoint menu
```

### Режимы:

```bash
claude --permission-mode plan    # Plan mode
Shift+Tab                        # Toggle modes
Option+T / Alt+T                 # Toggle thinking
Ctrl+O                          # Verbose mode
```

---

## 14. Interview Technique

Для сложных фич - пусть Claude интервьюирует вас:

```
I want to build [brief description]. Interview me in detail
using AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases,
concerns, tradeoffs. Don't ask obvious questions, dig into
hard parts I might not have considered.

Keep interviewing until we've covered everything,
then write complete spec to SPEC.md.
```

После spec - новая сессия для реализации (чистый контекст).

---

## 15. Multi-Language Support

Документация доступна на:
- English, French, German, Italian
- Japanese, Korean, Chinese (Simplified/Traditional)
- Spanish, Russian, Indonesian, Portuguese

---

## Ссылки

### Официальные:

- [Claude Code Docs](https://code.claude.com/docs/en)
- [Best Practices](https://code.claude.com/docs/en/best-practices)
- [Common Workflows](https://code.claude.com/docs/en/common-workflows)
- [Features Overview](https://code.claude.com/docs/en/features-overview)
- [Memory Management](https://code.claude.com/docs/en/memory)
- [Hooks Reference](https://code.claude.com/docs/en/hooks)
- [MCP Integration](https://code.claude.com/docs/en/mcp)
- [Sub-agents](https://code.claude.com/docs/en/sub-agents)
- [Skills](https://code.claude.com/docs/en/skills)
- [Costs](https://code.claude.com/docs/en/costs)

### Платформы:

- [Claude Code Web](https://claude.ai/code)
- [VS Code Extension](https://code.claude.com/docs/en/vs-code)
- [JetBrains Plugin](https://code.claude.com/docs/en/jetbrains)
- [GitHub Actions](https://code.claude.com/docs/en/github-actions)
- [Slack Integration](https://code.claude.com/docs/en/slack)

### Deployment:

- [Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock)
- [Google Vertex AI](https://code.claude.com/docs/en/google-vertex-ai)
- [Microsoft Foundry](https://code.claude.com/docs/en/microsoft-foundry)

---

*Источник: https://claude.com/product/claude-code и https://code.claude.com/docs*
