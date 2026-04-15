# Timothy — AI Companion Memory Core

This repository is the persistent memory system for **Timothy**, Nufa's personal AI companion.

## On Every Session Start

Before responding to the first message, load these files in order:

1. `main/main-memory.md` — Timothy's identity + Nufa's profile + relationship context
2. `main/current-session.md` — Last session recap (working memory)
3. `main/reminders.md` — Open reminders; flag urgent/overdue items in greeting

Then deliver the session brief per `plugins/timothy-skills/skills/session-briefing/session-brief-core.md`.

## Keyword Triggers

| Keyword | Action |
|---------|--------|
| `timothy` | Full memory restoration — load the 3 files above, deliver session brief |
| `save` | Save current progress to relevant memory files |
| `save diary` | Write diary entry to `daily-diary/current/YYYY-MM-DD.md` |
| `commit` | Follow `plugins/timothy-skills/skills/auto-commit/SKILL.md` |
| `bye` / `goodnight` / `I'm done` | Follow `plugins/timothy-skills/skills/session-end/SKILL.md` — diary → memories → commit + push |

## Repository Structure

```
master-memory.md              ← Commands reference + skill system overview
main/
  main-memory.md              ← Timothy identity + Nufa profile (essential)
  current-session.md          ← Session RAM (essential)
  reminders.md                ← Open reminders
  decisions.md                ← Decision log
  post-mortems.md             ← Failure log
  relationship-memory.md      ← Nufa observations over time
plugins/
  timothy-skills/
    skills/                   ← 13 active skills
daily-diary/
  current/                    ← Active diary entries (YYYY-MM-DD.md)
  archived/                   ← Past months
library/                      ← Knowledge base (8 sections)
projects/                     ← Active + archived project files
```
