# framer-template-reviewer

Cursor plugin: **Framer Template Reviewer** agent + skill + command.

Audits published Framer templates with the six-category weighted rubric (Requirements 25%, Structure / Performance / SEO / A11y / Responsiveness 15% each) so weekly templates can ship marketplace-ready on first submission.

## Install

Lives at `~/.cursor/plugins/local/framer-template-reviewer/` (auto-available locally).

## Usage

1. Publish the Framer project preview.
2. Run command **review-framer-template** or ask: “Review this Framer template: https://….framer.website”
3. Fix CRITICAL → WARNING → INFO; re-audit until studio ship gate passes.

## Components

| Path | Role |
|------|------|
| `agents/framer-template-reviewer.md` | Full reviewer agent |
| `skills/framer-template-review/` | Crawl + score workflow |
| `commands/review-framer-template.md` | Slash-style command |

Companion API in this repo: `POST /api/assess`.
