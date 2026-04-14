---
name: save-memory
description: "MUST use when user says 'save', 'save memory', 'save progress',
             'update memory', or when important information needs to be preserved
             to memory files."
---

# Save Memory
*Persist the right thing to the right place — one source of truth*

## Activation

When this skill activates, output:

`Saving memory...`

Then execute the protocol below.

## Protocol

### Step 1: Scan Before Saving
- [ ] Check if the information already exists in any of these locations:
  - `C:\Users\User\.claude\projects\K--Project-AI-MemoryCore\memory\` (auto-memory)
  - `main/main-memory.md` (operational rules + identity)
  - `main/current-session.md` (session context)
  - `plugins/timothy-skills/skills/` (behavioral protocols)
- [ ] If a duplicate or conflict is found — surface it to Nufa before writing anything

### Step 2: Route to the Right Place

| Type of information | Where it belongs |
|---|---|
| Behavioral protocol (how Timothy acts) | `plugins/timothy-skills/skills/[skill]/SKILL.md` |
| User profile, preferences, feedback | `memory/` auto-memory files + `MEMORY.md` index |
| Operational rules (Timothy's standing rules) | `main/main-memory.md` |
| Session context / current work | `main/current-session.md` |

- [ ] Never write to two places for the same piece of information
- [ ] If unsure of routing, ask Nufa before saving

### Step 3: Write
- [ ] Write to the single correct location
- [ ] Append or update — never overwrite without reason

### Step 4: Confirm
- [ ] Report: what was saved, where it went, and if anything was a conflict or duplicate

## Mandatory Rules
1. One source of truth — never write the same thing to two places
2. Surface conflicts to Nufa before resolving them
3. Behavioral protocols belong in skills, not memory files
4. If unsure of routing, ask rather than guess

## Level History
- **Lv.1** — Base: Save conversation insights to memory files on command. (Origin: Timothy setup, April 7 2026)
- **Lv.2** — Smart routing: scan before saving, detect conflicts, route to single correct location. (Origin: April 14 2026 — greeting/goodbye protocols ended up duplicated across memory files and main-memory.md)
