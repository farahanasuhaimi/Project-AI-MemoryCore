# Current Session Memory - 2026-05-07
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — win-board features + fixes
**Last Active Project**: win-board (`D:\Kerja\Codes\win-board`)
**Status**: Multiple features shipped. Deploy to Hostinger + Google Calendar token setup pending.

## Last Session Recap

### win-board — What Was Done (2026-05-07)
6 commits pushed:

1. **Urgency badge → emoji-only scale** (`51b095d`)
   - Replaced LATE/URGENT text badges with ⚠️→🟠→🔴→🚨→🔥→☠️→💀 (1–7+ days)
   - Fixed `w-5 h-5` container for consistent alignment; `min-w-0` on task text

2. **Task time estimates** (`8638ba3`)
   - `estimated_minutes` column on tasks (migration required)
   - Required for Must, optional for all others; dropdown 10m/30m/1h/2h/6h
   - Running total in Must header; overload warning >12h

3. **Done carry-forward task persistence fix** (`3fa7030`)
   - Carry-forward tasks completed today now stay visible until tomorrow (`done_at >= today`)

4. **Docs update** (`20a4044`) — README + CLAUDE.md updated for Phase 2.5

5. **Google Calendar integration** (`ecd2cb5`)
   - `GoogleCalendarService` with silent token refresh
   - Today's schedule strip on dashboard (timed + all-day events)
   - Meeting total vs Must estimate free-time indicator

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Features shipped — deploy + Calendar setup pending |
| 2 | drtakaful | FAQPage schema campaign in progress (9/~30 done) |
| 3 | rox-bot | Dynamic CAPTCHA detection done — test_ocr.py run needed |
| 4 | cms-takaful | Built — awaiting deploy |

## Next Session Resume Points
- **win-board — Deploy to Hostinger**:
  1. `git pull origin main` on server
  2. `php artisan migrate` (3 pending migrations: estimated_minutes, google tokens)
  3. `php artisan config:cache && php artisan route:cache`
- **win-board — Google Calendar activation**:
  1. Enable Google Calendar API in Google Cloud Console (APIs & Services → Library)
  2. Re-login with Google on the live site to grant `calendar.readonly` scope + get refresh token
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-05-07*
