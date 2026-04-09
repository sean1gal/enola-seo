# ENOLA SEO — API Enhanced Mode

API mode gives specific audits access to real data that browser scraping cannot see:
actual search impressions, clicks, page position history, and Core Web Vitals field data.

Browser mode is the default. API mode is for agencies and power users who want harder numbers.

---

## What Each API Unlocks

| API | Free? | What It Adds | Audits Affected |
|-----|-------|-------------|-----------------|
| Google Search Console | Free | Real impressions, clicks, CTR, position per page | 09, 10, 12, 16 |
| PageSpeed Insights API | Free | Real CrUX field data (LCP, CLS, INP from actual users) | 21 |
| Google Analytics 4 | Free | Actual traffic by page, bounce rate, session data | 10, 12, 20, 25 |

All three are free. They require a Google account and a few minutes of setup.

---

## Setup — Google Search Console API

**What you need:** A verified Search Console property for the site.

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a project (or use an existing one)
3. Enable the **Search Console API**
4. Create credentials → **Service Account** → download the JSON key file
5. In Search Console: Settings → Users and permissions → Add the service account email with "Full" access
6. Set the environment variable:
   ```
   export GSC_KEY_FILE="/path/to/your-service-account.json"
   export GSC_SITE_URL="https://yourdomain.com/"
   ```

When ENOLA SEO detects `GSC_KEY_FILE` at startup, it offers API mode automatically.

**What changes in audit mode:**
- Audit 09 (Keyword Gap): shows real queries you rank for and their positions
- Audit 10 (Money Page): surfaces pages with high impressions but low CTR — real data, not inferred
- Audit 12 (Search Console Sprint): pulls actual page 2 rankings to target
- Audit 16 (Search Intent Map): maps real queries to buyer stage using actual search data

---

## Setup — PageSpeed Insights API

**What you need:** A Google Cloud API key (same project as above).

1. In Google Cloud Console → APIs & Services → Enable **PageSpeed Insights API**
2. Create credentials → **API Key**
3. Set the environment variable:
   ```
   export PAGESPEED_API_KEY="your-api-key-here"
   ```

**What changes:**
- Audit 21 (Technical SEO Scan): CrUX field data instead of estimated lab data. Real LCP, CLS, INP from actual user visits. Shows 75th percentile (what most users experience).

---

## Setup — Google Analytics 4 (optional)

**What you need:** GA4 property with data, same Google Cloud project.

1. Enable the **Google Analytics Data API** in Cloud Console
2. Add the service account email as a viewer in GA4 → Admin → Account Access Management
3. Set:
   ```
   export GA4_PROPERTY_ID="123456789"
   export GA4_KEY_FILE="/path/to/your-service-account.json"
   ```
   (Can reuse the same key file as GSC if same service account)

**What changes:**
- Audit 10 (Money Page): real traffic per page, not estimated
- Audit 20 (Monthly Report): pulls actual sessions, conversions, channel data
- Audit 25 (Content Refresh): identifies decaying pages by real traffic drop, not just content age

---

## Fallback Behavior

If a key is missing or a call fails, ENOLA SEO falls back to browser mode for that specific data point. It will tell you:

> "GSC key not found — running keyword gap from browser data instead. Results will be directional, not exact."

No audit fails completely. API mode enhances — it does not replace.

---

## For Agencies

Running audits for clients: set keys per-client using a `.env` file in the working directory.

```
# .env (in /your-client-project/)
GSC_KEY_FILE=/path/to/client-service-account.json
GSC_SITE_URL=https://clientdomain.com/
PAGESPEED_API_KEY=your-key
GA4_PROPERTY_ID=987654321
GA4_KEY_FILE=/path/to/client-service-account.json
```

ENOLA SEO reads from environment variables. If you use `direnv` or load `.env` before launching Claude Code, the keys are available automatically.

Client keys stay separate. No cross-contamination between client projects.

---

## Which Mode Should You Use?

| | Browser Mode | API Mode |
|--|:------------:|:--------:|
| Works immediately | ✅ | Setup required |
| No API keys needed | ✅ | ❌ |
| Real traffic data | ❌ | ✅ |
| Real search rankings | ❌ | ✅ |
| Real Core Web Vitals | ❌ | ✅ |
| Best for | Individuals, small businesses | Agencies, power users |

---

*© Sean Gal | enolarevenu.com — MIT Licensed*
