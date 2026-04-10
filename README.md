<div align="center">

# ENOLA SEO

**26 local SEO audits. Real browser data. Everything saved to files.**

Built for local businesses tired of losing to worse competitors on Google.

[![Version](https://img.shields.io/badge/version-2.0.0-B85C38?style=flat-square)](https://github.com/sean1gal/enola-seo/releases)
[![License](https://img.shields.io/badge/license-MIT-6D28D9?style=flat-square)](LICENSE)
[![Audits](https://img.shields.io/badge/audits-26-047857?style=flat-square)](#the-26-audits)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-B45309?style=flat-square)](https://claude.ai/download)
[![Free Forever](https://img.shields.io/badge/free-forever-1C1410?style=flat-square)](https://enolarevenue.com)

[Quick Start](#quick-start) · [26 Audits](#the-26-audits) · [Slash Commands](#slash-commands) · [Who It's For](#who-this-is-for) · [Contributing](CONTRIBUTING.md)

**[→ Landing page + full guide](https://build.enolarevenu.com/enola-seo)**

</div>

---

## What This Is

ENOLA SEO is a free Claude Code skill that turns Claude into a full SEO auditor — for any business type.

Tell it your website. It interviews you to understand your business, browses your real listings and competitors, diagnoses every gap, and runs the audits that apply to your situation. Local service business, SaaS, B2B, e-commerce — the system routes itself.

Everything it produces — copy, templates, action plans — gets saved to organized files on your machine.

No API keys. No subscriptions. No generic advice. Just real competitive intelligence and paste-ready output.

---

## Quick Start

Three ways to install — pick the one that fits your setup.

### Option A — MCP Plugin (Claude Desktop, OpenClaw, Cursor)

Add to your `claude_desktop_config.json` (or equivalent MCP config):

```json
{
  "mcpServers": {
    "enola-seo": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/sean1gal/enola-seo", "enola-seo-mcp"]
    }
  }
}
```

Restart your client. ENOLA SEO appears as a tool set. Say "run the local quick start preset" and it goes.

**Tools exposed:** `list_skills` · `load_skill` · `list_presets` · `load_preset` · `run_diagnostic` · `set_context` · `get_context`

### Option B — Claude Code Skill (one-line install)

```bash
curl -fsSL https://raw.githubusercontent.com/sean1gal/enola-seo/main/install.sh | bash
```

### Option C — Manual install

```bash
# Copy the enola-seo/ folder into your Claude Code skills directory
cp -r enola-seo/ ~/.claude/skills/

# Open Claude Code in any project directory and say:
run my SEO audit
```

### Choose your mode

First thing Enola asks — answer once, remembered forever:

> "How do you want to run this?
> 1. Browser only — no setup, works right now
> 2. API enhanced — richer data from Google Search Console + PageSpeed"

| | Browser Mode | API Enhanced |
|--|:---:|:---:|
| Works immediately | ✅ | Setup required (~10 min) |
| No API keys needed | ✅ | ❌ |
| Real traffic + ranking data | ❌ | ✅ |
| Real Core Web Vitals (field data) | ❌ | ✅ |
| Best for | Individuals, small businesses | Agencies, power users |

API setup guide: [`references/api-mode.md`](references/api-mode.md)

### First session

Every question has numbered answers. Answer with 1, 2, 3 — or type your own:

> "Do you have a website for your business?"

- **Yes** → Browses it, extracts everything, asks only for what's missing
- **No website yet** → Numbered intake, then builds your first pages for you
- **No business idea yet** → Runs market research first, finds the gap, then starts

**Total intake time: under 5 minutes.** Everything after that is audits and output.

### Second session and beyond

```
run my SEO audit
```

Enola loads your saved context. No re-interviewing. Jump straight to the audits.

### Done today

The recommended audits run in 2–4 hours. Every output includes a **TODAY** section — specific actions you can take in the next few hours, before you close the laptop.

---

## Slash Commands

Fast one-shot tasks — no interview needed:

| Command | What It Does |
|---------|-------------|
| `/enola audit [url]` | Full technical scan — Core Web Vitals, schema, crawlability, security |
| `/enola geo [url]` | AI visibility check — ChatGPT, Perplexity, Google AI Overviews |
| `/enola fix [url]` | Hard blockers only — what's costing you calls right now |
| `/enola score [url]` | Content quality + EEAT score (0–50 per page) |
| `/enola report` | Export full audit as branded PDF |

---

## The 26 Audits

<details>
<summary><strong>Google Business Profile — Audits 01–08</strong></summary>

| # | Audit | What You Get |
|---|-------|-------------|
| 01 | Category Audit | Every category competitors have that you don't. Tiered by impact. Steps to add. |
| 02 | Attributes Audit | Hidden tags driving clicks and rankings. Full comparison table. |
| 03 | Review Teardown | Velocity gap, keyword phrases competitors are ranking with, review request script. |
| 04 | Review Response System | 12 templates — 5★, 4★, 3★, 1–2★. Keyword-rich. Human-sounding. |
| 05 | Posts Strategy | 8-week calendar. Full copy for weeks 1–4. Neighborhood-specific content. |
| 06 | Services Copy | Optimized 40–60 word descriptions for every service. Paste-ready into GBP. |
| 07 | GBP Description | 3 versions — keyword, conversion, trust. A/B recommendation included. |
| 08 | Photo Plan | 8-week shot list. Naming conventions. Geotagging instructions per service area. |

</details>

<details>
<summary><strong>Website — Audits 09–13</strong></summary>

| # | Audit | What You Get |
|---|-------|-------------|
| 09 | Keyword Gap Audit | Top 20 keywords competitors rank for that you don't. Filtered to buyer intent. |
| 10 | Money Page Audit | Pages one fix away from page 1. Every fix written out — no placeholders. |
| 11 | City Page Builder | Full pages for every service + city combination you're missing. Paste into CMS. |
| 12 | Search Console Sprint | 30-day plan to push page 2 rankings to page 1. All copy written. |
| 13 | Review Sentiment | Mine competitor reviews for emotional language. Rewrite your homepage copy from it. |

</details>

<details>
<summary><strong>Authority — Audits 14–16</strong></summary>

| # | Audit | What You Get |
|---|-------|-------------|
| 14 | Backlink Strategy | 90-day plan. 15 links. Full outreach emails written for every single one. |
| 15 | Citation Audit | Every wrong NAP across 14+ directories. Fix instructions per platform. |
| 16 | Search Intent Map | Full keyword universe mapped to buyer stage. Stage 4 90-day ranking plan. |

</details>

<details>
<summary><strong>Content — Audits 17–20</strong></summary>

| # | Audit | What You Get |
|---|-------|-------------|
| 17 | Content Gap Analysis | 20 full content briefs. Problem-awareness first. Everything competitors rank for that you don't. |
| 18 | Entity Optimization | LocalBusiness JSON-LD schema. Knowledge graph strategy. 90-day build checklist. |
| 19 | GBP Posting Patterns | Reverse-engineered competitor posting data. First 4 weeks written in full. |
| 20 | Monthly Report | One-page revenue-only report template. Readable in 5 minutes. |

</details>

<details>
<summary><strong>Advanced — Audits 21–26</strong></summary>

| # | Audit | What You Get |
|---|-------|-------------|
| 21 | Technical SEO Scan | Core Web Vitals, schema, robots, sitemap, security, mobile, meta. PASS/WARN/FAIL per check. |
| 22 | GEO Audit | AI citation readiness. FAQ copy written. Citation bait brief. Schema for AI parsing. |
| 23 | Content Quality Score | EEAT score (0–50) per page. Rewrite brief for lowest scorer. |
| 24 | Hard Blockers Check | What's broken right now. Critical/Important/Clean. No timelines — just fix it. |
| 25 | Content Refresh Plan | Decaying pages found and prioritized. Rewrite brief + new intro paragraph per page. |
| 26 | PDF Export | Branded audit report. Client-ready or personal use. Cover, exec summary, plan. |

</details>

---

## B2C Local vs B2B Multi-Location

Every audit adapts to your business model.

| | B2C Local | B2B Multi-Location |
|-|-----------|-------------------|
| **Focus** | Map pack, GBP, emergency keywords | Multi-city pages, industry keywords, domain authority |
| **Review strategy** | Velocity + consumer language | Case studies + business outcomes |
| **Content** | Single-city service pages | City × industry matrix |
| **Backlinks** | Local directories, press, sponsors | Industry associations, case study features |
| **Sales cycle** | Same-day call → booked | Research → comparison → contact |
| **City pages** | One city, deep | Many cities, broad |

---

## What Gets Saved

Everything saves to `/seo-audit/` in your working directory:

```
/seo-audit/
  BUSINESS_CONTEXT.md     Persistent business data — loads every session
  CLAUDE.md               Hot cache — 5 lines, instant load
  DIAGNOSIS.md            Initial gap analysis
  ALERT-LOG.md            Open issues tracked across sessions
  01-gbp-categories.md
  02-gbp-attributes.md
  ...
  25-content-refresh.md
  26-pdf-export/
    [BusinessName]_SEO_Audit.pdf
  12-WEEK-PLAN.md
```

---

## Who This Is For

**Local service businesses** — plumbers, HVAC, electricians, roofers, landscapers, cleaners, lawyers, dentists, chiropractors, contractors. Anyone who needs Google to send them customers.

**Agencies** — use audit 26 to export a branded PDF proposal for clients.

**Businesses with no website** — audit 11 (City Page Builder) becomes your first website build brief.

**Entrepreneurs still choosing a niche** — run the market research path first. ENOLA SEO checks competition density, review gaps, and market viability before you commit.

---

## How The Memory Works

| Layer | File | What It Stores | When It Loads |
|-------|------|----------------|---------------|
| Hot cache | `CLAUDE.md` | 5 most important facts | Every session, instantly |
| Full context | `BUSINESS_CONTEXT.md` | Complete business data | On demand |
| Alert log | `ALERT-LOG.md` | Open issues from past sessions | Every session, checked first |

No re-interviewing. No lost context. Pick up exactly where you left off.

---

## What's New in v2

- 6 new advanced audits (Technical SEO, GEO, Content Quality, Hard Blockers, Content Refresh, PDF Export)
- Slash commands for one-shot tasks
- Smart intake: browses your website first, asks only for what's missing
- Market research path for businesses still choosing a niche
- B2C local vs B2B multi-location branching throughout all 26 audits
- GEO optimization for AI search visibility (ChatGPT, Perplexity, AI Overviews)
- Alert log tracks open issues across sessions
- `install.sh` one-liner installer

Full changelog in [CHANGELOG.md](CHANGELOG.md).

---

## Contributing

Issues and pull requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

Ideas for new audits, business types, or slash commands are especially useful.

---

<div align="center">

**ENOLA SEO v2.0 — by [Enola Revenue](https://enolarevenue.com)**

Free, forever. MIT Licensed.

</div>
