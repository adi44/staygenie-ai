# StayGenie — Product Requirements Document (PRD)

Last updated: 26 May 2026

## Purpose

StayGenie helps travelers find the right hotel quickly by using natural-language inputs and recommendations tailored to preferences, budget, and context. This PRD defines the MVP, success metrics, scope, user journeys, and a high-level technical approach.

## Problem statement

Users spend a lot of time comparing hotels across websites and filters. Existing experiences require manual searching, opening many tabs, and translating vague travel needs into rigid filters. This is time-consuming and often leads to suboptimal bookings.

## Target users

- Business travelers
- Tourists
- Families
- Digital nomads

## Goals

- Reduce time-to-recommendation for relevant hotels
- Improve booking confidence with concise, comparable recommendations
- Provide an intuitive natural-language interface so users don't need to master multiple search filters

## MVP features

### Must have

- Natural-language search: accept free-form trip descriptions and extract intent (destination, dates, party size, budget, special needs)
- Fast performance: return recommendations within a few seconds for typical queries
- Hotel recommendations: rank and surface top N (default 3) choices with reasons and key attributes (price, rating, distance, amenities)
- Booking simulations: simulate booking flows (rates, availability) for recommendations; provide links to booking pages

### Nice to have (post-MVP)

- Voice interface
- Travel itinerary generation (integrate hotel with calendars and trip plans)
- Review summarization and sentiment highlights

### Not included in MVP

- Payments
- Flights
- Visa assistance

## User stories

1. As a traveler, I can describe my trip to the bot in natural language so I don't need to manually search through multiple hotel websites.
2. As a user, I want the system to return the top 3 hotel recommendations tailored to my requirements so I can choose quickly.
3. As a user, I want concise reasons for each recommendation (e.g., "Great location near business district, free breakfast") so I can compare effectively.
4. As a user, I want an example booking simulation showing price and dates so I can verify availability before navigating to a booking partner.

## Acceptance criteria

Input example:

```
Need a hotel in Delhi
for 2 adults
3 nights
under INR 15000
```

Expected behavior:

- System parses destination (Delhi), dates/length (3 nights), guests (2 adults), budget (<= INR 15000)
- System returns the top 3 recommendations with the following for each:
  - Hotel name
  - Price estimate (total and per-night)
  - Rating and number of reviews
  - Key attributes (amenities, proximity to requested location)
  - Short explanation (1–2 lines) why it's recommended
  - Link to simulated booking or partner booking page

Non-functional acceptance:

- Response time: typical queries return within 2–5 seconds
- Relevance: at least 70% of sampled queries have a top-3 recommendation judged relevant in small user tests (initial target)

## Success metrics

- Time-to-first-recommendation (target: <5s)
- Conversion proxy: % of users who click through from a recommendation to a booking partner
- User satisfaction (NPS / qualitative feedback from early testers)
- Precision@3 in manual relevance labeling (target: >70% initially)

## Scope and constraints

- Data sources: public hotel APIs, partner APIs, cached price data, and review aggregators
- Privacy: do not store unnecessary PII; any saved preferences must be opt-in
- Cost: prioritize approaches that minimize API cost for MVP (caching, rate-limiting)

## Timeline (high level)

- Week 0–2: Intent extraction and prototype search pipeline (NLP + hotel data source integration)
- Week 3–4: Ranking, recommendation UI and booking simulation
- Week 5: Internal testing, small closed beta
- Week 6+: Iterate based on feedback and add nice-to-have features

## Technical approach (high level)

- Input processing: lightweight NLP pipeline that extracts entities (destination, dates, guests, budget, preferences)
- Enrichment: map destination to locations, retrieve hotel candidates from data sources, enrich with price and review data
- Ranking: simple rule-based + ML scoring for MVP (price match, rating, distance, amenities)
- Response: return top N recommendations with structured metadata and human-friendly explanations

## Risks & mitigations

- Data quality / availability: mitigate with caching and fallback partners
- Incorrect NLP extraction: provide a compact clarifying UI to edit parsed fields before final recommendation
- Cost of API usage: limit calls, cache results, and batch enrichments

## Open questions

- Which booking/data partners to prioritize for MVP (e.g., Booking.com, Expedia, Priceline)?
- Should we persist user preferences across sessions in MVP or keep everything session-based?

## Appendix: Example conversation

User: "I'm traveling to Delhi next month, 2 adults, 3 nights, budget under INR 15000 — prefer walking distance to Connaught Place."

System:

- "Top 3 hotels for Delhi, 3 nights, 2 adults, <= INR 15000"
  1. Hotel A — INR 12,800 total — 4.2★ (1,200 reviews)
      - Close to Connaught Place (0.4 km), free breakfast. Recommended because it matches budget and location.
      - [Simulate booking]
  2. Hotel B — INR 13,500 total — 4.0★ (900 reviews)
      - Good business amenities, near metro. [Simulate booking]
  3. Hotel C — INR 11,900 total — 4.1★ (600 reviews)
      - Lower price, fewer reviews, close to restaurants. [Simulate booking]

---

