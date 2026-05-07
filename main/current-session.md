# Current Session Memory - 2026-05-07
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — win-board deploy + Google Calendar + onboarding modal
**Last Active Project**: win-board (`D:\WebDev\win-board`)
**Status**: Fully deployed and stable. No open items.

## Last Session Recap

### win-board — What Was Done (2026-05-07 Evening)

1. **Hostinger SSH agent** — `K:\Project-AI-MemoryCore\tools\hostinger_ssh.py` (paramiko). Credentials in gitignored `tools/secrets.py`. Use for all server commands.

2. **Deploy completed** — migrations applied on Hostinger, config + route cache cleared.

3. **Google Calendar** — OAuth activated. Fixed to fetch from all calendars (not just primary). Async load so dashboard isn't blocked.

4. **Onboarding modal** — 3-slide welcome for new users. Bug fixed: `querySelector` on overlay + append-before-render.

5. **Docs** — README + CLAUDE.md updated for all changes.

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Stable — deployed, Calendar working, onboarding live |
| 2 | drtakaful | FAQPage schema campaign in progress (9/~30 done) |
| 3 | rox-bot | Dynamic CAPTCHA detection done — test_ocr.py run needed |
| 4 | cms-takaful | Built — awaiting deploy |

## Next Session Resume Points
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`
- **list.drtakaful.com**: Nufa mentioned it but couldn't locate the folder — investigate

## Notes
- Project root on this machine: `D:\WebDev\` (confirmed)
- SSH agent at `K:\Project-AI-MemoryCore\tools\hostinger_ssh.py`
- Always `git status` + `git pull` before starting any project (2 machines)

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-05-07 19:19*
