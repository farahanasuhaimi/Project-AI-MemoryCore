---
name: session-end
description: "MUST use when user signals end of session — 'bye', 'good night',
             'goodnight', 'good enough for today', 'that's enough', 'see you',
             'logging off', 'i'm done', 'session end', 'wrapping up', or any
             goodbye-style phrase. Executes the full session-end sequence:
             diary → memories → commit + push."
---

# Session End — Closing Protocol
*Nothing left behind. Every session complete.*

## Activation

When this skill activates, output:

`Wrapping up the session...`

Then execute the protocol below in order. Do not skip steps.

## Context Guard

| Context | Status |
|---------|--------|
| **User says goodbye-style phrase** | ACTIVE — full protocol |
| **User says "skip session end"** | DORMANT — acknowledge and close normally |
| **Mid-conversation (no goodbye)** | DORMANT — do not activate |

## Protocol

### Step 1: Write Diary Entry
- [ ] Run the `save-diary` skill (`plugins/timothy-skills/skills/save-diary/SKILL.md`)
- [ ] Document the session: what was worked on, key decisions, insights, next steps
- [ ] Append to `daily-diary/current/YYYY-MM-DD.md`
- [ ] Confirm: "Diary written."

### Step 2: Update Memories
- [ ] Update `main/current-session.md` — write session recap for next session's briefing
- [ ] Apply `save-memory` Lv.2 routing for any new information discovered this session
- [ ] Check `main/reminders.md` — move any resolved items to Completed
- [ ] Confirm: "Memories updated."

### Step 3: Commit and Push
- [ ] Run `auto-commit` skill — stage and commit all changes with structured message
- [ ] Push to remote: `git push`
- [ ] This context is pre-authorized for push — no extra confirmation needed
- [ ] If nothing to commit: report "Working tree clean — nothing to push"
- [ ] Confirm: "Pushed to GitHub."

### Step 4: Sign Off
- [ ] Report completion of all 3 steps
- [ ] Brief closing note — natural, not robotic

## Mandatory Rules
1. Always execute all 3 steps in order — diary first, memories second, push last
2. Never skip the diary step — even a short entry is better than none
3. Push is pre-authorized in this context only — no confirmation gate needed
4. If a step fails, report it clearly and continue with remaining steps
5. Never auto-trigger on casual mentions of leaving — only on clear session-ending phrases

## Edge Cases

| Situation | Behavior |
|-----------|----------|
| **Nothing significant happened** | Write a brief diary entry noting session type (e.g., "short planning session") |
| **Git push fails** | Report the error, confirm diary and memories were still saved |
| **Diary already written this session** | Skip Step 1, note "Diary already written", continue with Step 2 |
| **Clean working tree** | Skip commit, report "Nothing to commit", still confirm memories updated |
| **User says "just push"** | Run Step 3 only — skip diary and memory update |

## Level History
- **Lv.1** — Base: 3-step session-end sequence (diary → memories → push). Pre-authorized push in this context only. Goodbye phrase detection. (Origin: April 14 2026 — goodbye protocol had no proper skill home; session-briefing had no counterpart for session end)
