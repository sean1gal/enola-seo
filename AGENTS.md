# AGENTS.md — ENOLA SEO Compatibility

This file describes how ENOLA SEO behaves as a Claude Code skill and how it can be used alongside other agents or automation systems.

---

## What ENOLA SEO Is

ENOLA SEO is a Claude Code skill — a prompt-driven system that activates when Claude Code loads `SKILL.md`. It is not a plugin, MCP server, or standalone binary. It runs entirely inside a Claude Code session with browser access enabled.

---

## Activation

ENOLA SEO activates on natural language triggers. No slash command required for the full session flow.

**Triggers:** "run my SEO audit", "start enola seo", "audit my site", "why am I not ranking", "fix my GBP", `/enola`

**Slash commands (one-shot, no intake):**
```
/enola audit [url]
/enola geo [url]
/enola fix [url]
/enola score [url]
/enola report
```

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Claude Code | Any version with browser access |
| Browser access | Default in Claude Code — do not disable |
| Python 3 + reportlab | Only for Audit 26 (PDF Export) — installed on demand |
| API keys | None required |
| External services | None required |

---

## File Output

All output writes to `/seo-audit/` in the working directory where Claude Code is launched.

```
/seo-audit/
  BUSINESS_CONTEXT.md     — persistent business data
  CLAUDE.md               — hot cache (5 lines)
  DIAGNOSIS.md            — initial gap analysis
  ALERT-LOG.md            — open issues across sessions
  01-gbp-categories.md    — audit outputs (01–25)
  ...
  26-pdf-export/
    [BusinessName]_SEO_Audit.pdf
  12-WEEK-PLAN.md
```

ENOLA SEO does not write outside this directory. It does not modify system files, install packages silently, or make network requests beyond browser navigation.

---

## Using ENOLA SEO Alongside Other Skills

ENOLA SEO is self-contained. It does not call other skills and does not expect to be called by them.

If you are building a multi-skill workflow:

- **Run ENOLA SEO first** — it produces `BUSINESS_CONTEXT.md` which other skills can read for business name, URL, services, and location data
- **Reference `/seo-audit/` outputs** — any skill that needs SEO findings can read the audit files directly
- **Do not chain into intake** — ENOLA SEO's intake is designed to be a single session flow. Triggering it mid-session from another skill will restart the intake. Use slash commands for targeted one-shot tasks instead.

---

## Context Window Behavior

ENOLA SEO loads three reference files during a full audit session:
- `references/audits.md` (~460 lines)
- `references/advanced.md` (~340 lines)
- `references/output-formats.md` (~215 lines)

These load on demand, not all at once. Each is called when the relevant audit section runs.

In long sessions (running 10+ audits), context window usage will be heavy. If you notice degraded output quality in later audits, start a fresh Claude Code session — `BUSINESS_CONTEXT.md` will reload automatically and no data is lost.

---

## Extending ENOLA SEO

To add a new audit:

1. Add execution prompt to `references/audits.md` (audits 01–20) or `references/advanced.md` (audits 21+)
2. Add output format to `references/output-formats.md`
3. Add the audit to the menu in `SKILL.md` (Phase 4)
4. Follow the format: browse real URLs → write actual copy → end with `Impact: HIGH/MED/LOW | Timeline: X weeks`

See [CONTRIBUTING.md](CONTRIBUTING.md) for full contribution guidelines.

---

## Known Limitations

- **No API integrations** — ENOLA SEO uses browser navigation only. It cannot pull data from Google Search Console, DataForSEO, or Ahrefs APIs. What it can see is what a logged-out browser can see.
- **GBP data is public only** — It reads your public GBP listing. It cannot access your GBP dashboard, post insights, or call tracking data.
- **PDF export requires reportlab** — Audit 26 will check for it and install if missing. If the environment blocks pip installs, PDF export will not run.
- **Browser access must be enabled** — If Claude Code is running with browser access disabled, all browse steps will fail. ENOLA SEO will tell you before proceeding.

---

*ENOLA SEO v2.0 — MIT Licensed*
*Built by [Enola Revenue](https://enolarevenue.com)*
