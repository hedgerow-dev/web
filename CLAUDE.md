# Hedgerow — Project Instructions

## Always reference the style guide

Full style guide: `C:\Users\cczin\OneDrive\Desktop\brand\graphics\styleguide.md`

Read it before making any design, copy, or branding decision. The rules below are a working summary. When in doubt, read the full guide.

---

## Brand in one line

Hedgerow is a calm, premium, technically credible security brand. Editorial restraint. Warm natural surfaces. Strong typographic core. Visual language built on structure and quiet protection.

---

## Colour palette

| Name | Hex | Use |
|---|---|---|
| Midnight | `#013D5A` | Primary — text, headings, nav, footer, dark panels |
| Lionsmane | `#FCF3E3` | Background — warm paper tone, card surfaces |
| Celeste | `#B0D3CE` | Secondary surface — cards, callout backgrounds |
| Herb | `#708C69` | Main accent — section labels, buttons, active states |
| Marigold | `#F4A25B` | Highlight only — use rarely, micro-accents only |

Current CSS variables in `hedgerow.css`:
- `--midnight: #013D5A` → `--navy`
- `--lionsmane: #FCF3E3` → `--card` (bg surface)
- `--moss-shadow: #374A30` → `--sage` (section labels)
- `--clay-warmth: #BA7650` → `--amber / --marigold`
- `--stone-grey: #8A857E` → `--faint / --muted`

The site should feel like Midnight + Lionsmane. Herb/Moss Shadow is the accent. Marigold/Clay Warmth is used sparingly.

---

## Typography

**Primary font stack:** `'Avenir Next', 'Avenir', 'Century Gothic', 'Montserrat', sans-serif`

Montserrat is loaded from Google Fonts as the web fallback.

**Rules:**
- One font family throughout — no decorative serifs, no Cormorant Garamond, no display fonts
- Weight and spacing contrast do the work, not multiple typefaces
- Headlines: bold (`700`), tight tracking (`-.04em`)
- Body: regular (`400`) or medium (`500`)
- Labels: uppercase, wide tracking (`.12–.14em`), small size (`.65–.7rem`)

**Logo mark:** `hr█.` in Avenir Next bold — this is a separate typographic object, not subject to the body font rule.

---

## Writing rules

**Always:**
- Specific over vague
- Direct over inflated
- Technical over trendy
- Describe behavior, scope, and operating model — not emotional outcomes
- Start with the claim, then support it
- 3–10 words in headlines when possible

**Never:**
- "Next-generation", "cutting-edge", "revolutionary", "seamless", "powerful"
- "Unlock the future", "AI security, reimagined", "empowering" language
- Generic cybersecurity fear copy
- Founder-myth storytelling in product materials
- Startup cliché phrasing

**Vocabulary to prefer:** runtime, enforcement, deterministic, auditable, source-level, explainable, on-premise, codebase, attack path, controls, exposure, regulated

**Messaging order for any page:**
1. What it is
2. What it does
3. Who it is for
4. Why it is different
5. Why it can be trusted

---

## Visual / design rules

- Left-align most content
- Generous spacing — let sections breathe
- No gradients, no glassmorphism, no glows
- No rounded bubbly UI (border-radius ≤ 6px is fine)
- No icon-in-circle feature grids
- Dark sections sparingly — for emphasis only
- Flat or near-flat surfaces, minimal shadows, subtle borders
- No shields, locks, padlocks, or security clichés in visuals

---

## Products

**Thicket** — Runtime security for AI applications. Four enforcement layers. Deterministic. No external API. No AI making blocking decisions. Works in air-gapped environments.

**Rowan** — Source code analysis for AI infrastructure. Cross-file taint analysis, AI-specific sink models, reachability-aware SCA, agentic hunt mode.

**Both:** Do not label either as "production-ready" or "in beta". Do not restrict to enterprise — any team can get in touch.

---

## Repository

- GitHub: `kennethkcox/hedgerow.dev`
- Firebase project: `hedgerow-acc` (acceptance)
- Contact: `hello@hedgerow.dev`
- Deploy: push to `master` → GitHub Actions → Firebase Hosting

---

## Key files

- `hedgerow.css` — shared design system (colours, typography, components)
- `home.css` — homepage-specific styles
- `thicket/product.css` — Thicket page styles
- `rowan/rowan.css` — Rowan page styles
- `nav.js` — shared nav toggle (no inline onclick anywhere)
- `.github/workflows/deploy-acc.yml` — Firebase deploy workflow
- `firebase.json` / `.firebaserc` — Firebase Hosting config
