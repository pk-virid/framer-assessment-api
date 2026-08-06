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

| Path | Purpose |
|------|---------|
| `/` | Home composition |
| `/about` | Clinic story + team |
| `/treatments` | CMS list |
| `/treatment/:slug` | CMS detail |
| `/conditions` | CMS list |
| `/condition/:slug` | CMS detail |
| `/cases` | Case studies (with consent + outcomes disclaimer) |
| `/case/:slug` | Case detail |
| `/blog` | Blog list |
| `/blog/:slug` | Blog detail |
| `/gallery` | Facility / non-GA imagery |
| `/equipment` | Technology |
| `/locations` | Dubai locations list |
| `/location/:slug` | Location detail |
| `/contact` | Form + FAQ |
| `/privacy` | Privacy |
| `/terms` | Terms |
| `/instructions` | Buyer setup + DHA checklist |
| `/style-guide` | Tokens, type, components |
| `/404` | Not found |

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

### Treatments
Fields: `title`, `slug`, `category` (ref Conditions), `summary`, `heroImage`, `body` (rich text), `process` (rich text), `limitations` (rich text), `faq` (JSON/rich), `order`

### Conditions
Fields: `title`, `slug`, `summary`, `heroImage`, `body`, `relatedTreatments` (multi-ref)

### Cases
Fields: `title`, `slug`, `treatment` (ref), `summary`, `heroImage`, `gallery`, `consentOnFile` (boolean), `disclaimer` (text), `body`  
*Default seed items keep `consentOnFile` false and show placeholder art — buyers only publish real cases with consent.*

### Blog Posts
Fields: `title`, `slug`, `category`, `excerpt`, `cover`, `readMinutes`, `body`, `publishedAt`

### Locations
Fields: `title`, `slug`, `address`, `area` (e.g. Jumeirah), `phone`, `email`, `hours`, `mapLink`, `image`

### Team
Fields: `name`, `dhaTitle`, `bio`, `photo`, `order`

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
