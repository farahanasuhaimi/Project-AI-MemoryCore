# Dr Takaful Brand Kit
*Matcha × Strawberry — "Engineered for Legacy". Islamic credibility meets modern financial authority.*

## Identity

| Field | Value |
|-------|-------|
| Brand name | Dr. Takaful |
| Real name | Hana Suhaimi |
| Title | Life Planner & Takaful Consultant |
| Company | AIA Public Takaful |
| Tagline | *"Engineered for Legacy"* |
| Positioning | Jurutera Kewangan — bukan jurujual |
| Website | drtakaful.com |
| Biolink | beacon.drtakaful.com |
| WhatsApp | +6013-252 2587 / https://wa.me/60132522587 |
| Instagram | @nufas → https://instagram.com/nufas |

## Color Palette

| Role | Color Name | Hex | CSS Variable |
|------|------------|-----|--------------|
| Primary | Matcha Deep | `#3D6B4F` | `--matcha-deep` |
| Secondary | Matcha Mid | `#6A9E7B` | `--matcha-mid` |
| Border / Divider | Matcha Light | `#C2DBC9` | `--matcha-light` |
| Light BG | Matcha Pale | `#EBF4EE` | `--matcha-pale` |
| Accent / CTA | Strawberry | `#D93057` | `--strawberry` |
| Soft Pink BG | Berry Blush | `#F5B8C8` | `--berry-blush` |
| Page Background | Cream | `#F8F5EF` | `--cream` |
| Premium Accent | Gold | `#C9A84C` | `--gold` |
| Text Primary | Ink | `#1A1A18` | `--ink` |
| Text Secondary | Ink Soft | `#4A4A46` | `--ink-soft` |
| Captions | Ink Muted | `#8A8A84` | `--ink-muted` |

### CSS Variables (copy-paste ready)
```css
:root {
  --matcha-deep:  #3D6B4F;
  --matcha-mid:   #6A9E7B;
  --matcha-light: #C2DBC9;
  --matcha-pale:  #EBF4EE;
  --strawberry:   #D93057;
  --berry-blush:  #F5B8C8;
  --cream:        #F8F5EF;
  --gold:         #C9A84C;
  --ink:          #1A1A18;
  --ink-soft:     #4A4A46;
  --ink-muted:    #8A8A84;
}
```

### Colour Usage Rules
- **Matcha Deep** → trust, Islamic credibility, authority, headings
- **Strawberry** → CTA buttons, urgency hooks, emotional triggers
- **Gold** → premium positioning, PhD / credentials, highlights
- **Cream** → page background (never pure white — too clinical)
- Never use `#000000` — use `--ink` instead
- Never use generic purple gradients or blue as primary

## Typography

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

font-family: 'DM Serif Display', serif;  /* Headlines, brand name, quotes */
font-family: 'DM Sans', sans-serif;      /* Body, labels, UI text */
```

| Role | Font | Size | Weight |
|------|------|------|--------|
| Brand / Hero | DM Serif Display | 28–32px | normal (italic for emphasis) |
| Section heading | DM Serif Display | 20–24px | normal |
| Body | DM Sans | 14–15px | 400 |
| Label / caption | DM Sans | 10–12px | 500, uppercase, letter-spacing 0.1em |
| Micro / badge | DM Sans | 10px | 500 |

## Component Styles

### Brand Pill
```html
<div style="display:inline-flex;align-items:center;gap:6px;background:var(--matcha-deep);color:var(--matcha-pale);font-size:10px;font-weight:500;letter-spacing:0.12em;text-transform:uppercase;padding:4px 12px;border-radius:20px;">
  <span style="width:6px;height:6px;border-radius:50%;background:var(--gold);flex-shrink:0;display:inline-block;"></span>
  AIA Public Takaful
</div>
```

### Primary CTA Button (WhatsApp)
- Background: `var(--strawberry)`
- Border-radius: 14px
- Min-height: 64px (mobile touch target)
- Box-shadow: `0 4px 20px rgba(217,48,87,0.25)`
- Label: **"WhatsApp Hana"** (not "Dr. Hana")
- Pre-filled message:
  ```
  https://wa.me/60132522587?text=Assalamualaikum%20Dr.%20Hana%2C%20saya%20nak%20tahu%20lebih%20lanjut%20tentang%20takaful.%20Boleh%20bantu%3F
  ```

### Link Cards
```css
background: white;
border: 1px solid rgba(0,0,0,0.07);
border-radius: 14px;
min-height: 60px;
/* Hover */ border-color: var(--matcha-light); transform: translateY(-1px);
/* Active */ transform: scale(0.98);
/* Arrow */ color: var(--ink-muted); content: "→";
```

### Icon Backgrounds
```css
.icon-green { background: var(--matcha-pale); }   /* Main site / calculators */
.icon-red   { background: #FDF0F3; }               /* CI / urgency */
.icon-gold  { background: #FBF5E6; }               /* Hibah / legacy */
```

### Tool Cards (2-column grid)
- Use coloured dot indicators (8×8px, border-radius 50%) instead of emoji
- Dot colours: matcha-mid (calculators), gold (financial tools), strawberry (CTA)
- Min-height: 88px

### Badges
```css
.badge-green { border-color: var(--matcha-mid);   color: var(--matcha-deep); background: var(--matcha-pale); }
.badge-red   { border-color: var(--berry-blush);  color: var(--strawberry);  background: #FDF0F3; }
.badge-gold  { border-color: var(--gold);         color: #7A5E1A;            background: #FBF5E6; }
```

### Divider
```html
<div style="display:flex;align-items:center;gap:10px;margin:22px 0 18px;">
  <div style="flex:1;height:1px;background:var(--matcha-light);"></div>
  <span style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-muted);">Section Label</span>
  <div style="flex:1;height:1px;background:var(--matcha-light);"></div>
</div>
```

### Quote Block
```html
<div style="background:var(--matcha-deep);border-radius:14px;padding:20px;text-align:center;">
  <p style="font-family:'DM Serif Display',serif;font-size:15px;color:var(--matcha-pale);font-style:italic;line-height:1.6;">
    "Sistem perlindungan terbaik adalah sistem yang dipasang sebelum ianya diperlukan."
  </p>
  <span style="font-size:10px;letter-spacing:0.1em;text-transform:uppercase;color:var(--matcha-light);">
    Dr. Takaful · Engineered for Legacy
  </span>
</div>
```

## Background Decorative Elements

```css
/* Top-right matcha orb */
body::before {
  content: ''; position: fixed;
  top: -120px; right: -120px;
  width: 400px; height: 400px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--matcha-light) 0%, transparent 70%);
  opacity: 0.45; pointer-events: none; z-index: 0;
}
/* Bottom-left strawberry orb */
body::after {
  content: ''; position: fixed;
  bottom: -80px; left: -80px;
  width: 300px; height: 300px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--berry-blush) 0%, transparent 70%);
  opacity: 0.35; pointer-events: none; z-index: 0;
}
```

## Mobile Rules (always apply)

```css
* { -webkit-tap-highlight-color: transparent; }

.wrap { width: 100%; max-width: 420px; padding: 0 16px; }

/* Touch targets */
/* CTA: min-height 64px | Link cards: 60px | Tool cards: 88px | Social: 48px */

@media (max-width: 380px) {
  .header { padding-top: 36px; }
  h1 { font-size: 24px; }
  p.tagline { font-size: 12px; }
}
```

## Animations

```css
.fade-up { opacity: 0; transform: translateY(16px); animation: fadeUp 0.5s ease forwards; }
@keyframes fadeUp { to { opacity: 1; transform: translateY(0); } }

.delay-1 { animation-delay: 0.08s; }
.delay-2 { animation-delay: 0.16s; }
.delay-3 { animation-delay: 0.24s; }
.delay-4 { animation-delay: 0.32s; }
.delay-5 { animation-delay: 0.40s; }
.delay-6 { animation-delay: 0.48s; }
```

## Tone & Copy Rules

- Brand name: **Dr. Takaful** (with period)
- CTA / button label: **Hana** (not "Dr. Hana", not "Farahana")
- Language: Bahasa Malaysia + natural Manglish — casual but credible
- Emoji: only in Perlindungan/product sections; avoid in tools, social, footer
- No hard-sell — use scenario framing: *"Kalau hari ni kita takde, siapa yang tanggung?"*
- Positioning line: *"Jurutera Kewangan anda — bukan jurujual"*

## Key Pages

| Page | URL |
|------|-----|
| Main site | https://drtakaful.com |
| Biolink | https://beacon.drtakaful.com |
| Hibah Calculator | https://drtakaful.com/kalkulator-hibah.html |
| Belanjawanku | https://drtakaful.com/kalkulator-belanjawanku.html |
| Analisis Form | https://drtakaful.com/analisis-keperluan.html |
| Apply Form | https://drtakaful.com/borang-permohonan.html |
| MC Fact Finding | https://drtakaful.com/borang-fact-finding-medical-card.html |

## Projects Using This
- drtakaful.com (main marketing site) — `D:\WebDev\Takaful`
- beacon.drtakaful.com (biolink)
- cms-takaful (CRM at list.drtakaful.com)

---
*Documented: 2026-04-19*
