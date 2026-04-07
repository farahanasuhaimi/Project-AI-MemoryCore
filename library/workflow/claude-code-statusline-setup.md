# Claude Code Status Line — Usage Capacity Display
*Shows remaining capacity (5h + 7d windows) and context % in Claude Code's status bar*

## Overview
- **Trigger**: New machine setup or first time configuring Claude Code
- **Actors**: Timothy + Claude Code CLI
- **End State**: Status bar shows live capacity remaining + reset time after every response
- **Requires**: Claude.ai Pro/Max subscription (rate_limits data only available for subscribers)

## What It Displays

```
Claude Sonnet 4.6 | 5h:73% (resets 09:15 PM) | 7d:88% | ctx:91%
```

| Field | Meaning |
|-------|---------|
| `5h:XX%` | Capacity remaining in the rolling 5-hour window |
| `resets HH:MM AM/PM` | Local time when 5-hour window replenishes |
| `7d:XX%` | Capacity remaining in the rolling 7-day window |
| `ctx:XX%` | Context window remaining in current conversation |

> Rate limit fields appear after the **first API response** in a session, not on load.

## Setup Steps

### Step 1: Create the script
File: `~/.claude/statusline.sh`

```bash
#!/bin/bash
input=$(cat)

MODEL=$(echo "$input" | jq -r '.model.display_name // "Claude"')
CTX=$(echo "$input" | jq -r 'if .context_window.remaining_percentage then (.context_window.remaining_percentage | floor | tostring) + "%" else empty end')
FIVE_H_USED=$(echo "$input" | jq -r '.rate_limits.five_hour.used_percentage // empty')
WEEK_USED=$(echo "$input" | jq -r '.rate_limits.seven_day.used_percentage // empty')
RESET_AT=$(echo "$input" | jq -r '.rate_limits.five_hour.resets_at // empty')

LIMITS=""
if [ -n "$FIVE_H_USED" ]; then
  FIVE_H_REM=$(echo "$FIVE_H_USED" | awk '{printf "%.0f", 100-$1}')
  if [ -n "$RESET_AT" ]; then
    RESET_TIME=$(date -d "@$RESET_AT" +"%I:%M %p" 2>/dev/null || date -r "$RESET_AT" +"%I:%M %p" 2>/dev/null)
    LIMITS="5h:${FIVE_H_REM}% (resets ${RESET_TIME})"
  else
    LIMITS="5h:${FIVE_H_REM}%"
  fi
fi
if [ -n "$WEEK_USED" ]; then
  WEEK_REM=$(echo "$WEEK_USED" | awk '{printf "%.0f", 100-$1}')
  LIMITS="${LIMITS:+$LIMITS | }7d:${WEEK_REM}%"
fi
[ -n "$CTX" ] && LIMITS="${LIMITS:+$LIMITS | }ctx:${CTX}"

[ -n "$LIMITS" ] && echo "$MODEL | $LIMITS" || echo "$MODEL"
```

### Step 2: Update `~/.claude/settings.json`

Merge with existing content — do not overwrite other keys:

```json
{
  "autoUpdatesChannel": "latest",
  "statusLine": {
    "type": "command",
    "command": "~/.claude/statusline.sh"
  }
}
```

### Step 3: Make executable (Linux/Mac only — no-op on Windows)
```bash
chmod +x ~/.claude/statusline.sh
```

## Notes
- On Windows, `chmod` is not needed — the shebang line handles execution
- `date -d` (GNU) is tried first, `date -r` (BSD/macOS) as fallback for reset time parsing
- No API tokens consumed — status line runs entirely on local machine
- Use `statusline-setup` agent in Claude Code to reconfigure

## Projects Using This
- AI-MemoryCore (Nufa's home PC — Windows 10, GPU machine)

---
*Documented: 2026-04-07*
