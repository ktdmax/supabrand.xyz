# Intentionally synthetic assumptions

SYNTHETIC TEST DATA. Everything below was invented for this fixture or decided during modelling.

## Invented facts (not in the original SUPABRAND fixture)
- Sites (Vienna-Simmering and Brno assembly, Munich/Lyon/Utrecht service hubs, seven sales offices), headcount 1,240 FTE, organisation chart, company timeline.
- All product specifications (battery capacities, weights, cargo volume, N6 power, F4-B2 pack data) and the VELA A9 pre-release.
- Core-market price lists 2026 and 2027.
- Market profiles, channel mixes, dealer counts, dealer programme terms and the Austrian addendum.
- Personas, the owner survey, the dealer observation, the Lyon scooter pilot and its interim finding, the Kraków pilot discussion, the German trade fair dates, the website relaunch, the SECOND MILE DE target of 110 workshops, the PICO social campaign.
- Competitor notes. Riese & Müller, Cube, Gazelle, Urban Arrow, Ca Go, Segway-Ninebot and Xiaomi appear only as reference names; every statement about them is synthetic planning context, and "Voltbay Systems" is fictional.
- Legal positions (French material clause rationale, EU warranty wording guidance, road-use review, UK take-back panel) are fixture positions, not legal advice or findings.
- The ORBITAL MESH grant review of 2026-10-15 "took place, outcome pending".

## Modelling decisions
- Claims are `nature: knowledge` records of `kind: claim` with the §17.1 value shape; they carry no value contract because the Foundation fact contract schema used here (`brand-identity.schema.json`) requires a `name` property. Facts that do carry contracts always include `name`.
- Rules-family records use `rule.schema.json` 3.0.0 with `term_prohibited` checks; they are the only deterministic rules in the world.
- Half-open validity: a claim "valid until 2026-12-31" is written `to: 2027-01-01T00:00:00Z`.
- Scope dimension vocabulary: ISO market codes, BCP-47 locales, lowercase product families (`city`, `allroad`, `cargo`, `glide`, `node`), channels (`web`, `ecommerce`, `social`, `instagram`, `tiktok`, `linkedin`, `youtube`, `paid-digital`, `press`, `print`, `trade-show`, `sales`, `packaging`, `presentation`, `service`), audiences (`consumer`, `fleet-operator`, `facilities-manager`, `procurement`, `dealer`, `press`, `municipal-planner`, `installation-partner`), outputTypes (`brochure`, `product-page`, `case-study`, `service-carton`, `press-release`, `social-video`, `sales-presentation`). `brands` and `contentPurposes` are unused.
- Requests declare every scope dimension the relevant records use, because the resolver does not infer missing dimensions.
- The German consumer address record is scoped to `audiences: [consumer]` so that it never overlaps the German-language B2B record (precedence is authority-blind; an overlap produced an ambiguous subject winner in the first run).
- Draft Task Profiles are resolved only when a request sets `draftOk: true`; this is a fixture convention, not OBDS semantics.
- `taskProfileHash` is computed as `sha256_id` of the profile document by `tools/build.py`; the reference resolver does not compute it.
- Locale count: the fixture names 13 locales; `it-CH` is treated as served by the Italian desk without separate copy.
- `sourceRefs` with prefix `supabrand:` point to the existing fixture sources; `synthetic:` prefixes name invented internal documents that do not exist as files.

## Deliberate edge situations
- Superseded signature (`brand.signature.master.2024`, expired) next to the current one.
- Market override with a dependency: `claim.c06-c2-frame-recycled.fr` depends on `legal.fr-material-clause`.
- Evidence-dependent draft: `claim.c18-a8-vibration-draft` (unverified, `governance.status: draft`) references `evidence.e18-a8-vibration-comparator` (`state: unknown`).
- Future-valid records: `market.pricing-2027`, `product.vela-a9`.
- Informational local observation that differs from the binding record: `communication.local-observation.ch-signature`.
- Unresolved conflict: `legal.de-f4-carton-type-size` (6 pt vs 7 pt).
- Local programme override: `sales.dealer-programme.at`.
- Market-specific claims that go out of scope elsewhere: C11 (US), C12 (DE), C16 (AT/DE), C08 (seven PICO markets).
