# Current Session Memory - 2026-05-11
*Active working memory for current conversation*

## Session Context
**Session Type**: Discovery — bookkeeping (RezTax) rediscovered + documented
**Last Active Project**: bookkeeping (`D:\Kerja\Codes\bookkeeping`, local only)
**Status**: Project audited, markdown created, added to project list. Ready to work on next session.

## Last Session Recap

### bookkeeping — What Was Done (2026-05-11 afternoon)

1. **RezTax rediscovered** — forgotten project, last commit 2026-04-07 (34 days idle)
2. **Project audited** via controllers, routes, migrations, git log
3. **`projects/active/bookkeeping.md` created** — full snapshot documented
4. **`projects/project-list.md` updated** — bookkeeping added as #7 (🔴 stale)
5. Session cut short before actual work began

### What RezTax Has Built
- Income/expense CRUD, dashboard with monthly + yearly charts, category breakdown
- Tax summary page + PDF export (LHDN: EPF, insurance, lifestyle, medical reliefs + Zakat rebate)
- Savings goals tracking, CSV import, admin panel, Lemon Squeezy pricing stub
- Stack: Laravel 12, Tailwind v4, MySQL, dompdf, Lemon Squeezy

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Phase 3 stable — streak + XP fixes deployed |
| 2 | Project-B | Phase 5c done — dashboard live |
| 3 | cms-takaful | Fully deployed — polish done |
| 4 | takaful-content-planner | Phase 1 done — blocked on Google OAuth setup |
| 5 | drtakaful | FAQPage schema in progress |
| 6 | rox-bot | test_ocr.py needed |
| 7 | bookkeeping (RezTax) | 🔴 Rediscovered — audit pending, next: run + assess |

## Next Session Resume Points
- **bookkeeping**: Run `php artisan serve`, walk through the UI, decide what's missing before deploy
- **win-board Phase 4**: Goal Cascade (10yr → 5yr → yearly → quarterly → daily)
- **takaful-content-planner Phase 2**: Content CRUD — needs Google OAuth creds first
- **Project-B Phase 5d**: Onboarding nudge if no finance_notes set
- **drtakaful**: Resume FAQPage schema from `kenapa-takaful-penting.html`
- **rox-bot**: Run `test_ocr.py`

## Notes
- cms-takaful local: `cd K:\cms-takaful && php artisan serve`
- win-board local: `cd D:\Kerja\Codes\win-board && php artisan serve`
- Project-B local: `cd K:\Project-B && uvicorn web.app:app --reload --port 8000`
- Hostinger SSH: `python D:\Kerja\Codes\Project-AI-MemoryCore\tools\hostinger_ssh.py "command"`
- Hostinger auto-deploys from GitHub — no need to `git pull` manually on server
- win-board local path is `D:\Kerja\Codes\win-board` (not `D:\WebDev\win-board`)

## Notes
- cms-takaful local: `cd K:\cms-takaful && php artisan serve`
- win-board local: `cd D:\Kerja\Codes\win-board && php artisan serve`
- bookkeeping local: `cd D:\Kerja\Codes\bookkeeping && php artisan serve`
- Project-B local: `cd K:\Project-B && uvicorn web.app:app --reload --port 8000`
- Hostinger SSH: `python D:\Kerja\Codes\Project-AI-MemoryCore\tools\hostinger_ssh.py "command"`
- Hostinger auto-deploys from GitHub — no need to `git pull` manually on server

---
*Session updated: 2026-05-11*
