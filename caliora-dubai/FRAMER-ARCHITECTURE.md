# Framer-native architecture (sellable template)

Rebuild Caliora as **native Framer** — no Webflow embed, no exported HTML shell. Buyers edit on canvas + CMS.

## Design tokens

| Token | Value (starter) | Notes |
|-------|-----------------|-------|
| `--bg` | `#F7F4EF` warm stone | Avoid purple/cream AI clichés; refined clinic light |
| `--ink` | `#14201C` deep pine | |
| `--muted` | `#5C6B64` | |
| `--brand` | `#0F6B5C` dubai teal | Primary actions |
| `--brand-2` | `#C4A574` soft sand gold | Accents only |
| `--surface` | `#FFFFFF` | |
| `--line` | `#D9E0DC` | |
| Display font | Fraunces or similar serif via Framer fonts | Expressive, not Inter |
| Body font | Geist or DM Sans | |

Breakpoints: Desktop 1200 · Tablet 810 · Phone 390 (Framer defaults ok).

Motion (2–3 intentional): hero fade/rise, section reveal on scroll, nav/CTA hover — subtle, clinical, not glow-heavy.

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

- `Nav` — logo, links, Book consultation; mobile sheet
- `Footer` — nav, locations, MOHAP + DHA licence slots, disclaimer
- `Button` / `TextLink` — primary, secondary, ghost
- `SectionHeading` — eyebrow + title + support
- `TreatmentCard`, `ConditionCard`, `PostCard`, `LocationCard`
- `StatRow` — editable stats (no fake defaults locked in)
- `FeatureList` — numbered 1–4
- `Testimonial` — experience-only + consent note
- `DisclaimerBar` — outcomes vary
- `LicenceStrip` — MOHAP / DHA numbers
- `ContactForm` — Framer Form with compliant microcopy
- `CTABand` — closing consultation CTA

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
