# THIS IS THE ARTICLE I ALMOST DIDN'T PUBLISH.

I built an AI system that audits your entire Google presence, finds every gap your competitors are exploiting, and writes you a ranked execution plan.

I'm giving it away for free.

Not a watered-down version. The whole thing. 26 prompts. The thinking behind each one. And a downloadable skill file that runs it all automatically.

Here's everything.

---

## WHAT THIS IS AND WHY IT EXISTS

I've built over 30 websites.

Different countries. Different languages. Different niches. Affiliate marketing, information sites, lead generation. Sites that ranked on page 1 and generated commissions while I slept. Sites that beat competitors with 10x my budget and 100x my brand recognition.

I didn't start with an advantage. I started with a domain and a wrong assumption about how Google worked.

What I built over the years — through testing, failure, rebuilding, and testing again — was a repeatable system. The same levers. The same order. The same logic that worked in Thailand worked in English markets. The same fundamentals that ranked affiliate sites ranked local service businesses.

Then I automated it.

When Claude Code launched with real browser access — the ability to actually open URLs, browse live pages, pull real competitor data — I saw exactly what was possible.

Everything I knew could become a prompt.

Not a generic prompt.

A context-aware, business-specific, browse-first prompt that produces real output — copy, templates, action plans, saved files — not generic advice you could have Googled yourself.

I call it ENOLA SEO. It's the marketing intelligence layer of Enola Revenue — an AI-powered business operating system built on the Hubbard Seven-Division Org Board framework. Division 2 is marketing. This is what happens when you give Division 2 a complete operating system.

It runs in Claude Code. It interviews you once. It saves everything to files on your machine. And it's completely free.

You can copy every prompt from this article one by one.
Or you can download the whole skill from GitHub and let it run automatically.

Both work. The prompts are the same either way.

---

## WHY MOST BUSINESSES LOSE ON GOOGLE

Before we get into the prompts — you need to understand the actual problem.

Most local businesses losing on Google aren't losing because their competitors are smarter, better funded, or more experienced. They're losing because of three fixable things they don't know about.

**Thing 1: Wrong GBP categories.**
Your Google Business Profile has a primary category and secondary categories. Most business owners set this up when they created the listing and never touched it again. Meanwhile their competitors added secondary categories that directly control which searches trigger their listing in the map pack. Wrong categories = invisible for entire search categories. One change. One week. New searches appearing.

**Thing 2: Review velocity, not review count.**
A business with 200 reviews that got 180 of them two years ago is weaker than a business with 90 reviews getting 15 a month. Google tracks momentum. Most businesses look at their star rating and feel good. They should be calculating their monthly velocity and setting a target.

**Thing 3: NAP inconsistency.**
Name, Address, Phone — if these are listed differently across directories, Google doesn't fully trust your listing. Wrong phone number on Yelp. Old address on Apple Maps. Each inconsistency is a small trust signal working against you. Fixing citations is one of the only SEO tasks where you can see real movement within 30 days.

Fix these three things and most businesses move. Everything else in this article amplifies what you've already built. But if the foundation is broken, nothing amplifies.

---

## THE SETUP — DO THIS BEFORE ANYTHING ELSE

This is the step 90% of people skip. It's also why 90% of people get generic AI output.

Before any prompt runs, Claude needs to know your business. Not as a one-time message. As permanent context that loads before every single audit.

Copy this. Fill in every bracket. Paste it into Claude Code first — before anything else.

```
Here is everything you need to know about my business.
Use this as the base for every audit you run.
Never ask me for this information again.

BUSINESS BASICS
Business name: [your business name]
Address: [full address]
Phone: [phone number]
Website: [website URL]
Google Business Profile URL: [GBP URL — the maps.google.com link]
Primary service: [what you do]
Secondary services: [service 2], [service 3], [service 4]
Service areas: [city 1], [city 2], [city 3], [city 4], [city 5]
Years in business: [X]
Team size: [solo / small team / large team]
Target customer: [who your best customer is]
Average job value: [$X]

SEO SITUATION
Top 5 keywords I want to rank for: [kw1], [kw2], [kw3], [kw4], [kw5]
Keywords I currently rank for: [kw1], [kw2]
Keywords I should rank for but don't: [kw1], [kw2]
Google reviews: [X] total, [X] star rating, [X] new per month
GBP monthly views: [X impressions — check GBP insights]
Monthly website traffic: [X visits — estimate is fine]
Map pack status: [ranking for X, not ranking for Y]
Biggest SEO problem right now: [one honest sentence]

COMPETITORS
[Competitor 1] — [GBP URL] — [website] — [why they're beating you]
[Competitor 2] — [GBP URL] — [website] — [why they're beating you]
[Competitor 3] — [GBP URL] — [website] — [why they're beating you]

WHAT I'VE ALREADY TRIED
[Any SEO work done — agency, DIY, tools, what worked, what didn't]

HOW I WANT YOU TO WORK
Always prioritize quick wins unless I ask otherwise.
Tell me impact level (HIGH/MED/LOW) and timeline for every recommendation.
Output comparison data in table format.
Write actual copy — never use placeholders like [your keyword here].
Browse real URLs before every audit. Don't guess when you can look.
Never ask me for this information again.
```

That last line does the work. It tells Claude to treat this as infrastructure — not a chat message.

Once this is loaded, every prompt that follows stops being generic. Claude isn't answering a stranger's SEO question anymore. It's answering yours.

---

## THE 26 PROMPTS

I've organised these into five sections in the same order I run them.

Don't run all 26 at once. The order matters. Quick wins first, infrastructure second, compounding plays third.

The execution order is at the end.

---

## PART 1 — GOOGLE BUSINESS PROFILE
*Prompts 1–8. This is always where I start. Your GBP is more important than your website for local search. Most businesses treat it like a directory listing. The ones winning the map pack treat it like a product.*

---

### PROMPT 01 — GBP CATEGORY AUDIT

This is the first thing I run on every business. If your categories are wrong, nothing else matters. Categories control which searches trigger your listing. One wrong category and you're invisible for entire intent clusters you should be dominating.

I've seen businesses add one secondary category and start ranking for a new set of searches the following week. That's not theory. That's what actually happens.

The pattern recognition is the real value here. When you map categories against map pack rankings you start seeing things. Every business ranking for "emergency plumber in [city]" also has "water damage restoration" as a secondary. That pattern is invisible until you do this analysis.

```
Open Chrome and go to Google Maps.
Search [primary service] in [city] for my top 3 target keywords.
For each search, note which competitors appear in the Map Pack.
Open each competitor's GBP listing and extract their primary category
and every secondary category listed.
Build a comparison spreadsheet:
  ∙ One tab per keyword
  ∙ Columns: business name | primary category | secondary categories |
    star rating | review count | ranking position
  ∙ Highlight every category my competitors have that I'm missing
Then give me a prioritized add-list:
  ∙ Tier 1: categories ALL competitors share — non-negotiable, add this week
  ∙ Tier 2: categories most competitors share — strong recommendation
  ∙ Tier 3: categories only one competitor has — differentiation opportunity
For each missing category:
  ∙ Which searches it unlocks
  ∙ Estimated map pack impact
  ∙ Exact steps to add it in GBP
```

---

### PROMPT 02 — GBP ATTRIBUTES AUDIT

Most business owners don't know GBP attributes exist. The ones that do know they exist don't know they affect rankings.

Attributes are the small tags on your listing. "Veteran-owned." "Free estimates." "24/7 availability." "Wheelchair accessible." Google uses these to match specific searches to specific listings. Someone searches "woman-owned cleaning company" — Google looks at which GBP listings have that attribute. Someone searches "24 hour plumber near me" — same thing.

Your competitors have attributes you don't. This audit finds every one of them.

```
Open Chrome and go to my GBP at [URL] and these competitors:
[URL1], [URL2], [URL3].
Extract every visible attribute and tag from each listing.
Build a comparison table:
Columns: attribute | my listing (Y/N) | comp 1 (Y/N) | comp 2 (Y/N) | comp 3 (Y/N)
Produce three lists:
  1. Attributes ALL competitors have — table stakes, I need these immediately
  2. Attributes MOST competitors have — strong recommendations
  3. Attributes only ONE has — differentiation opportunities
For each attribute I'm missing:
  ∙ Ranking impact: HIGH / MED / LOW
  ∙ CTR impact: yes / no
  ∙ Exact steps to add in GBP
```

Attributes are a two-for-one play. They help you rank for more specific searches AND they increase click-through rate because those small trust signals appear before someone even clicks your listing.

---

### PROMPT 03 — REVIEW TEARDOWN

Star rating tells you almost nothing.

What actually matters is velocity — how fast your competitors are getting new reviews compared to you. A business with 200 reviews that got 180 of them two years ago is genuinely weaker than a business with 90 reviews getting 15 a month. Google tracks recency. Most businesses look at their total count and feel safe.

The second insight is in the language. "Great furnace install in Highland Park" is doing SEO work for that competitor whether they know it or not. Reviews with keywords and location names are ranking signals. This audit extracts exactly which words are working — so you can train your own customers to use them.

```
Open Chrome and go to these competitor GBP listings: [URL1], [URL2], [URL3].
Read their last 50 reviews each.
Extract per competitor:
  ∙ Total reviews + star rating
  ∙ Reviews in last 30 / 60 / 90 days — calculate monthly velocity
  ∙ Top 5 services mentioned by name in reviews
  ∙ Top 5 neighborhoods or cities mentioned
  ∙ Any staff names mentioned (these are ranking signals)
  ∙ Recurring complaints — these are weaknesses I can exploit
  ∙ Exact phrases customers use when recommending — these are money phrases
Compare their velocity to mine at [my GBP URL].
Calculate:
  ∙ How many reviews per month do I need to catch the leader?
  ∙ How long will it take at my current rate?
  ∙ How long if I double my current rate?
Output:
  ∙ Velocity gap table
  ∙ Top 10 phrases to train my customers to mention
  ∙ Word-for-word review request script — something I can send after every job
```

---

### PROMPT 04 — REVIEW RESPONSE SYSTEM

Getting reviews is half the game. How you respond is the other half.

Google has confirmed that responding to reviews improves local ranking. But most businesses either don't respond at all or paste "thanks for your review!" on everything. Both are leaving ranking signals on the table.

Your review responses are free keyword real estate. 10 responses a month, each mentioning your service and city — that's 120 pieces of keyword-rich content added to your GBP per year that didn't exist before. And how you handle negative reviews directly determines whether new customers trust you or scroll past.

```
Open Chrome and go to my GBP at [URL] and these competitors:
[URL1], [URL2], [URL3].
Read the last 30 owner responses from each listing.
Note per listing:
  ∙ Response rate (responses / total reviews as %)
  ∙ Whether responses mention specific services
  ∙ Whether responses mention specific locations or neighborhoods
  ∙ Average response length and tone
  ∙ How negative reviews are handled
Build a comparison spreadsheet.
Then write a complete review response system:
  ∙ 3 variations for 5-star reviews
    (naturally include [service keyword] + [city], 40-80 words each)
  ∙ 3 variations for 4-star reviews
    (acknowledge the slight gap, invite return)
  ∙ 3 variations for 3-star reviews
    (accountability + resolution, no excuses)
  ∙ 3 variations for 1-2 star reviews
    (professional, empathetic, defuse negativity — never defensive)
Every template must sound like a real person wrote it.
Not a PR department. Not a robot.
Each 5-star template must include at least one keyword from: [keywords]
```

---

### PROMPT 05 — GBP POSTS STRATEGY

GBP posts are the most underused feature on the platform. Most businesses don't know they exist.

Posts appear directly on your listing. They expire after 7 days. Posting consistently signals to Google that your business is active. Active businesses get preferred placement.

The competitor analysis almost always reveals the same thing: nobody's posting. That gap is yours right now.

The real play inside this prompt is the neighborhood-specific content. Every post mentioning "just completed a roof replacement in [neighborhood]" builds location relevance. Google starts associating your business with that area. Do this across 8-10 neighborhoods every month and you're building local authority that's extremely hard to replicate.

```
Open Chrome and go to my GBP at [URL] and these competitors:
[URL1], [URL2], [URL3].
Check the posts section for each listing.
Record per listing:
  ∙ Total posts in last 90 days
  ∙ Average post frequency per week
  ∙ Post types used (offer / update / event / product)
  ∙ Topics and themes covered
  ∙ Whether posts include images and CTAs
  ∙ Seasonal patterns
  ∙ Gaps in their posting schedule
Build a comparison spreadsheet.
Then build an 8-week GBP posting calendar:
  ∙ 2-3 posts per week
  ∙ Mix of: seasonal promotions, before/after showcases,
    neighborhood-specific posts mentioning [area1], [area2], [area3],
    review highlights, team spotlights, educational content
  ∙ Every post: 100-150 words, 1 target keyword minimum, clear CTA,
    image description (exact shot to take)
Write full copy for weeks 1-4.
Detailed outlines for weeks 5-8.
Format: Week | Day | Type | Full Copy | Image Description
```

---

### PROMPT 06 — SERVICES COPY

Google gives you an entire section to describe your services. This is prime keyword real estate where you control every word. Reviews are written by customers. Q&A can come from anyone. But service descriptions? That's your copy. Your keywords. Your positioning.

Most businesses leave it blank or write one line with no keywords. That's like having a landing page with just a title.

The cross-reference against your website is where this gets interesting. Businesses add new services to their site and forget to update their GBP. If you do "trenchless sewer repair" but it's not on your GBP, you don't exist for that search in the map pack.

```
Open Chrome and go to my GBP services section at [URL]
and these competitors: [URL1], [URL2], [URL3].
Extract every service listed — whether it has a description,
how long the description is, how it's structured.
Cross-reference against my website at [URL]:
  ∙ Services on my site not on my GBP
  ∙ Services on my GBP with no description
  ∙ Services where my description is weaker than competitors
Write optimized descriptions for every service I offer.
Per service:
  ∙ 40-60 words
  ∙ Primary service keyword included naturally
  ∙ Specific service area mentioned
  ∙ Customer outcome stated — what they GET, not what I DO
  ∙ Sounds like a real business, not an SEO tool
Flag the top 3 services by keyword opportunity.
Output: complete services section, paste-ready into GBP.
```

---

### PROMPT 07 — GBP DESCRIPTION

750 characters. Most businesses waste every single one.

They either leave the description blank, copy-paste from their website, or stuff it with keywords that read like a bot wrote them. Your description needs to do three things simultaneously: carry your primary keywords naturally, mention your core service areas, and convince someone to pick you over the five other businesses on their screen.

Three versions lets you test. Run version 1 for 30 days. Check impressions and calls. Try version 2. Most people write one description and never touch it again. Treating it as a testable asset gives you a compounding edge nobody else in your market is working.

```
Open Chrome and go to my GBP at [URL]
and these competitors: [URL1], [URL2], [URL3].
Extract the full description from every listing.
Analyze:
  ∙ Character count
  ∙ Keywords used
  ∙ Service areas mentioned
  ∙ Unique selling points stated
  ∙ CTA included or not
  ∙ Overall tone
Find: what ALL top competitors mention — non-negotiable elements
Find: what nobody mentions — the gap I can own
Write 3 versions of my GBP description, all under 750 characters:
Version 1 — KEYWORD: maximum ranking signal, every character working
Version 2 — CONVERSION: make someone call right now, urgency + clarity
Version 3 — TRUST: years in business, review count, local credibility
Each version: character count + keywords included + one-line strategy note
Recommend: which version to test first + what metric to watch over 30 days
All three must include: [keyword1], [keyword2], [keyword3]
and service areas: [area1], [area2], [area3]
Make them sound like a human wrote them — not a marketing team.
```

---

### PROMPT 08 — PHOTO PLAN

Businesses with photos get 42% more direction requests and 35% more click-throughs. But it's not about having photos — it's about uploading consistently and making every photo work as a ranking signal.

Most businesses uploaded 10 blurry phone pictures three years ago and stopped. The businesses dominating the map pack upload every week, geotag every image to a specific neighborhood, and name their files with service keywords.

Consistency beats volume. 50 photos in one day then nothing for 6 months tells Google you're not active. 3-5 quality photos every week tells Google your business is alive. The naming convention and geotagging instructions in this prompt alone are worth more than most paid SEO advice.

```
Open Chrome and go to my GBP at [URL]
and these competitors: [URL1], [URL2], [URL3].
For each listing record:
  ∙ Total photos
  ∙ Photos uploaded in last 30 days
  ∙ Photos uploaded in last 90 days
  ∙ Photo types: team, job site, before/after, trucks, equipment,
    storefront, completed work
  ∙ Quality: professional vs phone shots
  ∙ Whether photos show specific neighborhoods or local landmarks
  ∙ Upload frequency per week
Build a comparison spreadsheet.
Then build an 8-week photo upload plan:
  ∙ Photos per week needed to beat top competitor velocity by 50%
  ∙ Specific shot list per week: what to photograph, where, why it ranks
  ∙ Rotation priority: before/after early (highest trust signal),
    then team, trucks, completed work
  ∙ Naming convention with service keywords + location names
    (example: hvac-repair-chicago-north-side-01.jpg)
  ∙ Geotagging instructions for each service area:
    [area1], [area2], [area3]
  ∙ List of photos that actively hurt rankings
    (stock images, blurry shots, irrelevant content)
Format: 8-week plan table + naming examples + geotagging guide
```

---

## PART 2 — WEBSITE
*Prompts 9–13. Your GBP gets people to click. Your website converts them. But first it has to rank. Most local business websites have the wrong pages ranking — or no pages ranking at all.*

---

### PROMPT 09 — KEYWORD GAP AUDIT

The revenue your website should be generating is hiding in keywords your competitors rank for that you don't. This prompt finds every single one of them.

The filter is what makes this useful instead of overwhelming. Most keyword gap tools return thousands of results. Filtered to local intent, realistic volume, and buyer-intent language — you get 20 keywords worth actually pursuing.

```
Open Chrome and go to my website at [URL] and these competitor websites:
[comp1.com], [comp2.com], [comp3.com].
Identify keywords competitors rank for that I don't.
Filter to local intent only:
  ∙ Contains city name, area, "near me", "emergency", "best", "local"
  ∙ Buyer intent: commercial or transactional searches only
  ∙ Realistic search volume (not zero, not dominated by national brands)
  ∙ Keyword difficulty I can realistically compete for
For the top 20 gaps:
  ∙ Volume tier: HIGH / MED / LOW
  ∙ Difficulty: EASY / MED / HARD
  ∙ Buyer intent stage (1-4, where 4 = ready to hire)
  ∙ Page type needed: service page / city page / blog / GBP
  ∙ Action: optimize existing page OR create new page
Sort by: highest volume + lowest difficulty = top priority.
Output: prioritized table + top 5 immediate actions this week.
```

---

### PROMPT 10 — MONEY PAGE AUDIT

Most local business websites are sitting on page 2 rankings that are one title tag change away from page 1. This is the lowest-hanging fruit in SEO and almost nobody is picking it.

A jump from position 15 to position 5 is worth more than creating 10 new pages. This prompt finds every opportunity and writes every fix.

```
Open Chrome and browse my website at [URL].
Identify pages likely sitting on page 2 for high-value keywords —
common patterns for [business type].
For each opportunity, diagnose the gap:
  ∙ Title tag missing keyword or too weak?
  ∙ H1 not matching search intent?
  ∙ Content too thin (under 500 words)?
  ∙ No internal links pointing to this page?
  ∙ Meta description killing CTR?
Build a 30-day sprint with actual copy for every fix:
Week 1: Rewrite title tags + H1s for top 5 opportunities
(write the exact new text — not instructions)
Week 2: Content additions
(what to add, approximate word count, where on page)
Week 3: Internal linking map
(which pages link where, exact anchor text)
Week 4: Meta description rewrites for low-CTR pages
(write the actual new copy)
Every fix is written out.
No recommendations without the actual text.
```

---

### PROMPT 11 — CITY PAGE BUILDER

Google ranks pages, not websites. If you don't have a page specifically about [service] in [city], you will not rank for that search. That's not an opinion. That's how the index works.

Most businesses have one generic service page and wonder why they don't appear in cities 20 minutes away. This prompt builds the entire location page stack — the work that would take a team of writers weeks gets done before lunch.

```
Open Chrome and check my website at [URL].
Identify: which city + service combination pages already exist.
Find: every missing combination across my services and cities.
For each missing page, write a complete optimized page:
SEO title: under 60 chars, [service] + [city], natural
Meta description: under 155 chars, service + city + reason to click
H1: natural, not keyword-stuffed
Opening paragraph: 100 words — the specific pain point of someone
in THAT city needing THIS service right now
Why Us section: 150 words — city-specific references where possible
Service Details: 200 words — process, what's included, what they get
FAQ: 3 questions specific to customers in that city
CTA: phone number + "Call now for same-day service in [city]"
URL slug: exact
Internal links: 2-3 suggestions from existing pages
B2B note: add industry-specific sections, longer form, different CTA.
Output: one complete page per city, paste-ready into CMS.
```

---

### PROMPT 12 — SEARCH CONSOLE SPRINT

Most business owners log into Google Search Console, feel overwhelmed by the data, and close the tab. This prompt makes sense of all of it and builds a 30-day plan with every fix already written.

Page 2 keywords are pure opportunity. Someone is already searching for exactly what you offer. You're just one optimization push away from being visible to them.

```
Open Chrome and review my website structure at [URL].
Identify page 2 keywords — positions 11-20 — common for [business type].
These are the highest-priority optimization targets.
A jump from position 15 to position 5 is worth more than 10 new pages.
For each page 2 keyword:
  ∙ Is the keyword in the title tag?
  ∙ Is it in the H1?
  ∙ Is it in the first 100 words?
  ∙ How many words is the page?
  ∙ Does it have internal links pointing to it?
  ∙ What does the current meta description say?
Build a 30-day sprint with actual copy for every fix:
Week 1: New title tags + H1s — write the exact text
Week 2: Content to add — what + word count targets
Week 3: Internal linking — exact pages + anchor text
Week 4: Meta description rewrites for high-impression/low-click pages
Flag quick wins: fixes that can be done in under 10 minutes.
Impact estimate per fix: HIGH / MED / LOW.
```

---

### PROMPT 13 — REVIEW SENTIMENT ANALYSIS

This is the prompt most agencies don't know exists.

Most businesses write their website copy about themselves. The businesses that dominate write their copy in the language their customers actually use. There's a difference between what you think your customers care about and what they actually say when they tell a friend about you.

Review sentiment analysis finds that language. The exact emotional words. The specific outcomes they mention. The fears they had before calling you. The phrases that make a stranger trust you enough to pick up the phone.

```
Open Chrome and go to these competitor GBP listings:
[URL1], [URL2], [URL3].
Read the last 100 reviews for each competitor.
Extract:
  ∙ Top 20 emotional words customers use most
    (relieved, finally, trustworthy, professional, impressed…)
  ∙ Top 10 specific outcomes mentioned
    (fixed in one visit, no mess left behind, arrived on time…)
  ∙ Top 5 fears or frustrations before the service
    (worried it would cost a fortune, other companies canceled…)
  ∙ Exact phrases used when recommending to others
    (these are the money phrases — copy these verbatim)
  ∙ Language that appears in 5-star reviews but NOT in 3-star reviews
Compare: competitor review language vs my review language at [my GBP URL].
Where are the emotional gaps?
Then use all of this to rewrite:
  ∙ My GBP description — using the emotional language real customers use
  ∙ My homepage headline + subheadline
  ∙ My review request script — so customers naturally say the right words
  ∙ 3 social proof statements for my website that mirror how my best
    customers actually talk about my service
```

---

## PART 3 — AUTHORITY
*Prompts 14–16. Authority is what makes rankings stick. Without it, you can optimize everything and still get outranked by a worse business with more trust signals.*

---

### PROMPT 14 — BACKLINK STRATEGY

Backlinks are trust transfer. You don't need hundreds. You need the right ones from the right sources.

2-4 real contextual links per month compounds faster than 20 random directory submissions. This prompt finds exactly where your competitors are getting their authority from, tells you how they earned each link, and writes the outreach email you can send today.

```
Open Chrome and browse competitor websites: [comp1.com], [comp2.com], [comp3.com].
Look for visible link patterns — directories, news mentions,
associations, sponsor pages, industry publications.
Categorize by ease of replication:
  ∙ Easy: directories, citations, local associations
  ∙ Medium: local news features, sponsor opportunities, guest posts
  ∙ Hard: industry publications, local government, universities
Build a 90-day link building plan:
Month 1 — 5 easy links:
Exact sites + full submission text or outreach email per link
Month 2 — 5 medium links:
Pitch angle + full outreach email per link
Month 3 — 5 authority links:
Strategy + full outreach email per link
For every link: write the complete email or submission copy.
Focus on links a local owner can get without an agency or a budget.
B2B: heavier emphasis on industry associations and case study features.
```

---

### PROMPT 15 — CITATION AUDIT

Citations are how Google verifies your business is real. Inconsistent NAP data across directories is one of the most common local SEO problems and most businesses have no idea how many wrong citations are actively working against them.

If your phone number is listed differently on Yelp than on Google, it creates a trust signal conflict that suppresses your rankings. Fixing citations is one of the few SEO tasks where you can see real movement within 30 days of making the changes.

```
Open Chrome and search for my business across these platforms one by one:
Google Business Profile, Yelp, Bing Places, Apple Maps, Facebook, BBB,
Angi, HomeAdvisor, Thumbtack, Houzz, Yellow Pages, Manta, Foursquare,
Superpages, and any industry-specific directories for [industry].
My correct NAP:
Name: [exact business name]
Address: [exact address]
Phone: [phone number]
Website: [URL]
For each platform record:
  ∙ Listing exists: Y/N
  ∙ Name as listed (exact)
  ∙ Address as listed (exact)
  ∙ Phone as listed (exact)
  ∙ Duplicate listings: Y/N
Flag every inconsistency.
Output:
  ∙ Audit table with all findings
  ∙ Priority fix list (which inconsistencies hurt rankings most)
  ∙ Step-by-step fix instructions per platform
  ∙ High-value directories where I have no listing yet
  ∙ Monthly citation maintenance checklist
```

---

### PROMPT 16 — SEARCH INTENT MAP

Most businesses optimize for the wrong keywords. They chase high-volume awareness terms and ignore the low-volume, high-intent searches that actually generate calls.

Stage 4 keywords have lower search volume but they convert at 5-10x the rate of Stage 2 keywords. This prompt maps your entire keyword universe to the buyer journey so you know exactly where your effort should go — and stops you from wasting months on keywords that never turn into revenue.

```
For [business type] in [city] offering [service1], [service2], [service3]:
Map the keyword universe into 4 buyer journey stages:
Stage 1 — UNAWARE: has a problem, doesn't know what it's called
e.g. "water coming through ceiling", "AC making weird noise"
Stage 2 — AWARE: knows the problem, researching solutions
e.g. "how to fix leaking roof", "why is my AC not cooling"
Stage 3 — COMPARING: evaluating options and providers
e.g. "plumber vs DIY", "how to choose HVAC company"
Stage 4 — READY: wants to book now
e.g. "emergency plumber [city]", "HVAC repair near me"
For each stage:
  ∙ 10 example keywords with volume tier
  ∙ Average conversion rate comparison
  ∙ Content type that should target these keywords
Content strategy per stage:
Stage 4 → service pages + GBP (where the money is)
Stage 3 → comparison + FAQ pages
Stage 2 → educational blog content → funnels to service pages
Stage 1 → problem-identification content → builds early trust
Top 5 Stage 4 keywords for my business:
For each: current status + 90-day ranking plan
```

---

## PART 4 — CONTENT
*Prompts 17–20. Content is what builds the compounding moat. Once it ranks, it works for free, forever. These prompts find what to create and how to make it last.*

---

### PROMPT 17 — CONTENT GAP ANALYSIS

Your competitors are ranking for searches your customers are doing right now. Every one of those searches is a call going to someone else.

The filter matters here. 50-500 searches per month is the local content sweet spot — real volume, low enough competition to win without a domain authority of 80. Problem-awareness content gets prioritized first because it answers objections before the phone call even happens.

```
Open Chrome and browse competitor websites:
[comp1.com], [comp2.com], [comp3.com].
Compare against my site at [URL].
Find content competitors have that I don't.
Filter to:
  ∙ 50-500 searches per month (local sweet spot)
  ∙ Question keywords: how, why, what, when, is, can, does
  ∙ Problems my service solves
Organize top 20 gaps into 3 categories:
  ∙ Problem-awareness: "why is my X doing Y"
  ∙ Solution-comparison: "repair vs replace X"
  ∙ Local service: "X service in [city] cost"
For each of the 20, write a complete content brief:
  ∙ SEO title
  ∙ URL slug
  ∙ Target keyword + secondary keywords
  ∙ Main questions to answer
  ∙ Recommended word count
  ∙ Internal linking opportunities
  ∙ CTA at bottom
  ∙ 200-word summary of what the page covers
Prioritize problem-awareness content first.
It does the most work for local businesses by answering objections
before the phone call.
```

---

### PROMPT 18 — ENTITY OPTIMIZATION

This is the most advanced prompt in this article. Most local SEOs don't know this lever exists.

Google doesn't just rank websites. It ranks entities. Your business needs to exist as a verified entity in Google's knowledge graph to unlock the highest level of local trust signals. Businesses with strong entity signals rank higher, get more citations in AI Overviews, and are more resilient to algorithm updates.

This is infrastructure. It takes time to build and years to fully compound. Start now.

```
Open Chrome and search "[business name] [city]" on Google.
Note: does a Knowledge Panel appear?
Search "[business name]" on wikidata.org.
Note: does my business exist as an entity?
Go to search.google.com/test/rich-results and enter my website URL.
Note: what schema is currently implemented and what's missing?
My business details for entity building:
Name: [exact business name]
Address: [full address]
Phone: [phone number]
Website: [URL]
GBP: [GBP URL]
Founded: [year]
Industry: [industry]
Build a complete entity optimization plan:
  1. LocalBusiness schema markup — write the complete JSON-LD
     ready to paste into my homepage
     Include: name, address, phone, url, geo coordinates,
     openingHours, serviceArea, priceRange,
     aggregateRating if reviews exist
  2. Platform list for entity signals:
     LinkedIn company page, industry associations,
     local chamber, Crunchbase if eligible,
     Knowledge Panel trigger strategy
  3. Brand mention strategy: anchor text patterns to build across the web
  4. 90-day entity build checklist — week by week
This is SEO infrastructure. Treat it accordingly.
```

---

### PROMPT 19 — GBP POSTING PATTERNS

Everyone knows posting on GBP matters. Almost nobody knows when to post, what format performs, or which topics actually drive map pack visibility.

This prompt reverse-engineers everything your top competitors have figured out about GBP posting. The timing. The format. The seasonal patterns. The gaps in their schedule. Then it builds you a strategy based on what's already proven to work in your specific market — not generic advice.

```
Open Chrome and go to the GBP listings for these competitors:
[URL1], [URL2], [URL3].
Analyze their full visible posting history.
For each post record:
  ∙ Date + day of week + approximate time
  ∙ Post type: offer / update / event / product
  ∙ Word count
  ∙ Image: yes/no
  ∙ CTA button: yes/no + what it says
  ∙ Topic and service mentioned
  ∙ Specific neighborhood or city mentioned
  ∙ Price or offer included: yes/no
Build a full spreadsheet — one row per post.
Then analyze patterns:
  ∙ Best days and times for posting
  ∙ Post types they use most in their active periods
  ∙ Seasonal spikes — which months are heaviest
  ∙ Gaps in their schedule — windows to dominate unchallenged
Build my posting strategy from the actual data:
  ∙ Optimal cadence, days, times, post type mix for my market
  ∙ Not generic advice — built from reverse-engineering my specific competitors
Write the first 4 weeks of posts in full (2-3 per week):
  ∙ Day, time, type, full copy (100-150 words), keyword, CTA, image description
Weeks 5-8: topic outlines.
```

---

### PROMPT 20 — MONTHLY SEO REPORT

Most business owners track the wrong things. Total traffic looks good on a slide. Domain rating sounds impressive. Neither tells you if SEO is making you money.

Calls from GBP. Direction requests. Organic clicks. These are the numbers connected to your bank account. Everything else is vanity until those move.

```
Open Chrome and access:
  ∙ Google Search Console for [yourdomain.com]
  ∙ Google Business Profile insights at [GBP URL]
  ∙ Google Analytics 4 for [yourdomain.com] if available
Pull last 30 days vs previous 30 days for every metric.
From Search Console:
  ∙ Total organic clicks + change
  ∙ Total impressions + change
  ∙ Average CTR + change
  ∙ Average position + change
  ∙ Top 10 keywords by clicks
  ∙ Top 10 keywords that improved in position
  ∙ Top 10 keywords that dropped
From GBP Insights:
  ∙ Profile views + change
  ∙ Calls + change (this is the headline metric)
  ∙ Direction requests + change
  ∙ Website clicks + change
  ∙ Review count change
  ∙ Photo views
From GA4 if available:
  ∙ Organic sessions
  ∙ Organic conversion rate
  ∙ Top organic landing pages
Build a one-page monthly report:
  ∙ 3 WINS this month
  ∙ 3 PROBLEMS to address
  ∙ The single most important action next month
  ∙ GBP calls: up or down
Readable in 5 minutes.
Shareable with any team member or VA.
Also write: 5-minute monthly review checklist — exactly what to check, in order.
```

---

## PART 5 — ADVANCED
*Prompts 21–26. These go deeper. Technical infrastructure, AI search visibility, content health scoring, hard blockers, decaying content, and the full PDF export. Run these after the first 20 are done — or run 24 first if something is actively broken.*

---

### PROMPT 21 — TECHNICAL SEO SCAN

Most local businesses have at least one technical problem costing them rankings. A page that loads in 6 seconds on mobile. A sitemap that doesn't exist. Schema markup that's wrong or missing entirely.

Technical issues are invisible until you look for them. And they silently undermine everything else you're doing.

```
Open Chrome and browse my website — homepage + top 3 service pages.
Check and grade each category: PASS / WARN / FAIL

SPEED + CORE WEB VITALS
  ∙ Mobile page load time (target: under 3 seconds)
  ∙ Largest Contentful Paint: PASS <2.5s | WARN 2.5-4s | FAIL >4s
  ∙ Cumulative Layout Shift: PASS <0.1 | WARN 0.1-0.25 | FAIL >0.25
  ∙ Interaction to Next Paint: PASS <200ms | WARN 200-500ms | FAIL >500ms
  ∙ Image sizes and formats (WebP? Compressed?)
  ∙ Render-blocking resources

CRAWLABILITY
  ∙ robots.txt exists + valid syntax
  ∙ sitemap.xml exists + accessible
  ∙ No pages accidentally set to noindex
  ∙ Canonical tags present and consistent
  ∙ Internal links working (no 404s in main navigation)

MOBILE
  ∙ Viewport meta tag present
  ∙ Touch targets minimum 44x44px
  ∙ Text readable without zooming
  ∙ No horizontal scroll

SCHEMA MARKUP
  ∙ LocalBusiness schema present
  ∙ Required fields complete: name, address, phone, url, geo
  ∙ AggregateRating schema if reviews exist
  ∙ Any validation errors

SECURITY
  ∙ HTTPS active
  ∙ HTTP → HTTPS redirect working
  ∙ No mixed content (HTTP resources on HTTPS pages)

META TAGS
  ∙ Title tags: 30-60 chars, unique per page
  ∙ Meta descriptions: 120-160 chars, unique per page
  ∙ One H1 per page, matches search intent

Output:
  ∙ Scorecard table: Category | Status | Issue | Fix | Impact
  ∙ Hard blockers section — fix before anything else
  ∙ Quick wins section — under 10 minutes each
  ∙ Full fix instructions for every FAIL and WARN
```

---

### PROMPT 22 — GEO AUDIT

GEO = Generative Engine Optimization.

Google AI Overviews, ChatGPT, Perplexity, and Claude now answer local service questions directly. "Best plumber in [city]" is becoming an AI-generated answer, not a list of links. If your business isn't in those answers, you're invisible to a growing percentage of buyers who never scroll to the organic results.

This is where local SEO is going. The businesses that optimize for AI citations now will have an insurmountable advantage by 2027.

```
Open Chrome and search "[primary service] in [city]" on Google.
Note: does an AI Overview appear? Does my business appear in it?
Check my website for GEO signals:

QUOTABILITY
  ∙ Does my content have direct, quotable answers to common questions?
  ∙ Clear who/what/where/when/how much statements?
  ∙ Statistics or specific data points AI systems can cite?
  ∙ Named experts or credentials that build authority?

STRUCTURE FOR AI PARSING
  ∙ FAQ sections with direct Q+A format?
  ∙ Clear heading hierarchy (H1 > H2 > H3)?
  ∙ Schema markup that makes entity relationships clear?
  ∙ Concise service definitions (AI systems love these)?

ENTITY CLARITY
  ∙ Is my business clearly identified as a real local entity?
  ∙ Name, location, service area stated explicitly on multiple pages?
  ∙ Consistent brand mentions across citations?

FRESHNESS
  ∙ Content dated recently?
  ∙ Any pages with obviously outdated information?
  ∙ Last-modified signals in schema?

Score each category: STRONG / WEAK / MISSING
Build a GEO optimization plan:
  ∙ Top 5 content changes to become AI-citable
  ∙ Write a FAQ section — 5 questions + direct answers for my top searches
  ∙ Schema additions that improve AI parsing
  ∙ One citation bait content piece — brief + outline
Output: GEO scorecard + FAQ copy written in full + schema additions
```

---

### PROMPT 23 — CONTENT QUALITY SCORE

Content that doesn't demonstrate real expertise doesn't rank. Google's EEAT — Experience, Expertise, Authoritativeness, Trustworthiness — is the invisible filter everything passes through now.

Generic content used to rank. It doesn't anymore. This prompt scores what you have and tells you exactly what to add to each page to pass the filter.

```
Open Chrome and browse my website — homepage + top 3 service pages.
Score each page across 5 dimensions (0-10 each):

EXPERIENCE (0-10)
  ∙ First-hand knowledge signals present?
  ∙ Specific project examples, case studies, real numbers?
  ∙ Before/after specifics? "We've completed X jobs in [city]"?

EXPERTISE (0-10)
  ∙ Team credentials visible?
  ∙ Technical depth appropriate to the service?
  ∙ Certifications, licenses, training mentioned?

AUTHORITY (0-10)
  ∙ Third-party mentions, press, awards?
  ∙ Review count + rating visible on page?
  ∙ Years in business prominent?

TRUST (0-10)
  ∙ Physical address visible?
  ∙ Phone number prominent above the fold?
  ∙ HTTPS, trust signals, payment logos?

CONTENT DEPTH (0-10)
  ∙ Word count appropriate? (service pages 600+ words)
  ∙ Answers real buyer questions?
  ∙ No thin filler content?
  ∙ Updated recently (within 12 months)?

Total score: X / 50 per page
Flag:
  ∙ Pages under 300 words
  ∙ Pages with no images
  ∙ Pages that read as keyword-stuffed
  ∙ Pages with outdated information
Output:
  ∙ Score table: Page | E | E | A | T | Depth | Total | Grade
  ∙ Priority fixes ranked by score gap
  ∙ Full rewrite brief for lowest-scoring page
  ∙ What to add to each page to reach 40+ / 50
```

---

### PROMPT 24 — HARD BLOCKERS CHECK

Nothing else matters until the bleeding stops.

This audit ignores optimization entirely. It finds only what is actively costing you customers right now — today — before any other audit makes sense to run.

Run this first if the user says anything like: "why am I not getting calls", "my listing disappeared", "the site is broken", "I had rankings and lost them overnight."

```
Open Chrome and go to my website + my GBP listing.
Check each category. FAIL = stop everything, fix this first.

PHONE + CONTACT
  ∙ Is my phone number clickable on mobile?
  ∙ Is my phone number identical on GBP, website, and all directories?
  ∙ Is my contact form working? (test it)
  ∙ Are my business hours accurate on GBP?

GBP STATUS
  ∙ Is the listing verified?
  ∙ Any suspension warnings?
  ∙ Any suggested edits from strangers overriding my info?
  ∙ Primary category: correct?
  ∙ Description: present or blank?
  ∙ At least 10 photos uploaded?

WEBSITE BASICS
  ∙ Does the site load on mobile?
  ∙ Any pages returning 404?
  ∙ Is the homepage redirecting somewhere unexpected?
  ∙ Is the SSL certificate valid?
  ∙ Is a call-to-action visible above the fold on mobile?

TRUST KILLERS
  ∙ Any placeholder text visible?
  ∙ Broken images on the homepage?
  ∙ Social links pointing to empty or inactive profiles?
  ∙ Copyright date showing an old year?
  ∙ Reviews with no responses for over 3 months?

Output — three sections only:
CRITICAL (fix today): numbered list, exact steps
IMPORTANT (fix this week): numbered list, exact steps
CLEAN (no issues found): list
No timelines. No optimization advice. Just fix it.
```

---

### PROMPT 25 — CONTENT REFRESH PLAN

Rankings decay. Content written 2-3 years ago loses ground to competitors who updated theirs last month. This is one of the most common causes of "I used to rank and now I don't."

The ROI on refreshing existing content is almost always higher than creating new content. You already have the page. You already have whatever authority it built. You just need to make it current and competitive again.

```
Open Chrome and browse my website — all main service pages
and any blog content visible.
Identify decay signals per page:
  ∙ Content age (when was it last updated?)
  ∙ Outdated information (old prices, discontinued services, old staff)
  ∙ Missing recent keywords (new location names, new service modifiers)
  ∙ Thinner than competitor pages now
  ∙ Schema missing or incomplete
  ∙ No internal links added since original publish
  ∙ Images old or missing alt text
Prioritize pages to refresh:
Tier 1: Pages that used to rank, probably don't now
Tier 2: Pages still ranking but losing position slowly
Tier 3: Blog posts that could funnel to service pages
For top 3 priority pages write:
  ∙ Refresh brief: what to add, remove, update
  ∙ New sections to add (headline + 3-bullet outline)
  ∙ New internal links (from where, anchor text)
  ∙ Schema to update or add
  ∙ Estimated word count increase needed
  ∙ One rewritten intro paragraph (signals freshness to Google)
Output: decay audit table + full refresh brief for top 3 + rewritten intros
```

---

### PROMPT 26 — PDF EXPORT

The full audit as a branded, client-ready PDF.

Use it for your own records. Share it with a business partner. Hand it to a VA with clear instructions. Or use it as an agency to deliver a professional proposal.

```
Requirements: Python 3 + reportlab installed
All audit files present in /seo-audit/
Ask first: "Who is this for?"
→ Personal use: functional formatting, no cover branding needed
→ Client or stakeholder: cover page, executive summary, branding
Build the PDF from audit files in /seo-audit/:
COVER PAGE
Business name + primary service + city
SEO Audit Report + date
Powered by Enola Revenue
SECTION 1 — EXECUTIVE SUMMARY
Business snapshot from BUSINESS_CONTEXT.md
Diagnosis summary from DIAGNOSIS.md
Top 3 quick wins
Overall health score
SECTION 2 — AUDIT RESULTS
One section per audit that was run
Clean formatting — no raw markdown visible
SECTION 3 — 12-WEEK PLAN
Full plan if 12-WEEK-PLAN.md exists
CLOSING PAGE
Next step: execute the plan above.
enolarevenue.com
Generate: /seo-audit/26-pdf-export/[BusinessName]_SEO_Audit.pdf
```

---

## HOW TO USE ALL 26 PROMPTS

Don't run everything at once. The order matters.

**Week 1:** Load business context. Run prompts 01 and 02. Fastest fixes with the most immediate map pack impact. You could see new searches appearing within days.

**Week 2:** Prompts 03, 04, 05. Review target set. 8 weeks of GBP content ready to go.

**Week 3:** Prompts 06, 07, 08. GBP fully optimized.

**Week 4:** Prompts 09, 21, 24. Keyword gaps found. Technical issues fixed. Hard blockers eliminated.

**Week 5-6:** Prompts 10, 11, 12, 13. Website and messaging aligned with GBP.

**Week 7-8:** Prompts 14, 15, 16. Authority building in the right direction.

**Week 9-10:** Prompts 17, 18, 19, 22. Long-term moat forming. Showing up in AI answers.

**Week 11-12:** Prompts 23, 25. Decaying content found and fixed.

**Ongoing:** Prompt 20. Measure what moved. Double down on what's working.

Run prompt 26 whenever you want a full PDF of everything.

90 days of consistent execution on this system and you will outrank businesses that have been established for years. The fundamentals compound. The shortcuts don't.

---

## THE FASTER WAY

Every prompt in this article is already built into a free Claude Code skill called ENOLA SEO.

Instead of copying prompts one by one — drop one folder into Claude Code, say "run my SEO audit", and Enola interviews you, browses your actual GBP and competitors, runs the audits you choose, and saves everything to organized files on your machine.

Persistent memory. Slash commands. PDF export. All 26 audits.

Free. MIT licensed. GitHub link in the first comment.

---

## THE REAL TALK

90% of people reading this will save it and never run a single prompt.

That's just how it goes.

The ones who run prompt 01 this week will be ranking for new searches before the month ends. The ones who complete all 26 over 90 days will be in a different position than their competitors entirely.

Not because the prompts are magic.

Because they executed while everyone else was saving articles.

---

*ENOLA SEO is part of Enola Revenue — an AI-powered business operating system.*
*enolarevenue.com*
