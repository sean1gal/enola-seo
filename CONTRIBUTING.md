# Contributing to ENOLA SEO

Thanks for helping. This is a free tool — contributions keep it useful.

---

## What Helps Most

### New audit ideas
The most valuable contributions. If you found a gap that's costing local businesses rankings and there's no audit for it, open an issue.

Good audit ideas include:
- A specific problem you've seen repeatedly across multiple businesses
- Something competitors have that clients consistently lack
- A check that's tedious to do manually but easy to automate with browser access

Not useful:
- Vague ideas like "more keyword research"
- Audits that duplicate what's already in 01–26
- Platform-specific audits that only apply to a handful of businesses

### Business type requests
ENOLA SEO is written for general local service businesses. If you work in a specific industry (medical, legal, home services, restaurants) and you know the audit gaps for that category, open an issue describing the differences.

### Bug reports
Something didn't run? A file didn't save? A slash command didn't trigger? Open an issue with the template below.

---

## Bug Reports

Use this format:

```
**Audit or command:**
[e.g., Audit 03, /enola fix, Phase 1 intake]

**What happened:**
[What Claude produced that it shouldn't have, or didn't produce that it should have]

**What should have happened:**
[Expected behavior based on the README or SKILL.md]

**Claude Code version:**
[Run: claude --version]

**Operating system:**
[Mac / Linux / Windows]

**Any error messages:**
[Paste if applicable]
```

---

## Feature Requests

Use this format:

```
**What you want:**
[One sentence describing the feature]

**Who it helps:**
[What type of business or user, and how often this situation comes up]

**Why it's not already covered:**
[Which existing audit does the closest thing, and what's missing]
```

---

## Submitting a Pull Request

1. Fork the repo
2. Make your changes in a branch: `git checkout -b your-change-name`
3. Test it — run the skill in Claude Code against a real business before submitting
4. Submit the PR with a clear description of what changed and why

### What gets merged

- Audit additions with complete execution prompts (follow the format in `references/audits.md`)
- Bug fixes with a clear explanation of what was wrong
- Accuracy corrections — if a check is wrong or produces bad output in edge cases

### What doesn't get merged

- Cosmetic reformatting without functional change
- Audit additions without tested execution prompts
- Changes that remove the browse-first requirement (this is core to how the tool works)

---

## Style Rules

These apply to everything in this repo:

- Browse real URLs before producing output. Never guess.
- Write actual copy — never `[placeholder text]`
- Every audit ends with: `Impact: HIGH/MED/LOW | Timeline: X weeks`
- Caveman prompts → dense output. Short instructions, complete deliverables.
- Save every output to `/seo-audit/[##]-[slug].md`

If a PR breaks any of these, it won't merge.

---

## Questions

Open an issue. Label it `question`.

No Slack. No Discord. Just GitHub.

---

*ENOLA SEO is MIT licensed. Contributions are MIT licensed.*
*Built by [Enola Revenue](https://enolarevenue.com)*
