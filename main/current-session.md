# Current Session Memory - 2026-06-08
*Active working memory for current conversation*

## Session Context
**Session Type**: amin-maju — Full scaffold built + smoke-testing started (office laptop)
**Mood**: Productive — wonderful weekend just before this
**Last Active Project**: amin-maju (`D:\Kerja\Codes\amin-maju`)

---

## What Was Done (2026-06-08 Office Laptop Session)

### Projects Archived
- Project-B, rox-bot, bookkeeping (RezTax) — moved to `projects/archived/`

### amin-maju — New Project Built from Scratch

**Stack**: Laravel 12 · Tailwind v4 (CSS-first) · Alpine.js v3 · MySQL · Vite 7

**Full scaffold in one session:**
- Auth (login/logout only, owner creates accounts)
- Role-based access: owner / worker / bookkeeper via `EnsureRole` middleware
- 9 Models: Project (softDeletes), ProjectPhase, Task, Quotation, QuotationItem, InfoContact, Expense, ClientPayment, WorkerWage
- 9 Migrations (fixed ordering issue: quotation_items must come after quotations)
- 11 Controllers with full CRUD
- `ProjectPhaseSeeder` service — 9 default phases in BM, auto-seeded on project create
- 30+ Blade views — all in BM, Tailwind v4 styling
- Alpine.js: tab switching, dynamic quotation item rows, AJAX task checkbox toggle
- PDF quotation via `window.print()` (no Composer dep)
- P&L reports: per-project + overview

**Bugs Fixed This Session:**
1. Nested form bug → archive-on-save (separated archive form from edit form)
2. Migration order: `quotation_items` sorted before `quotations` alphabetically → fixed timestamp
3. Layout `x-data` missing `@props` → `$title` not injected
4. `layouts/` vs `components/layouts/` — Blade component lookup requires `components/layouts/`
5. Dashboard hardcoded zeroes → DashboardController passes live DB data
6. Task checkbox full page reload → AJAX fetch + Alpine reactive toggle
7. `@json()` with comma-containing expression → Blade `explode(',')` breaks it → moved map to controller
8. `@json($itemsData)` in HTML attribute → `"` breaks attribute → moved to `<script>` tag
9. Archived projects invisible → ProjectController::index() now passes `$archivedProjects` (onlyTrashed)
10. "Papan Pemuka" → "Dashboard"

**Smoke Test Status (at session end):**
- Auth ✅
- Projects (create, 9 phases, edit, archive/restore) ✅
- Tasks (AJAX checkbox toggle) ✅ — in progress
- Quotations (create, PDF) ✅ — edit fix applied, not yet re-tested
- Finance, Reports, Role restrictions — NOT YET TESTED

**Repo**: `https://github.com/farahanasuhaimi/amin-maju` (private)
**Local**: `D:\Kerja\Codes\amin-maju`
**DB**: `amin_maju` on local MySQL

---

## Next Up
1. Resume smoke test after lunch: Finance tab, Reports, Role restrictions (403 check)
2. Re-test quotation edit (script tag fix applied)
3. Update seed credentials to real names before production
4. Hostinger subdomain + auto-deploy setup

## Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | amin-maju | Scaffold complete — smoke-testing in progress |
| 2 | cms-takaful | Priority 1–3 ✅ Deployed. Next: Priority 4 |
| 3 | win-board | Phase 3 stable — Next: Phase 4 Goal Cascade |
| 4 | takaful-content-planner | Blocked on Google OAuth |
| 5 | drtakaful | FAQPage schema ✅ — Next: Phase 3 retheme |
| — | Project-B | ARCHIVED (Phase 4 GUI pending) |
| — | rox-bot | ARCHIVED (35% done) |
| — | bookkeeping (RezTax) | ARCHIVED (pre-deploy review needed) |

---
*Session: 2026-06-08 — office laptop. amin-maju built from scratch in one session.*
