# Current Session Memory - 2026-06-12 (Office Laptop)
*Prepared for next session — last updated 12:53*

## Last Session
**Date**: 2026-06-12 (afternoon, office laptop)
**Machine**: Office laptop
**Focus**: Project rename + setup

### What Was Done
- sts-quote renamed to `sts-projex` on GitHub
- Fresh clone at `D:\Kerja\Codes\sts-projex` (couldn't rename local folder — file lock)
- `.env` copied from old `sts-quote` folder
- `composer install` + `npm install` completed — project fully set up
- Old `sts-quote` folder still at `D:\Kerja\Codes\sts-quote` — can delete when convenient

### What's Next (start here next session)
1. **Phase 2A — Database** (`TASK.md` Phase 2, step 2A):
   - Migration: `expenses` (id, project_id, quotation_id, description, amount, category, date, status)
   - Migration: `claims` (id, expense_id, submitted_by, amount_claimed, status, remarks, submitted_at, approved_at)
   - Migration: `payments` (id, claim_id, amount_paid, payment_date, reference_no, recorded_by)
   - Models: Expense, Claim, Payment

---

## Project State — sts-projex (formerly sts-quote, Phase 1 Complete)

| Feature | Status |
|---------|--------|
| Auth + roles (Spatie) | ✅ |
| Rate card — manpower 6-col + equipment 7-col | ✅ |
| Client / Project / Package CRUD | ✅ |
| Client inactive + Project archive toggles | ✅ |
| Project staff assignment (PM approval) | ✅ |
| Smart Add: Manpower/Equipment/Scaffolding/T&C%/Cost Plus | ✅ |
| Quotation workflow (submit → approve → final) | ✅ |
| PDF — section ordering + typed row expansion | ✅ |
| Package archive toggle | ✅ |
| Expense ledger — receipt log + quoted vs actual + PDF | ✅ |

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
*End of day 2026-06-12. sts-quote renamed to sts-projex, fresh setup done. Next session: Phase 2A.*
