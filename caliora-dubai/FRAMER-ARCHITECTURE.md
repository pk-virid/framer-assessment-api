# Framer-native architecture (AED 15,000 sellable template)

Rebuild Caliora as **native Framer** — no Webflow embed, no exported HTML shell. Buyers edit on canvas + CMS.

**Commercial bar:** AED 15,000. Craft and motion must read as private-clinic luxury. Full motion system: [`PREMIUM-MOTION.md`](./PREMIUM-MOTION.md).

## Design tokens

| Token | Value (starter) | Notes |
|-------|-----------------|-------|
| `--bg` | `#F3EEE6` limestone | Warm, gallery-like; not generic cream cliché |
| `--bg-deep` | `#0E1714` | Dark bands / home-dark optional page |
| `--ink` | `#101A17` deep pine | |
| `--muted` | `#5E6D66` | |
| `--brand` | `#0B5F52` dubai teal | Primary actions |
| `--brand-soft` | `#DCEDEA` | Soft fills, hover washes |
| `--brand-2` | `#B8956C` sand gold | Hairlines, numerals, rare ornament |
| `--surface` | `#FFFAF5` | |
| `--line` | `#D5DDD8` | |
| Display font | Fraunces (or equivalent serif) | Large, calm, high contrast |
| Body font | Neue Haas / DM Sans / similar grotesque | Not Inter as the brand voice |

Breakpoints: Desktop 1440 artboard · 1200 content · Tablet 810 · Phone 390.

Spacing scale: 8 / 16 / 24 / 40 / 64 / 96 / 128 / 160 — section padding desktop **128–160px**.

## Pages

Canonical IA: [`SITE-IA.md`](./SITE-IA.md) (aligned to [Sensate Dental OS](https://sensatedentalos.framer.website/) + your primary nav).

### Primary nav
| Path | Purpose |
|------|---------|
| `/` | Home composition |
| `/about` | Clinic story + approach |
| `/treatments` | CMS list |
| `/treatments/:slug` | Treatment detail |
| `/conditions` | CMS list |
| `/conditions/:slug` | Condition detail |
| `/symptoms` | CMS A–Z list |
| `/symptoms/:slug` | Symptom detail |
| `/membership` | Plans + compare CTA |
| `/membership/:slug` | Optional plan detail |
| `/offers` | CMS promotions |
| `/offers/:slug` | Offer detail + terms |
| `/contact` | Contact Us form + FAQ + locations |

### Authority + marketplace (secondary / footer)
| Path | Purpose |
|------|---------|
| `/articles` | Patient education list |
| `/articles/:slug` | Article detail (author + medical reviewer) |
| `/clinicians` | Named DHA-licensed profiles |
| `/clinicians/:slug` | Clinician detail |
| `/learn` | Topic hubs |
| `/learn/:slug` | Hub detail |
| `/privacy` · `/terms` | Legal |
| `/instructions` | Buyer + DHA setup |
| `/style-guide` | Design system |
| `/search` | Optional site search |
| `/404` | Not found |

### Optional funnels
`/funnel/new-patient`, `/funnel/smile-makeover`, `/symptoms/check`

## Shared layout components

- `Nav` — logo, links, Book consultation; scroll-compact + mobile clip sheet
- `Footer` — nav, locations, MOHAP + DHA licence slots, disclaimer
- `Button` / `TextLink` — variants Default/Hover/Pressed/Focus; arrow micro-motion
- `MagneticButton` *(optional code)* — ≤8px desktop magnetism for hero/closing CTA
- `MaskedHeadline` *(optional code)* — line-mask reveal for heroes
- `SectionHeading` — eyebrow + title + support with appear cascade
- `TreatmentRow` — editorial image/type swap (not cheap card grid)
- `ConditionCard`, `PostCard`, `LocationCard` — interaction cards only where lists need them
- `StatRow` — editable stats (defaults empty / tasteful placeholders; count-up off by default)
- `FeatureList` — numbered 1–4 with rule draw-in
- `Testimonial` — experience-only + consent note
- `DisclaimerBar` — outcomes vary
- `LicenceStrip` — MOHAP / DHA numbers
- `ContactForm` — Framer Form with compliant microcopy + refined focus
- `CTABand` — closing consultation CTA with premium hover
- `PageShell` — layout template for shared Nav/Footer + page effects

## Motion package (non-negotiable for price)

See `PREMIUM-MOTION.md`. Minimum ship set:

1. Hero load choreography (brand → masked title → support → CTAs)
2. Sitewide scroll reveals with stagger
3. Image scale-settle + subtle parallax
4. Nav scroll-compact + link underline draw
5. Button variant polish
6. Page transitions via Page Effects
7. FAQ height animation
8. `prefers-reduced-motion` fallbacks

## CMS collections

Full field lists: [`SITE-IA.md`](./SITE-IA.md).

| Collection | Route | Notes |
|------------|-------|-------|
| Treatments | `/treatments/:slug` | + related conditions/symptoms/articles |
| Conditions | `/conditions/:slug` | + when-to-seek-care |
| Symptoms | `/symptoms/:slug` | Educational urgency note; not diagnosis |
| Articles | `/articles/:slug` | Author + medical reviewer + reviewedAt |
| Offers | `/offers/:slug` | Terms + MOHAP note; no bait claims |
| Membership Plans | `/membership/:slug` | Single / Family / Corporate pattern |
| Clinicians | `/clinicians/:slug` | DHA title + licence placeholder |
| Topic Hubs | `/learn/:slug` | Groups the content graph |
| Locations | contact cards / optional CMS | Dubai areas |

Detail pages share: medical review strip, related graph, consultation CTA, outcomes/licence footers.

## Forms & interactions

- Contact form → Framer Form email notification
- Newsletter → optional Form or embed slot
- Smooth page transitions via Framer page effects (supported in July 2026 agent update)
- A11Y: button names, alt text on images, focus states, sufficient contrast

## Marketplace readiness checklist

- [ ] No lorem / “click to edit” leftovers  
- [ ] Home, Terms, Privacy present  
- [ ] All nav links resolve  
- [ ] Phone + desktop breakpoints reviewed  
- [ ] Alt text on key images  
- [ ] Licence + disclaimer slots visible  
- [ ] Instructions page for buyers  
- [ ] Style guide page  
- [ ] CMS sample content DHA-safe  

## Reference structure (Caliora → Framer mapping)

| Caliora (Webflow) | Framer |
|-------------------|--------|
| Conditions CMS | Conditions collection |
| Treatments CMS | Treatments collection |
| Locations NY/Miami | Locations Dubai ×2 |
| Cases / Gallery | Cases + Gallery pages w/ disclaimers |
| Components in Designer | Framer Components + variants |
| Style guide | `/style-guide` |
| Lenis smooth scroll | Framer scroll / page effects |
