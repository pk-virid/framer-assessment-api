# Caliora Dubai — Framer Dentist Template (DHA-ready)

Framer-native remake of [Caliora](https://caliora-dentist-template.webflow.io/) positioned for **Dubai dental clinics**, with copy rewritten for **DHA / MOHAP medical advertising standards**.

## Status

| Step | State |
|------|--------|
| `@framer/agent` skills installed | Done |
| Framer project connected | **Blocked** — needs project URL + browser auth or API key |
| DHA copy deck | Ready in this folder |
| Framer IA / CMS plan | Ready in this folder |
| Canvas build + publish | Waiting on connection |

## Why Framer External Agent (not a custom MCP)

Per [Framer External Agents](https://www.framer.com/agents/external/) and Plugins 4.1:

- Use `npx @framer/agent@latest setup` (already run) — installs official `framer` + `framer-code-components` skills
- No separate Framer MCP server is required
- Canvas edits go through `framer.agent.applyChanges` / `startConversation` on a branch
- Publishing / branching APIs are available for marketplace shipping workflows

## Connect (required from you)

1. Open team workspace: `https://framer.com/projects/?teamId=54a51444-6177-462a-8aa2-02357847044c`
2. Create a blank **Site** project (e.g. `Caliora Dubai Dentist`)
3. Either:
   - Paste the project URL in chat and approve the browser auth popup, **or**
   - Site Settings → General → API Keys → create key, then set secrets `FRAMER_API_KEY` + optional `FRAMER_PROJECT_ID`
4. Agent will run:

```bash
npx @framer/agent@latest project auth "<projectUrlOrId>" "<apiKey>"
npx @framer/agent@latest session new "<projectUrlOrId>"
```

## Sellable template goals

- 100% Framer-native (Stacks, Components, CMS, Forms, Styles — not a Webflow export)
- Marketplace-ready pages: Home, About, Treatments, Conditions, Blog, Contact, Locations, Privacy, Terms, Style Guide
- Placeholder clinic brand (`Caliora Dental Clinic — Dubai`) buyers can rename
- DHA-safe marketing language (see `DHA-COMPLIANCE.md`)
- Dubai-localised locations, contact patterns, insurance/payment notes, Arabic-ready structure notes

## Files

- `DHA-COMPLIANCE.md` — advertising rules baked into every section
- `COPY-DECK.md` — full section copy (EN) for Dubai dentists
- `FRAMER-ARCHITECTURE.md` — pages, CMS, components, tokens
- `BUILD-PLAYBOOK.md` — exact Framer agent execution order after auth
