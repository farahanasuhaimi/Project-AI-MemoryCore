# 📋 Session Briefing — Skill Plugin

## Skill Name
Session Briefing

## Trigger Words
- Session start (automatic — fires before first response)
- `"brief"`
- `"session brief"`
- `"what did we do last time"`
- `"where did we leave off"`

## Suppress Trigger
- `"skip brief"` — suppresses for this session only

## Activation Condition
Fires automatically at the start of every new conversation session, before processing the user's first message.

## Behavior
1. Read `main/current-session.md` — extract last session recap (1–2 lines)
2. Read `main/reminders.md` — count open items (skip section if none)
3. Read project list — identify active project + 🔴/🟡 health flags (if LRU System installed)
4. Check current time — determine time period (if Time-based-Aware System installed)
5. Compose and deliver brief (max 12 lines) before responding to user

## Output Rules
- Maximum 12 lines total
- Maximum 3 attention flags — show most critical first
- Skip any section that has nothing to report
- Deliver before processing the user's first request

## Companion Skills
- Time-based-Aware-System → time period + work suggestion
- LRU-Project-Management-System → active project + health flags
- Reminders-System → open reminder items

## Lv.4 — Diary Recap (active)

On session start, after the standard brief, read the last 3 diary entries:

1. Glob `daily-diary/current/*.md`, sort by filename (date order), take the 3 most recent
2. Read each entry — extract: what was worked on, what was accomplished, what was left incomplete
3. Summarize in 3–5 lines: recent progress + anything unfinished
4. Suggest what to focus on next based on "Looking Forward" / next steps sections
5. Deliver as a natural continuation of the session brief — not a separate block

**Rules:**
- Keep the recap concise — a summary, not a re-read
- Only suggest next steps, don't prescribe them
- Trigger on any greeting-style first message ("hi", "hey", "hi timothy", etc.)

## Level History
- **Lv.1** — Base: session recap + time suggestion
- **Lv.2** — Reminders integration (requires Reminders-System)
- **Lv.3** — Project health flags (requires LRU-Project-Management-System)
- **Lv.4** — Diary recap: on greeting, read last 3 diary entries, summarize recent progress, suggest next steps. (Origin: April 14 2026 — Nufa wants zero context loss between sessions)
