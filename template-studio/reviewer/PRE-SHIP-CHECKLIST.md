# Pre-ship checklist — target score 100

Run before Marketplace submit. Gate for the weekly studio line:

**Ship only if** Framer Template Reviewer returns:
- `overallScore >= 95`
- `categories.templateRequirements.score === 100`
- zero `CRITICAL` fixes
- preferably zero `WARNING` too for AED 15k templates

## 1) Template Requirements (must be perfect)

- [ ] No lorem / “placeholder” / “click to edit” / instructional “Add any…” copy  
- [ ] No dead `#` or `example.com` links in nav/footer/CTAs  
- [ ] Unique `<title>` per page (not default Framer project name)  
- [ ] Home, Terms, Privacy present and linked  
- [ ] Instructions / Getting Started with “content you must replace”  
- [ ] Custom favicon + webclip  
- [ ] Meta description + OG tags on key pages  
- [ ] Realistic demo content (differentiated pricing/features if present)  
- [ ] No real personal PII; use obvious `[placeholders]`  
- [ ] One copyright year + brand string sitewide  
- [ ] Style Guide page  

## 2) Structure

- [ ] Single Nav + Footer components (no divergent copyright footers)  
- [ ] CMS list bindings show correct fields per item  
- [ ] No duplicate footer links  
- [ ] Color + text styles used (not one-off randoms)  

## 3) Performance

- [ ] Source images ≤ ~2400px long edge, WebP/AVIF preferred  
- [ ] No fragile external video CDNs; host in Framer  
- [ ] Minimal third-party scripts  

## 4) SEO

- [ ] Titles ~50–60 chars, unique  
- [ ] Meta descriptions ~150–160 chars  
- [ ] One H1 per page; no skipped heading levels  
- [ ] `/sitemap.xml` + `/robots.txt`  
- [ ] Alt text on content images  

## 5) Accessibility

- [ ] Form `<label>`s (not placeholder-only)  
- [ ] No typos in marquee/UI copy  
- [ ] No vague duplicate “Learn more” → same URL  
- [ ] `html lang` set  
- [ ] Contrast AA on body text  

## 6) Responsiveness

- [ ] Desktop / tablet / phone breakpoints checked  
- [ ] Touch targets ≥ 44px on key controls  
- [ ] Body text ≥ 16px on mobile  
- [ ] No horizontal scroll bugs  

## How to run

### In Cursor
Invoke agent **Framer Template Reviewer** or skill `framer-template-review` with the published URL.

### Via API
```bash
curl -s -X POST "$ASSESS_URL/api/assess" \
  -H 'content-type: application/json' \
  -d '{"templateUrl":"https://YOUR.framer.website","strictStudioGate":true}'
```

Fix every CRITICAL and WARNING, republish, re-run until `studioShipReady: true`.
