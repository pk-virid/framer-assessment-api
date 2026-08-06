# Caliora structural blueprint — exact clone spec

Source of truth for the Framer rebuild. Structure, section order, element composition and
navigation conventions mirror the Caliora Webflow template 1:1. **Copy, brand name, logo and
imagery are original** (DHA-compliant deck in `COPY-DECK.md`) — only layout conventions are cloned.

## Site map (target)

Primary: `/` · `/about` · `/conditions` · `/treatments` · `/cases` · `/equipment` · `/blog` · `/gallery` · `/contact` · `/locations`
Detail (CMS): `/condition/:slug` (4) · `/treatment/:slug` (8) · `/blog/:slug` (6) · `/location/:slug` (2)
Utility: `/style-guide` · `/instructions` · `/licenses`
Variant: `/home-dark` (dark-theme duplicate of Home)

## Navigation (fixed top bar)

- Left: logo mark + brand name + small slogan line under name
- Links row:
  1. **Pages** — mega-menu listing every page
  2. **Conditions** — dropdown, 4 condition links each with 1-line description
  3. **Treatments** — dropdown, 8 treatment links
  4. **Locations** — dropdown, 2 location links
- Right: primary CTA button → `/contact` (ours: "Book a consultation")

## Section themes (tokens)

`light-strong` `light-subtle` `default` `dark-subtle` `dark-base` `dark-strong` `transparent` —
plus `no-paddings` / `no-padding-bottom` / `is-cta-section` modifiers. Map to our Brand tokens.

## Home — 10 sections in order

| # | Theme | Block | Composition |
|---|-------|-------|-------------|
| 1 | no-paddings | **Condition hero** | Full-viewport CMS listing over cover images; per condition: H1/heading, paragraph, related-treatments link list with icons |
| 2 | light-subtle | **Approach intro** | Eyebrow label, oversized heading, primary button (bg animation on hover) |
| 3 | no-padding-bottom | **Popular treatments grid** | Section title; CMS grid of treatment cards — media, tag pill, hover overlay w/ reveal image, content, action button |
| 4 | default | **CTA circle** | Fluid heading, large arrow-link w/ underline, image cluster arranged in circle + brand symbol at centre, 2 rotating circle borders |
| 5 | light-strong | **Features accordion** | 2-col: title + paragraph left; numbered accordion list right (01–04, toggle icon, dropdown body) |
| 6 | dark-subtle | **Stats band** | Heading; CMS stats: image column + stat items (logo symbol, paragraph, label, large number) |
| 7 | light-strong | **Newsletter** | Centered heading (max-width), email field + submit, success/error states |
| 8 | light-strong | **Featured blog** | Heading; 1 large featured card (gradient over image) + column of small cards |
| 9 | is-cta-section | **Radial CTA** | Radial background text ring; heading + large arrow-link; 2 images; checklist of feature bullets |
| 10 | no-paddings | **Locations + footer** | Locations list (title, address, opening hours) over parallax image; footer: brand col, explore links, utility links (Style guide / Instructions / Licences), social icons, giant marquee wordmark |

## About

hero title band → stats strip → full-bleed image + counters → values list (icon list items) →
team CMS strip → CTA circle → story split sections → dark team/join band → FAQ/values →
locations + footer.

## Conditions (listing)

Full-viewport CMS condition listing (same block as home hero) → intro band → radial CTA → dark marquee band + footer.

## Condition detail

Split content (sticky sidebar + rich body, eyebrow labels) → image trio band → dark CMS band
(related treatments) → 5-part CMS gallery/detail sections → contact form band → footer.

## Treatments (listing)

Dark hero with full CMS treatment card grid → tabs band (pricing/booking info + 2 forms) →
slider showcase (5 sliders) → CTA + marquee footer.

## Treatment detail

Dark hero w/ cover + stat → split content (sticky sidebar) → image trio → radial CTA →
before/after band → form + related CMS + footer.

## Cases

Hero + CMS case grid with before/after stats → CTA circle → icon list band → tabs + forms + footer.

## Equipment

CMS equipment grid w/ icon lists → image band w/ stats → accordion + stats + footer.

## Gallery

CMS gallery grid → dark CMS band → stats + footer.

## Blog

Featured blog section (large + small cards) → category band → full post grid → newsletter + footer.

## Blog post

Split content (sticky meta sidebar + rich text) → newsletter band → related posts + footer.

## Locations

CMS locations listing → contact form band → map/image band → newsletter + footer.

## Location detail

Cover CMS hero → split content (address, hours, parking, transit eyebrow rows) → team/services
band → contact form → accordion + stats + footer.

## Contact

Contact form band (eyebrow rows: phone, email, address, hours; form right) → locations CMS →
FAQ accordion + stats → gallery/stats + marquee footer.

## Style guide

Token sheet: colors, type scale (H1–H6, body sizes), labels, buttons, section themes
(light-subtle → dark-strong swatch bands), spacing, components + footer.

## Instructions

Single rich-text section: how to customise the template + footer.

## CMS model (target)

| Collection | Items | Notes |
|---|---|---|
| Conditions | 4 | cosmetic, restorative, implantology, orthodontics |
| Treatments | 8 | emergency, general/prevention, veneers, whitening, crowns-bridges, ceramic-lingual braces, invisalign, implants |
| Blog | 6 | own DHA-safe educational posts |
| Cases | 6+ | before/after with stats |
| Equipment | 4+ | clinic technology items |
| Gallery | 8+ | clinic imagery |
| Locations | 2 | ours: Dubai (Jumeirah), Dubai (Downtown) — replaces NY/Miami |
| Team | 3+ | clinicians (reuse existing Clinicians) |
| Stats | 4 | numbers band (DHA-safe, buyer-editable placeholders) |
| FAQs | 4+ | accordion content |

Copy rules: everything from `COPY-DECK.md` + `DHA-COMPLIANCE.md`. No guarantees/superiority
claims, no fabricated KPIs — stats ship as clearly-editable placeholders.
