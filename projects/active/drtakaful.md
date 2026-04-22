# drtakaful - Dr Takaful Marketing Site
*Static HTML marketing site for Hana's Takaful consultancy practice*

## Project Overview
- **Type**: Static Website
- **Period**: Pre-2026-04-15 - Active
- **Tech Stack**: HTML + Tailwind CSS (CDN) + custom config (`src/tailwind-config.js`)
- **Theme**: Matcha × strawberry — DM Serif Display + DM Sans
- **Completion**: 50%
- **Duration**: 0 min

## Current Status
- **Last Session**: 2026-04-19 — Phase 2 complete (index.html fully rethemed)
- **Next Steps**: Phase 3 — retheme 6 tool/form pages
- **Known Issues**:
  - No auto-deploy — requires manual FTP/cPanel upload to web host
  - Hosting provider unknown (ask before setting up auto-deploy)

## Retheme Phase Tracker

| Phase | Scope | Status |
|-------|-------|--------|
| Phase 1 | `src/global.css` + `src/tailwind-config.js` | ✅ Done |
| Phase 2 | `index.html` (homepage) | ✅ Done |
| Phase 3 | Tool & form pages (6 files) | ⏳ Next |
| Phase 4 | Article/blog pages (~40 files) | ⏳ Pending |

## Phase 3 Files
- `kalkulator-hibah.html`
- `kalkulator-belanjawanku.html`
- `analisis-keperluan.html`
- `borang-permohonan.html`
- `borang-fact-finding-medical-card.html`
- `konsultasi-percuma.html`

## Session History (Last 5)

### 2026-04-19 — Phase 2 Complete
- **Changes**: All sections of index.html rethemed with brand tokens — zero generic grays remain. Sections: consultation form, featured case study, blog (30+ articles + badges), FAQ, tools grid, final CTA, footer, exit popup. Repo cleaned (5 Python scripts removed). README updated with brand token table + phase tracker. Mobile UX fix: removed redundant navbar WA pill.
- **Time Spent**: ~0 min

### 2026-04-15 — AI Content Generation Session
- **Changes**: DeepSeek API used for content generation via cms-takaful
- **Time Spent**: ~0 min

## Historical Summary
[No history yet — this section is populated when session count exceeds 5]

## Technical Notes
- **Repository**: github.com/farahanasuhaimi/drtakaful (version control only — no auto-deploy)
- **Local path**: `D:\WebDev\Takaful`
- **Deploy**: Manual upload to web host (FTP/cPanel) — files: `index.html`, `src/global.css`, `src/tailwind-config.js`
- **No build step** — Tailwind via CDN with custom config
- **Brand tokens**: Defined in `src/tailwind-config.js` — use tokens everywhere, no raw hex

---
**Last Updated**: 2026-04-23 | **Position**: #1/10 Active
