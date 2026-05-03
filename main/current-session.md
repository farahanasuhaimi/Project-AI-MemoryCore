# Current Session Memory - 2026-05-03
*Active working memory for current conversation*

## Session Context
**Session Type**: Work — drtakaful.com SEO + AI-SEO campaign
**Current Project**: drtakaful — `D:\WebDev\Takaful`
**Status**: win-board fully synced (GitHub + Hostinger) ✓. FAQPage schema campaign in progress on drtakaful.

## Active Project
- **Name**: drtakaful.com
- **Location on this PC**: `D:\WebDev\Takaful`
- **GitHub**: `https://github.com/farahanasuhaimi/drtakaful`
- **Live URL**: `https://drtakaful.com`
- **Audit Doc**: `docs/seo-article-audit.md`

## Working Memory

### drtakaful — FAQPage Schema Campaign Progress

**Goal**: Add FAQPage schema to all articles for AI-SEO (Google AI Overviews, Perplexity, ChatGPT Search)

**Pattern used** — insert as 3rd object in `@graph` array before closing `]`:
```json
    },
    {
      "@type": "FAQPage",
      "@id": "https://drtakaful.com/[filename]#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "...",
          "acceptedAnswer": { "@type": "Answer", "text": "..." }
        }
      ]
    }
```

**Completed (9 articles)**:
- [x] `simpanan-vs-takaful.html` — duplicate resolved, FAQPage added, CDN fixed, dark-card heading fix
- [x] `panduan-lengkap-medical-card-takaful.html` — year refresh + FAQPage
- [x] `panduan-lengkap-medical-card-2026.html`
- [x] `medical-card-atau-ci-dulu.html`
- [x] `perkeso-vs-takaful-medical-card.html`
- [x] `panduan-lengkap-penyakit-kritikal-takaful.html`
- [x] `harta-beku-dan-hibah-takaful.html`
- [x] `tempoh-menunggu-medical-card.html`
- [x] `socso-vs-takaful-penyakit-kritikal.html`
- [x] `beza-medical-card-vs-pelan-penyakit-kritikal.html`

**Next in queue** (from audit priority list):
- [ ] `kenapa-takaful-penting.html`
- [ ] `takaful-vs-insurans.html`
- [ ] `panduan-lengkap-hibah-takaful.html`
- [ ] `formula-10-peratus-pendapatan-takaful.html`
- [ ] `kenapa-perlu-rancang-kewangan-awal.html`
- [ ] ... (continue down `docs/seo-article-audit.md`)

**Other pending**:
- Fix weak titles: hibah (English), formula-10 (branded), kenapa-rancang (generic)
- Add schema to 7 no-schema tool/form pages
- simpananvstakaful.html → remove after 30 days from redirect (after ~2026-06-01)
- Update `docs/seo-article-audit.md` as items completed

### Key Technical Notes
- **CDN Tailwind**: `https://cdn.tailwindcss.com` — ALWAYS keep. `src/tailwind-config.js` is theme-only, not a replacement.
- **Heading visibility**: `prose-headings:text-gray-900` cascades into dark cards — always add explicit `text-white` on headings inside `bg-gray-900`/dark containers.
- **Canonical URL pattern**: `https://drtakaful.com/` lowercase per sitemap.xml (existing schemas use mixed-case `DrTakaful.com` — leave as-is unless doing full file rewrite)

### Project Portfolio
| Pos | Project | Status |
|-----|---------|--------|
| 1 | win-board | Phase 2 + polish complete — fully synced (GitHub + Hostinger) ✓ |
| 2 | drtakaful | FAQPage schema campaign in progress (9/~30 done) |
| 3 | rox-bot | Dynamic CAPTCHA detection done — test_ocr.py run needed |
| 4 | cms-takaful | Built — awaiting deploy |

## Session Recap (For AI Restart)
- **User**: Nufa (Farahana Suhaimi) — Takaful Consultant + Data Engineer, PhD (CNN)
- **This PC**: `D:\WebDev\` — main dev machine with GPU
- **win-board**: Fully synced — no further work needed
- **drtakaful**: FAQPage schema campaign started. 9 articles done. Resume from `kenapa-takaful-penting.html`
- **Working style**: "do it one by one" — each article committed and pushed before moving to next. "go" = proceed.

## Session Memory Limit
- **Maximum**: 500 lines
- **Reset Behavior**: RAM-style reset preserving only Session Recap
- **Format Reference**: See `main/session-format.md` for rebuild structure

---
*Session updated: 2026-05-03 — 20:09*
