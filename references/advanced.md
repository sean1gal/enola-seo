# ENOLA SEO — ADVANCED AUDITS 21–26

These six audits go deeper than local GBP and website basics.
Same rules: browse real URLs, write real copy, no placeholders.

---

## 21 — TECHNICAL SEO SCAN

Most local businesses have at least one technical problem costing them rankings.
This audit finds them all, separates the urgent from the optional, and writes the fixes.

```
Browse: my website — homepage + 3-5 key service pages
Check each category. Grade: PASS / WARN / FAIL

SPEED + CORE WEB VITALS
  ∙ Page load time on mobile (target: under 3s)
  ∙ Largest Contentful Paint: PASS <2.5s | WARN 2.5-4s | FAIL >4s
  ∙ Cumulative Layout Shift: PASS <0.1 | WARN 0.1-0.25 | FAIL >0.25
  ∙ Interaction to Next Paint: PASS <200ms | WARN 200-500ms | FAIL >500ms
  ∙ Image sizes — are they compressed? WebP format?
  ∙ Any render-blocking resources?

CRAWLABILITY
  ∙ robots.txt exists + valid syntax?
  ∙ sitemap.xml exists + submitted to Google?
  ∙ No pages accidentally set to noindex
  ∙ Canonical tags present + consistent
  ∙ Internal links working (no 404s on main nav)

MOBILE
  ∙ Viewport meta tag present?
  ∙ Touch targets big enough (44x44px minimum)
  ∙ Text readable without zooming
  ∙ No horizontal scroll

SCHEMA MARKUP
  ∙ LocalBusiness schema present?
  ∙ Required fields complete: name, address, phone, url, geo
  ∙ AggregateRating schema if reviews exist
  ∙ Any schema validation errors

SECURITY
  ∙ HTTPS active?
  ∙ HTTP → HTTPS redirect working?
  ∙ HSTS header present?
  ∙ No mixed content (HTTP resources on HTTPS pages)

META TAGS
  ∙ Title tags: present, 30-60 chars, unique per page
  ∙ Meta descriptions: present, 120-160 chars, unique per page
  ∙ H1: one per page, matches search intent
  ∙ OG tags for social sharing

OUTPUT FORMAT:
Scorecard table: Category | Status | Issue | Fix
Hard blockers section (fix before anything else)
Quick wins section (under 10 minutes each)
Full fix instructions for every FAIL and WARN
Estimated impact per fix: HIGH/MED/LOW
```

---

## 22 — GEO AUDIT

GEO = Generative Engine Optimization.
Google AI Overviews, ChatGPT, Perplexity, and Claude now answer local service questions directly.
If your business isn't in those answers, you're invisible to a growing slice of buyers.
This audit finds out where you stand and exactly what to do about it.

```
Browse: search "[primary service] in [city]" across:
  ∙ Google (check for AI Overviews)
  ∙ Note if any results from my website appear in AI-generated summaries

Check my website for GEO signals:

CITATIONS + QUOTABILITY
- Does my content have direct, quotable answers to common questions?
- Are there clear "who, what, where, when, how much" statements?
- Statistics or specific data points AI systems can cite?
- Named experts or credentials that build authority?

STRUCTURE FOR AI PARSING
- FAQ sections with direct question + answer format?
- Clear heading hierarchy (H1 > H2 > H3)?
- Schema markup that makes entity relationships clear?
- Concise definitions of services (AI loves these)?

ENTITY CLARITY
- Is my business clearly identified as a real local entity?
- Name, location, service area explicitly stated on multiple pages?
- Consistent brand mentions across citations (signals entity trust)?

FRESHNESS
- Content dated recently?
- Any pages with obvious outdated information?
- Last-modified signals in schema?

SCORE each category: STRONG / WEAK / MISSING

BUILD: GEO optimization plan
  ∙ Top 5 content changes to become AI-citable
  ∙ FAQ section to add (write the actual questions + answers for top 5)
  ∙ Schema additions for AI parsing
  ∙ One piece of "citation bait" content — write a brief + outline

OUTPUT: GEO score card + FAQ copy written + citation bait brief + schema additions
```

---

## 23 — CONTENT QUALITY SCORE

Content that doesn't demonstrate real expertise doesn't rank.
Google's EEAT (Experience, Expertise, Authoritativeness, Trustworthiness) is
the invisible filter everything passes through. This audit scores it.

```
Browse: my website — homepage + top 3 service pages
SCORE each page across 5 dimensions (0-10 each):

EXPERIENCE (0-10)
  ∙ First-hand knowledge signals present?
  ∙ Specific project examples, photos, case studies?
  ∙ "We've done X jobs in [city]" type proof?
  ∙ Before/after specifics?

EXPERTISE (0-10)
  ∙ Author or team credentials visible?
  ∙ Technical depth appropriate to service?
  ∙ Industry-specific language used correctly?
  ∙ Certifications, licenses, training mentioned?

AUTHORITY (0-10)
  ∙ Third-party mentions, press, awards?
  ∙ Review count + rating visible on page?
  ∙ Years in business prominent?
  ∙ Associations and affiliations?

TRUST (0-10)
  ∙ Physical address visible?
  ∙ Phone number prominent?
  ∙ Privacy policy, terms present?
  ∙ HTTPS, trust badges, payment logos?
  ∙ Response to reviews visible (shows engagement)?

CONTENT DEPTH (0-10)
  ∙ Word count appropriate (service pages 600+ words)?
  ∙ Answers real questions buyers have?
  ∙ No thin filler content?
  ∙ Updated recently (within 12 months)?

TOTAL SCORE: X/50 per page

THIN CONTENT FLAGS:
  ∙ Pages under 300 words (immediate flag)
  ∙ Pages with no images
  ∙ Pages copied or templated without customization
  ∙ Keyword-stuffed pages (reads unnatural)

OUTPUT:
Score table: Page | E | E | A | T | Depth | Total | Grade
Priority fixes ranked by score gap
Rewrite brief for lowest-scoring page (full brief, ready to execute)
What to add to each page to hit 40+/50
```

---

## 24 — HARD BLOCKERS CHECK

Nothing else matters until the bleeding stops.
This audit ignores optimization and finds only what is actively costing you
customers right now — today — before any other audit runs.

```
Browse: my website + GBP listing
CHECK EACH BLOCKER. FAIL = stop everything and fix this first.

PHONE + CONTACT
→ Phone number clickable on mobile?
→ Phone number same on GBP, website, all directories?
→ Contact form working? (test it)
→ Business hours accurate on GBP?

GBP STATUS
→ Listing verified?
→ No suspension warnings?
→ No "suggested edits" from strangers overriding my info?
→ Primary category correct?
→ Description present (not blank)?
→ At least 10 photos uploaded?

WEBSITE BASICS
→ Site loads on mobile? (check actual mobile render)
→ Any pages returning 404?
→ Homepage redirecting somewhere weird?
→ SSL certificate valid + not expiring soon?
→ Call-to-action visible above the fold on mobile?

TRUST KILLERS
→ Any placeholder text visible ("Lorem ipsum", "Your name here")?
→ Broken images on homepage?
→ Social links pointing to empty/inactive profiles?
→ Copyright date showing an old year?
→ Reviews showing but unanswered (over 3 months of silence)?

B2B SPECIFIC
→ Case studies or portfolio exist?
→ Service area clearly defined for commercial clients?
→ Quote/consultation request form working?

OUTPUT FORMAT:
CRITICAL (fix today): [list with exact steps]
IMPORTANT (fix this week): [list with exact steps]
CLEAN (no issues found): [list]
No impact estimates. No timelines. Just fix it.
This audit is always free to run at any time — say "check hard blockers".
```

---

## 25 — CONTENT REFRESH PLAN

Rankings decay. Content written 2-3 years ago loses ground.
This audit finds every page that used to perform and figures out why it stopped.
Then it writes the fix.

```
Browse: my website — all main service pages and any blog content visible

IDENTIFY DECAY SIGNALS per page:
  ∙ Content age (when was it last updated?)
  ∙ Outdated information (old prices, discontinued services, old staff names)
  ∙ Missing recent keywords (new service modifiers, new location names)
  ∙ Thin vs competitor content (their pages got longer and better)
  ∙ Schema not present or incomplete
  ∙ No internal links added since original publish
  ∙ Images old or missing alt text

PRIORITIZE pages to refresh:
Tier 1: Pages that used to rank, probably don't now
(high-value service pages, city pages)
Tier 2: Pages that rank but are losing position slowly
(monitor + optimize)
Tier 3: Blog posts that could funnel to service pages
(update + add CTA)

For TOP 3 PRIORITY PAGES write:
  ∙ Refresh brief: what to add, what to remove, what to update
  ∙ New sections to add (with headline + 3-bullet outline)
  ∙ New internal links to add (from where, to where, anchor text)
  ∙ Schema to update or add
  ∙ Estimated word count increase needed
  ∙ One rewritten intro paragraph (to signal freshness to Google)

OUTPUT:
Decay audit table: Page | Age | Issues | Priority | Action
Full refresh brief for top 3 pages
Rewritten intro paragraph for each
```

---

## 26 — PDF EXPORT

The full audit as a branded, client-ready PDF.
Use for: keeping your own records, sharing with a partner, handing to a VA,
or presenting to a client if you're an agency.

```
REQUIREMENTS:
  ∙ Python 3 + reportlab installed
  ∙ All relevant audit files present in /seo-audit/

PRE-CHECK — run before anything else:
  pip show reportlab
  If not found: pip install reportlab
  Confirm install before proceeding.

BEFORE GENERATING — ask:
"Who is this for?"
→ Yourself: minimal cover, functional formatting
→ Client/stakeholder: add cover page, summary executive section, agency branding

BUILD the PDF from audit files present in /seo-audit/:

COVER PAGE:
Business name + primary service + city
"SEO Audit Report"
Date generated
Powered by Enola Revenue (small footer)
[If agency mode: agency name prominent, Enola Revenue in small footer]

SECTION 1 — EXECUTIVE SUMMARY (always included):
Business snapshot (from BUSINESS_CONTEXT.md)
Diagnosis summary (from DIAGNOSIS.md)
Top 3 quick wins
Overall health score (calculated from audit results present)

SECTION 2 — AUDIT RESULTS (only audits that were run):
Each audit as its own page/section
Tables and copy from the .md files
Formatted cleanly — no raw markdown syntax visible

SECTION 3 — 12-WEEK PLAN (if 12-WEEK-PLAN.md exists):
Full plan formatted as timeline

CLOSING PAGE:
"Next step: execute the plan above."
Contact info for Enola Revenue (enolarevenue.com)
[If agency mode: agency contact, Enola Revenue as "powered by" footnote]

GENERATE: /seo-audit/26-pdf-export/[BusinessName]_SEO_Audit.pdf
OUTPUT: confirm file path + file size
```

---

## NOTES ON ADVANCED AUDITS

**Audit 21 (Technical):** Run this early — hard to justify optimizing copy on a page
that loads in 7 seconds. Technical issues compound everything else.

**Audit 22 (GEO):** 2026 forward. AI answers are eating local search results.
Businesses that optimize for AI citations now will be ahead by 2027.

**Audit 23 (Quality Score):** Best run after audits 6, 7, 11 — gives a before/after
picture once copy has been improved.

**Audit 24 (Hard Blockers):** Always run first if user says anything urgent —
"why am I not getting calls", "my listing disappeared", "the site is broken".

**Audit 25 (Content Refresh):** Highest ROI for businesses over 2 years old
that had good rankings and lost them. Check this before creating new content.

**Audit 26 (PDF):** Run last. Packages everything.

---

*© Sean Gal | enolarevenu.com — MIT Licensed*
