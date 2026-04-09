# ENOLA SEO — Audit 21: Technical SEO Scan
**Business:** Austin Drain Pros | austindrain.com
**Date:** 2026-04-09
**Model:** B2C Local
**Pages scanned:** Homepage, /drain-cleaning, /water-heater, /contact

---

## SCORECARD

| Category | Check | Status | Issue |
|----------|-------|:------:|-------|
| **Speed** | Mobile load time | ⚠️ WARN | 4.1s — above 3s target |
| **Speed** | Largest Contentful Paint | ⚠️ WARN | 3.8s — above 2.5s threshold |
| **Speed** | Cumulative Layout Shift | ✅ PASS | 0.04 — well within limit |
| **Speed** | Interaction to Next Paint | ✅ PASS | 180ms |
| **Speed** | Images compressed | ❌ FAIL | 7 images uncompressed, no WebP |
| **Speed** | Render-blocking resources | ⚠️ WARN | 2 JS files blocking render |
| **Crawl** | robots.txt | ✅ PASS | Present, valid |
| **Crawl** | sitemap.xml | ❌ FAIL | Missing — not submitted to Google |
| **Crawl** | Noindex errors | ✅ PASS | No pages accidentally blocked |
| **Crawl** | Canonical tags | ⚠️ WARN | Present on homepage, missing on service pages |
| **Crawl** | Internal links | ✅ PASS | No broken links found |
| **Mobile** | Viewport meta tag | ✅ PASS | Present |
| **Mobile** | Touch targets | ❌ FAIL | Phone number button: 28px — below 44px minimum |
| **Mobile** | Text readability | ✅ PASS | No zoom required |
| **Mobile** | Horizontal scroll | ✅ PASS | None |
| **Schema** | LocalBusiness schema | ⚠️ WARN | Present but incomplete — missing `geo` and `openingHours` |
| **Schema** | AggregateRating | ❌ FAIL | Missing — you have 47 reviews but they don't show in search |
| **Schema** | Validation errors | ⚠️ WARN | 1 error: `telephone` format incorrect (missing +1 country code) |
| **Security** | HTTPS | ✅ PASS | Active |
| **Security** | HTTP → HTTPS redirect | ✅ PASS | Working |
| **Security** | HSTS header | ⚠️ WARN | Not present |
| **Security** | Mixed content | ✅ PASS | None found |
| **Meta** | Title tags | ⚠️ WARN | /water-heater title is 71 chars — over 60 char limit |
| **Meta** | Meta descriptions | ❌ FAIL | /drain-cleaning and /contact have no meta description |
| **Meta** | H1 tags | ✅ PASS | One per page, matches intent |
| **Meta** | OG tags | ❌ FAIL | Missing on all pages |

**Score: 14 PASS / 7 WARN / 5 FAIL**

---

## HARD BLOCKERS — Fix Before Anything Else

### ❌ No sitemap.xml submitted to Google
Google is not being told which pages to index or how often they update. Every page you add or change takes longer to index.

**Fix:**
1. Generate sitemap at [xml-sitemaps.com](https://www.xml-sitemaps.com) — enter your domain, download the file
2. Upload `sitemap.xml` to your root directory (so it lives at `austindrain.com/sitemap.xml`)
3. Go to [Google Search Console](https://search.google.com/search-console) → Sitemaps → Submit `sitemap.xml`

**Time:** 15 minutes. Impact: HIGH.

---

### ❌ AggregateRating schema missing
You have 47 reviews at 4.6 stars. None of this shows in Google search results because there's no schema telling Google it exists. Competitors with this schema get star ratings in their search listings — you get a plain blue link.

**Fix — add this JSON-LD to every page's `<head>`:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Austin Drain Pros",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "reviewCount": "47",
    "bestRating": "5",
    "worstRating": "1"
  }
}
</script>
```

Update `ratingValue` and `reviewCount` monthly as reviews come in.

**Time:** 20 minutes. Impact: HIGH — star ratings in search results directly increase click-through rate.

---

### ❌ Images not compressed, no WebP
7 images on the homepage are serving at original resolution. Combined overhead: ~2.4MB. This is the primary cause of your 4.1s mobile load time.

**Fix:**
1. Run all images through [Squoosh.app](https://squoosh.app) — convert to WebP, quality 80
2. Re-upload compressed versions to your CMS/host
3. Update image tags if filenames change

Or if on WordPress: install **Smush** or **ShortPixel** — they handle this automatically.

**Time:** 30 minutes. Impact: HIGH — fixes LCP, drops load time to target range.

---

### ❌ Meta descriptions missing on 2 pages
`/drain-cleaning` and `/contact` have no meta descriptions. Google writes one for you — it picks random text, usually the wrong text.

**Fix:**

`/drain-cleaning`:
> Austin's same-day drain cleaning experts. Clogged drains, sewer backups, root intrusion — cleared fast. Licensed plumbers, upfront pricing. Call or book online.

`/contact`:
> Reach Austin Drain Pros — same-day plumbing and drain service in Austin, TX. Call [phone], book online, or use our contact form. We answer fast.

**Time:** 10 minutes. Impact: MED — affects click-through rate from search results.

---

### ❌ OG tags missing
When someone shares your pages on Facebook, iMessage, or Slack, no image or title appears — just a bare URL. This matters for referral traffic.

**Fix — add to `<head>` of every page:**

```html
<meta property="og:title" content="Austin Drain Pros — Same-Day Drain & Plumbing Service" />
<meta property="og:description" content="Fast, licensed plumbers in Austin TX. Drain cleaning, water heaters, sewer service. Call now." />
<meta property="og:image" content="https://austindrain.com/images/og-cover.jpg" />
<meta property="og:url" content="https://austindrain.com" />
<meta property="og:type" content="website" />
```

Create one 1200×630px image of your truck or team for `og-cover.jpg`.

**Time:** 20 minutes. Impact: LOW — does not affect rankings directly, affects referral click-through.

---

## QUICK WINS — Under 10 Minutes Each

**Touch target fix:** The phone number button is 28px tall. Change CSS `padding` to at least `12px 16px` to bring it to 44px minimum. One CSS line.

**Title tag fix:** `/water-heater` title is "Water Heater Installation, Replacement and Repair Services in Austin Texas" (71 chars). Trim to: "Water Heater Installation & Repair — Austin TX" (47 chars).

**Schema telephone fix:** Change `"telephone": "512-555-0182"` to `"telephone": "+15125550182"` in your LocalBusiness schema.

**Canonical tags:** Copy the homepage `<link rel="canonical">` tag pattern to all service pages. Each page points to its own URL.

---

## FULL FIX PRIORITY ORDER

| Priority | Fix | Time | Impact |
|----------|-----|------|--------|
| 1 | Compress images → WebP | 30 min | HIGH |
| 2 | Submit sitemap.xml | 15 min | HIGH |
| 3 | Add AggregateRating schema | 20 min | HIGH |
| 4 | Write missing meta descriptions | 10 min | MED |
| 5 | Fix touch target (phone button) | 5 min | MED |
| 6 | Add OG tags | 20 min | LOW |
| 7 | Fix title tag length | 5 min | LOW |
| 8 | Add canonical tags to service pages | 10 min | LOW |
| 9 | Add HSTS header (server config) | 15 min | LOW |

Total time to fix everything: ~2 hours.

---

**Impact: HIGH | Timeline: Fixes in 1 week, indexing in 2–3 weeks**

*Generated by ENOLA SEO v2.0 | enolarevenue.com*
