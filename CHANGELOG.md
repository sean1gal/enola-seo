# Changelog

All notable changes to ENOLA SEO are documented here.

---

## v2.0.0 — 2026-04-09

### Added
- 6 new advanced audits (21–26):
  - **21 Technical SEO Scan** — Core Web Vitals, schema, robots, sitemap, security, mobile, meta tags. PASS/WARN/FAIL per check.
  - **22 GEO Audit** — AI search visibility across Google AI Overviews, ChatGPT, and Perplexity. Quotability scoring, FAQ generation, citation bait brief.
  - **23 Content Quality Score** — EEAT scoring (Experience, Expertise, Authority, Trust, Depth) per page. 0-50 scale. Rewrite briefs for low scorers.
  - **24 Hard Blockers Check** — What's costing you calls right now. Phone, GBP status, website basics, trust killers. Critical/Important/Clean output only.
  - **25 Content Refresh Plan** — Decay audit for every page. Tier 1/2/3 priority. Rewrite briefs + fresh intros for top 3.
  - **26 PDF Export** — Full audit packaged as branded PDF via reportlab. Self-use or client-ready mode.
- Slash commands for one-shot tasks (no interview required):
  - `/enola audit [url]` — full technical scan
  - `/enola geo [url]` — AI visibility check
  - `/enola fix [url]` — hard blockers only
  - `/enola score [url]` — content quality + EEAT score
  - `/enola report` — export to PDF
- Business model detection: B2C local vs B2B multi-location. Changes competitive analysis depth, city/service targeting, and content strategy throughout all 26 audits.
- Two-layer memory system:
  - `CLAUDE.md` hot cache — 5 lines, loads every session instantly
  - `BUSINESS_CONTEXT.md` — full persistent context, loaded on demand
- Alert log (`ALERT-LOG.md`) — open issues tracked across sessions. Every session checks for unresolved items before starting.
- GEO optimization throughout — AI citation readiness built into diagnosis and relevant audits.
- `install.sh` — one-line installer for macOS and Linux.

### Changed
- SKILL.md restructured: phases clearly separated, reference files only load when needed
- Diagnosis format updated: BLEEDING NOW / LOSING MONEY SLOWLY / COMPOUNDING PROBLEMS
- Output formats standardized: every audit file uses the same header (Impact, Timeline, Model)
- B2C/B2B branching added to audits 09, 11, 14, 16, 17, 24

### Fixed
- Context file now writes immediately after intake (not deferred)
- Alert log checked at session start before any other action
- Slash commands bypass intake entirely when context already exists

---

## v1.0.0 — 2026-01-01

### Added
- Initial release
- 20 audits covering GBP, website, authority, and content
- Interview-first flow: 4 sections, one at a time
- Persistent context via `BUSINESS_CONTEXT.md`
- Diagnosis before audit menu
- 12-week execution plan on wrap-up
- All output saved to `/seo-audit/` as organized .md files
- MIT licensed, free forever

---

*ENOLA SEO by Enola Revenue — enolarevenue.com*
