---
name: dha-dentist-framer
description: >
  Build or edit Framer-native dental clinic templates for Dubai with DHA/MOHAP-safe
  marketing copy. Use when creating dentist templates, Caliora remakes, UAE clinic
  sites, or when the user mentions DHA compliance, MOHAP advertisement licence,
  or selling Framer templates to Dubai dentists. Requires @framer/agent setup first.
---

# DHA Dentist × Framer

## Preconditions

1. Run `npx @framer/agent@latest setup` if Framer skills are missing.
2. Load the official `framer` skill and connect a session before canvas edits.
3. Read project `caliora-dubai/COPY-DECK.md` and `DHA-COMPLIANCE.md` when present in the workspace.

## Build principles

- **AED 15,000 quality bar**: private-clinic luxury; quiet expensive motion; reject anything that feels like a free starter.
- **Framer-native only**: Stacks, Components, CMS, Forms, Styles. No Webflow HTML export shells.
- **Sellable template**: include Home, Treatments (+CMS), Conditions (+CMS), Blog (+CMS), Locations (Dubai), Contact, About, Cases, Privacy, Terms, Instructions, Style Guide.
- **Brand-forward hero**: first viewport = brand + one headline + one support line + CTA group + one dominant full-bleed visual. No stat strips or card grids in the hero.
- **Motion**: follow `caliora-dubai/PREMIUM-MOTION.md` — hero choreography, masked headlines, scroll reveals, image settle/parallax, nav compact, button variants, page transitions, reduced-motion fallbacks. No purple glow / bounce spam.
- **Dubai localisation**: `+971` phones, Dubai areas, MOHAP/DHA licence slots — not US cities from Caliora source.

## DHA copy guardrails (non-negotiable)

Refuse or rewrite any copy that:

- Guarantees outcomes, “pain-free forever”, miracles, or identical results
- Claims “best / #1 / leading in Dubai” or superiority vs other clinics
- Uses unverifiable case counts or shade-change guarantees as facts
- Promotes filming patients under general anaesthesia
- Omits editable MOHAP Adv. Licence + DHA Facility Licence footer slots
- Uses clinical cure testimonials (experience-only quotes allowed with consent note)

Prefer: consultation CTAs, assessment-dependent language, written plans before treatment, outcomes-vary disclaimers on cases/treatments.

## Execution order

1. Connect session → read generated `index.md` task map  
2. Styles + core components (`Button`, `Nav`, `Footer` with `LicenceStrip`)  
3. CMS collections + DHA-safe seed content  
4. Home via `applyChanges` or `framer.agent.startConversation` with Caliora reference + copy deck constraints  
5. Remaining pages + CMS detail routes  
6. Compliance pass + responsive/a11y pass  
7. Publish only if the user explicitly asks  

## Reference

Official Framer path: External Agents via `@framer/agent` — not a custom MCP server.
Plugins 4.1 branching/publishing APIs may be used for release workflows.
