# Build playbook — execute after Framer auth

## 0) Connect

```bash
# Prefer API key in cloud VMs (localhost OAuth callback is unreliable remotely)
npx @framer/agent@latest project auth "$FRAMER_PROJECT_ID" "$FRAMER_API_KEY"
# or: npx @framer/agent@latest project auth "https://framer.com/projects/<id>"

SESSION=$(npx @framer/agent@latest session new "$FRAMER_PROJECT_ID" | tail -n1)
echo "SESSION=$SESSION"
```

Read generated skill files:

- `~/.agents/skills/framer/projects/<safeId>/index.md` (task map)
- `project-inventory.md`

## 1) Design system first

Via `framer.agent.applyChanges` / styles:

1. Color styles: bg, ink, muted, brand, brand-2, surface, line  
2. Text styles: Display / H1–H3 / Body / Small / Button  
3. Create base components: Button, SectionHeading, LicenceStrip, DisclaimerBar  

## 2) CMS seed (DHA-safe)

Create collections from `FRAMER-ARCHITECTURE.md` and seed items from `COPY-DECK.md`.  
Do **not** seed fabricated clinical KPIs.

## 3) Pages — preferred build path

For large design recreation, use Framer’s design subagent (see skill `start-conversation.md`):

```js
state.agent ??= {};
const first = await framer.agent.startConversation(
  `Recreate a premium Framer-native dental clinic template inspired by https://caliora-dentist-template.webflow.io/ for Dubai dentists.
STRICT: Follow DHA-compliant copy from the attached brief. No guaranteed outcomes, no best-in-Dubai claims, no fake case counts.
Include MOHAP/DHA licence slots in footer. Locations in Dubai (Jumeirah + Business Bay placeholders).
Build Home first as one hero composition (brand-forward), then shared Nav/Footer components.`,
  {
    pagePath: "/",
    imageUrls: [
      /* optional screenshots of Caliora sections */
    ],
  },
);
state.agent.conversationId = first.conversationId;
```

Continue conversation to add About, Treatments index + detail wiring, Contact, Blog, legal pages.

Timeouts: 10 minutes per conversation turn.

## 4) Wire CMS lists

- Treatments / Conditions / Blog / Locations / Cases collection lists  
- Detail pages with slug routes  
- Related treatment links on condition pages  

## 5) Compliance pass

- Insert `LicenceStrip` + footer disclaimer sitewide  
- Outcomes disclaimer on Treatments, Cases, Gallery  
- Form microcopy from copy deck  
- Instructions page with buyer DHA checklist  
- Remove any absolute “pain-free” / “guaranteed” / superiority language  

## 6) Responsive + a11y pass

- Phone / tablet breakpoints  
- Alt text, heading order, tap targets  
- Page effects only if they don’t harm readability  

## 7) Marketplace QA

Run mental checklist in `FRAMER-ARCHITECTURE.md`. Optionally hit assessment API:

```bash
curl -s -X POST https://<assessment-host>/api/assess \
  -H 'content-type: application/json' \
  -d '{"templateUrl":"https://<published-framer-site>"}'
```

## 8) Publish (only if user asks)

```js
await framer.agent.publish();
```

Rename auto-branch to something like `caliora-dubai-dha-template` when `[FRAMER_BRANCH_CHANGE]` appears.

## Skills note

- Official skills from `@framer/agent` cover canvas/CMS/code components — **do not reinvent MCP**.  
- Local plugin `framer-dha-dentist` adds DHA copy guardrails for this product line.  
- July 2026 agent updates: Page Effects, A11Y attrs, richer overlays, CMS video — use carefully (no GA promo video).  
- Plugins 4.1: branching + publishing APIs available for release workflows.
