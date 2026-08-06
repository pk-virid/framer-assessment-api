# Weekly Framer template pipeline

Cadence: **one sellable Framer template per week.**  
Stack: `@framer/agent` + premium motion bar + niche compliance copy.

## Definition of done (every template)

1. Framer-native (components, CMS, styles, forms) — not a static export  
2. Marketplace pages: Home, key listing + detail CMS routes, Contact, About, Privacy, Terms, Instructions, Style Guide  
3. Premium motion pack applied (hero choreography, scroll reveals, nav/button polish, page transitions, reduced-motion)  
4. Niche-safe copy (for UAE health: DHA/MOHAP rules)  
5. Desktop + phone pass, working links, no lorem  
6. Published preview URL + buyer instructions  
7. **Framer Template Reviewer gate (mandatory):** `studioShipReady: true`  
   - overall ≥ 95, Template Requirements = 100, zero CRITICAL  
   - Agent: `framer-template-reviewer` · checklist: `reviewer/PRE-SHIP-CHECKLIST.md` · API: `POST /api/assess`  
   - Loop: fix → republish → re-audit until pass (do not submit cold)

## Weekly rhythm

| Phase | What happens |
|-------|----------------|
| **Kickoff** | Pick niche + reference URL + price tier + compliance constraints |
| **Brief** | Copy deck + IA + motion notes (clone prior pack, rewrite niche) |
| **Connect** | Blank Framer project in team workspace + API key/session |
| **Build** | Design system → CMS seed → Home (motion bar) → remaining pages |
| **Polish** | Responsive, a11y, compliance pass |
| **Review** | Run Framer Template Reviewer on published URL; clear CRITICAL/WARNING |
| **Ship** | Preview + remix links only after `studioShipReady`; archive brief for next week |

## Reuse from Caliora Dubai (week 1)

| Asset | Reuse how |
|-------|-----------|
| `PREMIUM-MOTION.md` | Default motion bible for all premium-priced templates |
| `framer-dha-dentist` plugin | Fork rules/skills per regulated niche |
| `FRAMER-ARCHITECTURE.md` | Clone page/CMS skeleton; swap collection names |
| `BUILD-PLAYBOOK.md` | Same agent execution order |
| `scripts/connect-framer.sh` | Same auth path every week |

## Backlog format (keep a running list)

```text
W1  Caliora Dubai Dentist     ref: caliora-dentist-template.webflow.io    AED 15,000   DHA
W2  [Niche]                   ref: [url]                                  AED [? ]     [compliance]
W3  ...
```

## Rules that protect the cadence

- One primary reference site per week — don’t frankenstein three aesthetics  
- Lock price tier before build (motion/craft bar scales with price)  
- Auth first: no canvas work without project URL / `FRAMER_API_KEY`  
- Don’t start week N+1 canvas until week N hits definition of done  
- Regulated niches (health, finance, legal): compliance deck before visual polish  

## Team workspace

Default Framer team: `https://framer.com/projects/?teamId=54a51444-6177-462a-8aa2-02357847044c`
