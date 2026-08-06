# Caliora — Dentist & Dental Clinic HTML Template (Dubai edition)

Hand-coded, dependency-light HTML template for dental clinics. Structure and animation
choreography follow premium dentist-template conventions; all copy, code and design tokens
are original and written for **DHA/MOHAP advertising compliance** (no guarantees, no
superlatives, licence slots in the footer).

## Pages (17)

- `index.html` — 10-section home: condition hero slides, approach, treatments grid, circle CTA, features accordion, dark stats band, newsletter, featured blog, radial CTA, locations + footer with marquee wordmark
- `about.html`, `conditions.html`, `treatments.html`, `cases.html`, `equipment.html`, `blog.html`, `gallery.html`, `locations.html`, `contact.html`
- Detail samples: `treatment-detail.html`, `condition-detail.html`, `blog-post.html`, `location-detail.html`
- Utility: `style-guide.html`, `instructions.html`, `licenses.html`

## Animations (GSAP + ScrollTrigger via CDN)

Opt-in via data attributes — see `assets/js/main.js`:

| Attribute | Effect |
|---|---|
| `data-hero` / `data-hero-line` / `data-hero-fade` | Hero load choreography (bg settle, masked line reveal, staggered fades) |
| `data-reveal` | Fade-up on scroll (expo easing), optional `data-delay` |
| `data-reveal-mask` | Masked line slide-up |
| `data-stagger` | Staggered children reveal (cards, grids, lists) |
| `data-parallax` | Scrubbed cover-image parallax |
| `data-count` / `data-suffix` | Number counters |
| `.marquee` | Infinite footer wordmark ticker (slows on hover) |
| `.accordion` | Animated accordions (`data-accordion-open-first` opens item 01) |

Nav compacts on scroll; dropdown/mega menus on hover; mobile burger menu.
`prefers-reduced-motion` is fully respected.

## Customising

1. **Brand** — edit tokens at the top of `assets/css/main.css` (`--bg`, `--brand`, `--gold`, `--deep`…) — palette follows the taupe / navy scale (seeds `#8F7868` and `#0E3E68`), rename the logo text in nav/footer.
2. **Content** — replace copy, Unsplash placeholder images, and all statistics with your verified details.
3. **Compliance** — swap MOHAP/DHA licence placeholders in the footer; have your Medical Director approve final copy.
4. **Forms** — point form `action` attributes at your endpoint.
5. **Regenerate interior pages** (optional) — page shells are produced by `build-pages.py` (`python3 build-pages.py`), or edit the HTML directly.

No build step required — open `index.html` or serve the folder statically.
