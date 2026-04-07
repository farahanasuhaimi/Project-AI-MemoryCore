---
name: save-memory
description: "MUST use when user says 'save', 'save memory', 'save progress',
             'update memory', or when important information needs to be preserved
             to memory files."
---

# Save Memory
*Persist important context and insights to Timothy's memory files*

## Activation

When this skill activates, output:

`Saving memory...`

Then execute the protocol below.

## Protocol

### Step 1: Identify What to Save
- [ ] Review current conversation for important information
- [ ] Identify new preferences, decisions, or context worth preserving
- [ ] Determine which memory files need updating (main-memory.md, current-session.md)

### Step 2: Update Memory Files
- [ ] Update `main/main-memory.md` with new personality insights, user preferences, or relationship context
- [ ] Update `main/current-session.md` with current working context and session recap
- [ ] Add diary entry if significant conversation occurred (if Save-Diary system is installed)

### Step 3: Confirm
- [ ] Display summary of what was saved
- [ ] Confirm all files updated successfully

## Mandatory Rules
1. Only save genuinely important information — not every conversation detail
2. Preserve existing content — append or update, never overwrite without reason
3. Confirm to user what was saved

## Level History
- **Lv.1** — Base: Save conversation insights to memory files on command. (Origin: Timothy setup, April 7 2026)
