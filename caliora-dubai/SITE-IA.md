# Site information architecture — Caliora Dubai

**Primary reference:** [Sensate Dental OS](https://sensatedentalos.framer.website/)  
**Visual / motion reference:** Caliora + `PREMIUM-MOTION.md`  
**Compliance:** `DHA-COMPLIANCE.md`

## Recommended structure (better than flat-only)

Your eight primary pages are correct for patient-facing nav. For a **AED 15,000** Dubai clinic OS template, add a thin **authority layer** under the hood (like Sensate) so Treatments / Conditions / Symptoms / Articles interlink — that is what buyers pay for.

### Primary nav (always visible)

| Label | Path | Type |
|-------|------|------|
| Home | `/` | Page |
| About | `/about` | Page |
| Treatments | `/treatments` | CMS list |
| Conditions | `/conditions` | CMS list |
| Symptoms | `/symptoms` | CMS list |
| Membership | `/membership` | Page + CMS plans |
| Offers | `/offers` | CMS list |
| Contact Us | `/contact` | Page + form |

### Secondary / footer (required for product + marketplace)

| Label | Path | Why |
|-------|------|-----|
| Articles | `/articles` | Patient education hub (Sensate pattern) |
| Clinicians | `/clinicians` | Named DHA-licensed profiles |
| Learn / Topics | `/learn` | Topic hubs grouping conditions + treatments + articles |
| Privacy | `/privacy` | Marketplace + legal |
| Terms | `/terms` | Marketplace + legal |
| Instructions | `/instructions` | Buyer setup + DHA checklist |
| Style Guide | `/style-guide` | Template craft |
| Search | `/search` | Optional but high-value (Sensate has it) |

### Optional upsell pages (include as template extras, not primary nav)

| Path | Purpose |
|------|---------|
| `/funnel/new-patient` | New patient journey |
| `/funnel/smile-makeover` | Cosmetic pathway |
| `/membership/compare` | Plan comparison |
| `/symptoms/check` | Simple symptom → condition router (educational, not diagnosis) |

**Why this is better than only 8 pages:**  
Sensate’s strength is the **content graph** (Symptom → Condition → Treatment → Article → Clinician → Membership). Primary nav stays simple; SEO and retention live in CMS detail routes.

---

## CMS collections (DHA-ready fields)

### Treatments (`/treatments/:slug`)
`title`, `slug`, `category`, `summary`, `heroImage`, `body`, `process`, `limitations`, `relatedConditions` (multi-ref), `relatedSymptoms` (multi-ref), `relatedArticles` (multi-ref), `clinician` (ref), `order`  
Seed from Sensate dental set (whitening, veneers, implants, RCT, cleaning, etc.). Soften absolute success-rate claims.

### Conditions (`/conditions/:slug`)
`title`, `slug`, `summary`, `heroImage`, `body`, `causes`, `whenToSeekCare`, `relatedTreatments`, `relatedSymptoms`, `relatedArticles`, `order`

### Symptoms (`/symptoms/:slug`)
`title`, `slug`, `summary`, `body`, `urgencyNote` (educational), `relatedConditions`, `relatedTreatments`, `relatedArticles`  
Index page = A–Z. Optional `/symptoms/check` = guided picker → condition links (**not** a diagnostic tool — disclaimer required).

### Articles (`/articles/:slug`)
`title`, `slug`, `excerpt`, `cover`, `body`, `category` / `topicHub`, `author` (ref), `medicalReviewer` (ref), `reviewedAt`, `readMinutes`, `relatedTreatments`, `relatedConditions`  
Every article ends with: educational only; not a substitute for in-clinic assessment.

### Offers (`/offers/:slug`)
`title`, `slug`, `summary`, `terms`, `validUntil`, `ctaLabel`, `linkedTreatment` / `linkedMembership`, `mohapNote`  
**DHA:** no guaranteed outcomes; no bait discounts that cannot be met; show licence slot; Medical Director approval note in Instructions.

### Membership plans (`/membership` + optional `/membership/:slug`)
`name`, `slug`, `priceLabel` (e.g. “from AED X / year — variables apply”), `includes` (rich/list), `exclusions`, `bestFor`, `order`  
Plans patterned on Sensate: Single Care · Family Smile · Corporate Wellness — rewritten without superiority claims.

### Clinicians / Authors
`name`, `slug`, `dhaTitle`, `dhaLicenceNo` (placeholder format), `bio`, `languages`, `photo`, `treatments` (multi-ref), `role` (Author / Reviewer / Both)

### Topic hubs (`/learn/:slug`) — recommended
`title`, `slug`, `summary`, `relatedTreatments`, `relatedConditions`, `relatedArticles`  
Hubs: Oral Health · Cosmetic · Restorative · Orthodontics · Implants · Periodontal · Endodontics · Children’s · Emergency · Aesthetic (if in scope)

---

## Detail page template (all clinical CMS types)

Shared layout for Treatment / Condition / Symptom / Article:

1. Breadcrumb  
2. Title + short summary  
3. **Medical review strip** — Author · Reviewer · Reviewed date · “Educational content”  
4. Hero image (facility / stock — not GA procedure promo)  
5. Body (DHA-safe)  
6. Related graph (conditions ↔ treatments ↔ symptoms ↔ articles)  
7. Limitations / “outcomes vary” (treatments & cases)  
8. CTA → Contact / Membership (consultation framing)  
9. Licence strip (global footer)

---

## Home composition (maps to Sensate sections, Caliora craft)

1. Full-bleed hero — brand + one headline + support + CTA (premium motion)  
2. Patient paths (New patient / Smile / Prevention) — optional funnels  
3. Treatments grid (CMS)  
4. Approach + honest stats (buyer-editable)  
5. Membership teaser  
6. Why us (DHA-reviewed content, digital planning, team, transparency)  
7. Topic hubs  
8. Featured articles  
9. Clinicians  
10. Experience testimonials (consent + non-clinical)  
11. Locations / Contact CTA  
12. Footer + MOHAP/DHA slots  

---

## What we take from Sensate vs what we improve

| Take | Improve for our sellable template |
|------|-----------------------------------|
| Nav: Treatments, Conditions, Symptoms, Membership, Offers | Keep your 8-item primary nav; park Learn/Articles/Clinicians in secondary |
| CMS content graph | Same graph; cleaner naming; no duplicate Articles≈Guides unless needed |
| Named clinicians + reviewers | Keep — strong DHA trust signal |
| Membership tiers | Keep; price as “from / variables apply” |
| Funnel pages | Include 2–3 as extras |
| Style/system pages in sitemap | Don’t publish builder/system URLs in buyer preview |
| Aggressive KPIs / “pain-free” / success % | Rewrite to assessment-dependent, verifiable language |

---

## Seed content volume (week-1 shippable)

| Collection | Seed count |
|------------|------------|
| Treatments | 12–16 |
| Conditions | 12–16 |
| Symptoms | 12–16 |
| Articles | 8–12 |
| Offers | 3–4 |
| Membership plans | 3 |
| Clinicians | 3–4 |
| Topic hubs | 6–8 |

Enough to feel like an OS; not so many that Marketplace QA collapses under unfinished pages.
