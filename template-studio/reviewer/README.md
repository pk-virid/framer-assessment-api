# Framer Template Reviewer

Specialist QA used on **every** weekly template before Marketplace submit.

## What it is

Same role as a managed “Framer Template Reviewer” agent:

1. Crawl published preview URL  
2. Audit 6 weighted categories  
3. Score + grade + Marketplace / Studio ship readiness  
4. Emit CRITICAL / WARNING / INFO fixes with page citations  

## Where it lives

| Surface | Path |
|---------|------|
| Cursor agent plugin (local) | `~/.cursor/plugins/local/framer-template-reviewer/` |
| Repo mirror | `template-studio/reviewer/cursor-plugin/` |
| Pre-ship checklist | `PRE-SHIP-CHECKLIST.md` |
| HTTP API | `POST /api/assess` in repo root |

## Studio ship gate (not vanity scoring)

The reviewer does **not** invent 100s. Builds must earn them.

| Gate | Rule |
|------|------|
| Marketplace Ready | score ≥ 75 and no critical Template Requirements failures |
| **Studio Ship Ready** | score ≥ 95 **and** Template Requirements = 100 **and** zero CRITICAL |

AED 15k templates should clear Studio Ship Ready before listing.

## API

```bash
curl -s -X POST "$ASSESS_URL/api/assess" \
  -H 'content-type: application/json' \
  -d '{"templateUrl":"https://your-template.framer.website","strictStudioGate":true}'
```

Requires `ANTHROPIC_API_KEY`. Optional `ANTHROPIC_MODEL` override.
