---
name: framer-template-review
description: >
  Audit a published Framer template URL for marketplace readiness using the
  six-category weighted rubric. Use when the user pastes a framer.website
  preview, asks if a template is submission-ready, or runs weekly QA.
---

# Framer template review

## Steps

1. Confirm URL (prefer published `*.framer.website` / `*.framer.app` / custom domain).
2. Fetch `/`, `/sitemap.xml`, `/robots.txt`.
3. Build page list from sitemap + internal links (cap at ~40 content pages for deep read; note total sitemap size).
4. Fetch each key page HTML; extract titles, headings, visible text, images, links, forms.
5. Score with the agent rubric in `agents/framer-template-reviewer.md`.
6. Emit the full report. For studio ship gate, state clearly whether **≥95 + Template Requirements 100 + zero CRITICAL** is met.

## Optional API

If `ANTHROPIC_API_KEY` is available in this repo:

```bash
curl -s -X POST "${ASSESS_URL:-http://localhost:3000}/api/assess" \
  -H 'content-type: application/json' \
  -d '{"templateUrl":"https://example.framer.website"}'
```

Prefer live crawl + this skill when running inside Cursor; use the API for automation hooks.
