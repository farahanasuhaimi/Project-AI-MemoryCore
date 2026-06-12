# Current Session Memory - 2026-06-13 (Home PC)
*Prepared for next session — last updated 01:12*

## Last Session
**Date**: 2026-06-12 evening → 2026-06-13 early morning
**Machine**: Home PC
**Focus**: sts-projex home PC setup + PM onboarding banner

### What Was Done
- Cloned `sts-projex` to `K:\sts-projex` on home PC
- `.env` bootstrapped from cms-takaful — updated APP_NAME + DB_DATABASE + fresh APP_KEY
- `composer install`, `npm install`, DB created, all 19 migrations landed, seeders run
- Fixed missing "Staff" link in projects index — route existed but was never in the view
- Built PM onboarding dashboard banner: 4-step checklist, step auto-tick, auto-hide when complete, Alpine dismiss with localStorage
- Verified via curl: banner shows for PM, hidden for admin, hidden when all steps done
- DB cleared of test data during verification — clean state (seeded only)

### What's Next (start here next session)
1. **Phase 2A — Database** (`TASK.md` Phase 2, step 2A):
   - Migration: `expenses` (id, project_id, quotation_id, description, amount, category, date, status)
   - Migration: `claims` (id, expense_id, submitted_by, amount_claimed, status, remarks, submitted_at, approved_at)
   - Migration: `payments` (id, claim_id, amount_paid, payment_date, reference_no, recorded_by)
   - Models: Expense, Claim, Payment

---

## Project State — sts-projex (Phase 1 Complete + Home PC Ready)

| Feature | Status |
|---------|--------|
| Auth + roles (Spatie) | ✅ |
| Rate card — manpower 6-col + equipment 7-col | ✅ |
| Client / Project / Package CRUD | ✅ |
| Client inactive + Project archive toggles | ✅ |
| Project staff assignment (PM approval) | ✅ |
| Staff link in Projects index | ✅ (fixed this session) |
| Smart Add: Manpower/Equipment/Scaffolding/T&C%/Cost Plus | ✅ |
| Quotation workflow (submit → approve → final) | ✅ |
| PDF — section ordering + typed row expansion | ✅ |
| Package archive toggle | ✅ |
| Expense ledger — receipt log + quoted vs actual + PDF | ✅ |
| PM onboarding banner (dashboard) | ✅ (built this session) |

---

## Open Reminders
*(none)*

---

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | sts-projex | Phase 1 complete · Next: Phase 2A — expenses/claims/payments DB |
| 2 | amin-maju | Smoke test ✅ · Security done · Next: Hostinger deploy |
| 3 | cms-takaful | Priority 1–3 ✅ Deployed · Next: Priority 4 |
| 4 | win-board | Phase 3 stable · Next: Phase 4 Goal Cascade |
| 5 | takaful-content-planner | Blocked on Google OAuth |
| 6 | drtakaful | FAQPage schema ✅ · Next: Phase 3 retheme |

---
*End of session 2026-06-13 early morning. Home PC setup done, onboarding banner shipped. Next: Phase 2A.*
