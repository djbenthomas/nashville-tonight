# Nashville Tonight — the downtown directory

Concept from Benny, 2026-11-19. **This is the main task.** Everything else is secondary.

The pitch in one line: **a QR code on a flyer downtown that tells you where to go tonight — by music,
by night, by the kind of crowd you want to be in.**

---

## Why it works

There is no real directory. Google Maps gives you a list of bars; it doesn't tell you that Robert's is
traditional country and the place three doors down is a party bar with a cover band. Tourists and
locals both solve this by asking somebody. This becomes the somebody.

Benny is downtown enough, knows enough people, and can get flyers into hands — that's the distribution
nobody else has.

## What the user does (30 seconds, on a phone)

1. Scans the QR on a flyer (or a table card, or a sticker in a window)
2. Picks **tonight** (or any night of the week)
3. Picks **what they want to hear** — real country, rock, bluegrass, americana
4. Picks **the kind of night** — sit and listen, dance, or full party
5. Gets a short list of rooms, in walking distance, with what tonight actually is

Optional but powerful: **"no bachelorette chaos"** as a filter. That's the mature-crowd promise and
nobody else is offering it.

## The flyer

Front: "You're already downtown. Here's where to actually go." + QR + three examples.
Back: the week at a glance, and a line for sponsors.

**Tracking:** each flyer batch gets its own short code (`?f=rd1`, `?f=broadway2`). That tells us which
locations and which distributors actually produce scans — which is what we sell to sponsors later.

**Distribution:** Benny's people. What they get for handing them out:
- their show featured that week in the directory
- their name/venue on the flyer's "brought to you by" line
- first shot at paid featured slots when sponsorships start

That's the trade: distribution in exchange for promotion, not cash.

## Money (in order of realism)

1. **Featured slot** — a venue or act pays to be pinned at the top for their night. $50–$150/week.
2. **Flyer sponsorship** — a whiskey brand, a boot company, a ride-share, a hotel. One logo on the
   back of a print run. Priced per 1,000 flyers.
3. **Artist promotion** — acts pay a small monthly fee to keep their shows listed and featured.
4. **Data/insight** — after a few months, "what people actually search for on a Thursday" is a
   sellable story to venues and brands. Don't promise this early; just collect the data.

Nobody pays until there's traffic. The first job is proof of scans.

## Update loop (the hard part — this is why directories die)

- **Weekly:** Monday morning, refresh the week's lineups from venue calendars (30–45 min)
- **Daily (5 min):** check that tonight's listings are still right
- **Every listing shows a "last verified" date.** Honesty beats freshness theater.
- **A "report an error" link on every card** — free QA from the crowd

If the data goes stale, the product is dead. This is the whole job.

## MVP — what gets built first

- One mobile-first page, no login, no app
- 20–30 venues, hand-curated, with genre + vibe + best nights + cover + hours
- Filters: night / music / vibe / walkable-from-Broadway
- Every card: what it is, why it's on the list, what to order, when the real crowd shows up
- QR + printable flyer
- Analytics: which filters get used, which listings get tapped (this is the sponsorship evidence)

**Not in the MVP:** user accounts, reviews, ticket sales, artist self-serve, real-time lineups.

## Naming

Working name: **Nashville Tonight**
Alternates: *Real Nashville Tonight*, *The Downtown Card*, *Where To Go Nashville*

Domain later (nashvilletonight.com or similar). Start on GitHub Pages, swap when it earns it.

## Risks

- **Stale data** kills trust faster than no data. The weekly loop is non-negotiable.
- **Venue politics**: listing someone as "party bar" or "tourist trap" can burn a relationship.
  Keep the tone factual, never insulting. Describe the room, let people decide.
- **Accuracy on schedules** — never publish a lineup we haven't seen on the venue's own calendar.
- **Scope creep** — the second it becomes a ticketing platform, it stops shipping.

## Relationship to the other work

- **Keeping Nashville Country** (Instagram) is the audience engine for this. Same voice, same taste.
- **AS·U·LIKE·IT** gets a permanent footer credit — every flyer, every page. That's a lot of local
  exposure for the DJ business without a single ad.
- The real-country list already built is the seed data for the "real country" category.

## Status

- [x] Concept + plan (this doc)
- [x] MVP page with filters and curated venue data
- [x] Printable flyer with QR
- [ ] Published to GitHub Pages
- [ ] First 100 flyers distributed
- [ ] Weekly update loop running
