# Current Session Memory - 2026-06-11
*Active working memory for current conversation*

## Session Context
**Session Type**: sts-quote — Home PC session, bug fixes + new features
**Mood**: Produktif
**Last Active Project**: sts-quote (`K:\sts-quote`)
**Machine**: Home PC

---

## What Was Done This Session

### Cleanup
- Removed `\Log::info` debug lines from `ClientController.php`
- CSRF bypass + `/dev/reset` route already gone from previous session

### 11 Code-Review Bugs Fixed (subagent review)
- Route ordering: proposals + byCategory registered before resource (prevents `{rateItem}` shadowing)
- `createRevision()` now copies `item_type` + `meta` when cloning quotations
- `subtotal()` uses loaded collection instead of extra DB query
- `item_type` validation has enum constraint (`in:normal,percentage,...`)
- `rate_category_id` validation changed to nullable
- `prepareSubmit()` syncs meta before flattening percentage/cost_plus rows
- Row reload: percentage/cost_plus restore `qty`/`unit_price` from meta on load
- Scaffolding rows now store `item_type: 'scaffolding'`
- Equipment rows show correct duration options (MOB/Day/Week/Month) in rate type select
- `percentagePreview()` label corrected to include equipment
- PDF rate type column shows `%` / `Cost+` for percentage/cost_plus rows
- Expense `destroy()` now requires PM/planner role or own record

### Archive / Inactive Feature
- Projects: `archived_at` timestamp — archive/restore toggle on index, "View Archived" filter
- Clients: `is_active` boolean — set inactive/reactivate toggle on index, "View Inactive" filter
- Archived projects hidden from package creation dropdowns

### Project Staff Assignment
- `project_staff` table: `project_id`, `user_id`, `assigned_by`, `approved_by`, `approved_at`
- `ProjectStaff` model + `ProjectStaffController`
- Admin assigns planners → pending state
- PM approves/rejects → planner gets edit access
- `Project::hasEditAccess()` gate enforced on quotation + package edit/update/submit/clone
- `/projects/{project}/staff` management page (pending + approved + add form)
- Fixed: admin couldn't see projects — moved clients + projects to `role:pm|admin`

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
- Client inactive + Project archive toggles ✅
- Project staff assignment with PM approval ✅
- 11 code-review bugs fixed ✅

### What's Next
1. **Claims / reimbursement** — Phase 2 next feature

---

## Open Reminders
*(none)*

---

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | sts-quote | Phase 2 in progress · Next: Claims / reimbursement |
| 2 | amin-maju | Smoke test ✅ · Security done · Next: Hostinger deploy |
| 3 | cms-takaful | Priority 1–3 ✅ Deployed · Next: Priority 4 |
| 4 | win-board | Phase 3 stable · Next: Phase 4 Goal Cascade |
| 5 | takaful-content-planner | Blocked on Google OAuth |
| 6 | drtakaful | FAQPage schema ✅ · Next: Phase 3 retheme |

---
*Session: 2026-06-11 home PC — cleanup, 11 bugs fixed, archive/inactive, project staff assignment. Committed + pushed.*
