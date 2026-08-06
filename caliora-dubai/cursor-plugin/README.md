# framer-dha-dentist

Local Cursor plugin that adds DHA/MOHAP-safe guardrails when building **Framer-native** dentist templates for Dubai.

## Install

Saved at `~/.cursor/plugins/local/framer-dha-dentist/` — available to Cursor automatically.

Also requires Framer External Agent skills:

```bash
npx @framer/agent@latest setup
```

## Components

- **Skill** `dha-dentist-framer` — build order + compliance rules
- **Rule** `dha-copy` — copy constraints for dentist/dental files

## Notes

Does not replace `@framer/agent`. It layers Dubai healthcare advertising constraints on top of Framer canvas/CMS workflows.
