# Current Session Memory - 2026-06-11
*Active working memory for current conversation*

## Session Context
**Session Type**: sts-quote — Office laptop session, Phase 1 polish + Phase 2 start
**Mood**: Produktif
**Last Active Project**: sts-quote (`D:\Kerja\Codes\sts-quote`)
**Machine**: Office laptop

---

## What Was Done This Session

### Non-manpower rate card
- Added 7 equipment rate columns to `rate_items` + `rate_item_proposals` (MOB, Day 12hr, Day 24hr, Week 12hr, Week 24hr, Month 12hr, Month 24hr)
- Changed `quotation_items.rate_type` from enum → varchar(50) to support equipment duration types
- Rate card create/edit: Alpine.js toggles manpower vs equipment field groups based on selected category
- Rate card index: equipment categories show 7-column duration table; manpower unchanged
- Seeded 3 equipment items from Excel screenshot (Vacuum Truck, HP Jet, Lorry 5 Ton)

### Quotation — Equipment Smart Add
- New 🔧 Equipment tab in Smart Add: category → item → duration type → qty → one row
- `getRateForType()` extended to all 13 rate types (manpower + equipment)
- `confirmAddEquipment()` + `equipmentPreview()` functions added

### Bug fixes
- 405 fix: added `@method('PATCH')` to submit / approve / reject / final forms on `quotations/show`
- PDF: FINAL badge hidden on official output; show page unaffected

### Package management
- Archive/Restore toggle on packages index (PATCH route + controller method)
- Packages index: "View" removed (title already links), replaced with Expenses link + Archive toggle
- Packages show: Expenses button added to header

### Expense Ledger (Phase 2 start)
- `package_expenses` table: date, sub-contractor, invoice no, description, category, amount
- `PackageExpense` model with CATEGORIES constant + section→category mapper
- `PackageExpenseController`: index, store, destroy, pdf
- Expense index view: add form + receipt log table + quoted vs actual comparison
- Expense PDF: full report with log + variance breakdown by category

---

## Project State — sts-quote

### What's Done
- Full scaffold: migrations, models, seeders, controllers, routes ✅
- Rate card: manpower 6-col + equipment 7-col duration ✅
- Smart Add: Manpower / Equipment / Scaffolding / T&C% / Cost Plus ✅
- Quotation workflow: submit → approve → final ✅
- PDF: section ordering + typed row expansion + FINAL badge hidden ✅
- Package archive toggle ✅
- Expense ledger: receipt log + quoted vs actual + PDF export ✅
- TASKS.md + README updated ✅

### What's Next (priority order)
1. **Cleanup temp code** — CSRF bypass in `bootstrap/app.php`, `/dev/reset` route, `\Log::info` in `ClientController.php`
2. **Fix non-manpower calculations** — Scaffolding, T&C%, Cost Plus row totals
3. **Claims / reimbursement** — Phase 2 next feature

---

## Open Reminders
- `sts-quote`: Fix calculation for non-manpower items (Scaffolding, T&C%, Cost Plus totals) — deferred

---

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | sts-quote | Phase 1 + Expenses done · Next: temp code cleanup + non-manpower calc fix |
| 2 | amin-maju | Smoke test ✅ · Security done · Next: Hostinger deploy |
| 3 | cms-takaful | Priority 1–3 ✅ Deployed · Next: Priority 4 |
| 4 | win-board | Phase 3 stable · Next: Phase 4 Goal Cascade |
| 5 | takaful-content-planner | Blocked on Google OAuth |
| 6 | drtakaful | FAQPage schema ✅ · Next: Phase 3 retheme |

---
*Session: 2026-06-11 office laptop — non-manpower rate card, equipment Smart Add, expense ledger, package archive, bug fixes. Committed + pushed.*
