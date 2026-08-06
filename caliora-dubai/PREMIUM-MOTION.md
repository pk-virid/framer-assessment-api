# Premium motion & craft system — AED 15,000 tier

Caliora Dubai must feel like a private clinic brand site, not a marketplace starter. Motion is the product differentiator: **quiet, expensive, inevitable** — never playful, never glow-heavy, never “AI template.”

Pricing bar: if a Dubai clinic medical director and marketing lead open the preview, the first 5 seconds must justify fifteen thousand dirhams.

---

## Motion philosophy

1. **Restraint over spectacle** — one clear motion idea per section; no overlapping gimmicks.
2. **Material feel** — ease curves mimic physical weight (inertia in, soft settle out).
3. **Editorial timing** — headlines resolve before body; imagery breathes after type.
4. **Scroll as cinematography** — progress-linked opacity/translate/scale, not bounce.
5. **Interaction as polish** — CTAs and nav feel magnetic and precise at 60fps.
6. **Clinical calm** — no neon glows, no springy emoji motion, no purple gradients.

### Global easing & duration tokens

| Token | Value | Use |
|-------|-------|-----|
| `ease-out-expo` | `cubic-bezier(0.16, 1, 0.3, 1)` | Entrances, reveals |
| `ease-in-out-soft` | `cubic-bezier(0.45, 0, 0.55, 1)` | Scroll-linked, page transitions |
| `ease-out-quart` | `cubic-bezier(0.25, 1, 0.5, 1)` | Hovers, micro |
| `dur-micro` | 180–220ms | Button/nav hover |
| `dur-ui` | 320–420ms | Cards, menus |
| `dur-section` | 700–1100ms | Scroll reveals |
| `dur-hero` | 1100–1600ms | Hero choreography |
| `stagger` | 60–90ms | List/children |

Reduced motion: honor `prefers-reduced-motion` — fade only, no large translate/parallax.

---

## Mandatory sitewide motions (ship all)

### 1. Hero choreography (first viewport)
Sequence on load (desktop):
1. Ambient image: slow ken-burns (scale 1.0 → 1.06 over ~12s, loop-free once) + subtle vignette
2. Brand mark: fade + 12px rise, 0ms delay
3. Headline: **masked line reveal** (clip-path / overflow mask), 120ms after brand
4. Support line: fade/rise, 180ms after headline completes
5. CTA group: fade/rise + hairline underline draw on secondary link, 120ms after support
6. Scroll cue: opacity pulse 0.35→0.7, 2.4s loop, very soft

No badges, chips, or stats in the hero.

### 2. Scroll reveals (every major section)
- Section eyebrow → title → support → content, staggered
- Distance: 24–36px rise (desktop), 16–24px (mobile)
- Trigger: when ~15–20% of section enters viewport
- Once only (no re-play spam on scroll up), except optional parallax layers

### 3. Image treatment
- Enter: scale 1.04 → 1.0 + fade, `dur-section`
- Optional parallax: image moves at 0.15–0.25 of scroll speed (subtle)
- Hover (where interactive): 1.0 → 1.03 scale, 420ms, overflow clip
- Never harsh zoom or blur gimmicks

### 4. Navigation
- Arrival: bar fades in after hero brand (or solid from first paint on inner pages)
- Scroll: compact height + backdrop blur/tint after 24px (smooth, not snap)
- Link hover: opacity 0.55→1 + 12–16px underline draw from left
- Mobile menu: full-bleed panel, clip reveal from top, staggered links (70ms)
- CTA in nav: fill softens + 1px lift (`translateY(-1px)`), no shadow stacks

### 5. Primary button (component variants)
Variants: `Default` · `Hover` · `Pressed` · `Focus`
- Hover: background shift 4–6% darker/lighter + label tracking +0.01em + arrow nudges 4px
- Pressed: scale 0.985
- Focus: 2px brand ring, accessible
- Arrow icon: independent 180ms ease-out-quart

### 6. Treatment / content rows
Inspired by Caliora’s stacked treatment storytelling:
- Active row expands or crossfades image (shared element feel)
- Inactive rows: opacity 0.45–0.6
- Index numerals: count or fade with 80ms stagger
- Horizontal rule: scaleX 0→1 from left as row enters

### 7. Page transitions
- Exit: opacity 1→0 + 8–12px rise, 280ms
- Enter: opacity 0→1 + 12px rise, 420ms delayed 80ms
- Keep shared Nav/Footer mounted (layout template) so only page body transitions

### 8. Footer arrival
- Licence strip and disclaimer fade last (compliance readable, not theatrical)
- Location columns stagger 70ms

---

## Elevated motions (include for AED 15k feel)

| Motion | Where | Spec |
|--------|-------|------|
| Headline mask reveal | Home, About, Treatments heroes | Per-line clip, 0.8–1.1s expo |
| Magnetic CTA | Hero + closing band | Cursor influence ≤8px desktop only |
| Smooth scroll feel | Sitewide | Framer smooth scroll / page effects; no janky Lenis embed hacks |
| Ticker (optional) | Below approach or equipment | Pause on hover; overflow lint-safe; slow 28–40s loop; clinic values words only (no medical hype) |
| FAQ accordion | Contact | Height animate 320ms; chevron rotate 180° |
| Form focus | Contact | Field border color brand, 180ms; error shake max 4px once |
| Case gallery | Cases | Crossfade 500ms; disclaimer always visible before imagery |
| Marquee-free stats | About | Numbers optional soft count-up **only** for buyer-editable verified figures; default off |

---

## Explicitly banned (cheapens a 15k template)

- Purple glow / neon / glassmorphism stacks
- Bounce/spring everywhere
- Auto-playing loud video backgrounds in hero
- Confetti, cursor trails, particle swarms
- Stat counters with fake “8400+ cases” defaults
- Card grids in the hero
- Floating badges (“#1 Clinic”, “Guaranteed smile”)
- Aggressive parallax that causes nausea on mobile

---

## Typography & layout craft (motion’s partner)

Premium motion fails if type/spacing is generic.

- Display: high-contrast serif (e.g. Fraunces / similar), generous tracking on eyebrows (−0.02em on display)
- Body: refined grotesque, 1.6 line-height, max ~34–38ch for long reading
- Section vertical rhythm: 120–160px desktop, 72–96px mobile
- Hero: full-bleed image plane edge-to-edge; brand is hero-level signal
- One job per section; avoid pill clusters and icon soup
- Color: deep pine + dubai teal + sand gold accent — restraint on gold (ornament, not fill)

---

## Framer implementation map

| Effect | Framer approach |
|--------|-----------------|
| Hero sequence | Appear effects + delay cascade; or code component for mask lines |
| Scroll reveals | While-in-view / scroll section variants |
| Nav compact | Scroll variant on nav component |
| Button states | Component variants + transitions |
| Page transitions | Page Effects (July 2026 agent support) |
| Parallax | Scroll speed transform on image layers |
| Accordion | Variants or native interaction |
| Magnetic button | Light code component (`framer-motion`) only if variants can’t deliver |
| Reduced motion | Override variants / media query in code components |

Prefer **native Appear / Variants / Page Effects** first. Add code components only for mask headlines and magnetic CTA if canvas tools can’t hit the bar.

---

## Acceptance test (quality gate)

Preview on MacBook + iPhone:

1. **0–3s:** Brand and hero read as private clinic, not SaaS landing  
2. **Scroll 1 screen:** Reveals feel sequenced, not random fades  
3. **Hover CTA + nav:** Immediately “expensive” without glare  
4. **Treatments section:** Image/type relationship feels editorial  
5. **Contact form:** Focus states refined; copy still DHA-safe  
6. **Reduced motion on:** Site remains elegant, not broken  

If any step feels like a free Webflow clone, tighten timing and remove an effect — never add more.
