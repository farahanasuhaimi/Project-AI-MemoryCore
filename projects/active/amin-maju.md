---
project: amin-maju
status: active
started: 2026-06-08
last_updated: 2026-06-10
---

# amin-maju — Home Contractor Management System

## Purpose
Bookkeeping + project management app for Kak Amin's home contractor business. Built by Nufa to help sister manage projects from land purchase to key handover.

## Users
| Role | Person |
|------|--------|
| Owner | Kak Amin (sister) |
| Worker | Husband |
| Bookkeeper | Nufa |

## Stack
Laravel 12 · PHP 8.2 · Tailwind v4 · Alpine.js v3 · MySQL · Vite 7 · Hostinger

## Current State (2026-06-10)
- Full smoke test complete — all 4 phases passed (subagent-verified)
- P1 security fixes applied: IDOR ownership checks, XSS (Js::from), session fixation, self-deactivation guard
- P2 fixes applied: dashboard balance scoped to active projects, worker task access, login throttle, Finance delete buttons, Kenalan auto-save flash
- P3 polish applied: Saturday end-of-week, DB transaction on project create, contacts.type enum, quotation task link on update, checkbox old() fix
- All fixes committed + pushed (commits: a035a9f, b04ded8, 64bc8b0)
- Hostinger deploy: NOT yet configured

## What's Built
| Module | Status |
|--------|--------|
| Auth — login, logout, remember me, inactive guard | ✅ |
| Role system — owner / worker / bookkeeper | ✅ |
| Projects — CRUD, archive/restore, 9 auto-seeded phases | ✅ |
| Phases — rename inline (Alpine AJAX), status toggle, reorder | ✅ |
| Tasks — CRUD, AJAX checkbox, type: general/quotation/info-gathering | ✅ |
| Quotations — outgoing + incoming, line items, PDF print, status flow | ✅ |
| Contact Timeline (InfoContact) — log per project, auto-save to Kenalan | ✅ |
| Contact Directory (Kenalan) — standalone directory, linked to InfoContact | ✅ |
| Finance — Expenses, ClientPayments (milestone-based), WorkerWages | ✅ |
| Milestone Labels — per-project custom label overrides (stored as JSON) | ✅ |
| Project Summary Bar — contract value, received, outstanding, expenses, dijangka terima | ✅ |
| P&L Reports — per-project + business overview | ✅ |
| Dashboard — owner task board (now/this week/next week), worker task list, bookkeeper finance summary | ✅ |
| Primavera Tier 1 — phase progress bar, overdue badge, schedule pill | ✅ |
| PWA — installable on Android/iOS (standalone mode) | ✅ |
| User management — owner only, invite-style with is_active toggle | ✅ |

## Next Steps
1. **Hostinger subdomain + auto-deploy setup** — app is smoke-tested and ready
2. **Change seed credentials** to real user data before production seed
3. Review P2-2 (potential sub-contractor double-count in totalExpenses) with Kak Amin

## Repo
GitHub private: `amin-maju`
Local: `D:\Kerja\Codes\amin-maju`
