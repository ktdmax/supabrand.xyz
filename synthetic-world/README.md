# SUPABRAND synthetic knowledge world (OBDS 4.2.0)

> **SYNTHETIC TEST DATA.** Everything in this folder describes a fictional company,
> SUPABRAND Mobility SE, and its fictional brands, products, markets, partners, claims
> and projects. Real city, country, currency, channel and competitor names appear only as
> entity references. No statement about a real company, market share, legal finding or
> competitor behaviour in this folder is a real-world fact. Nothing here is confidential
> data of any real organisation.

## What this is

A coherent OBDS 4.2.0 Knowledge Records cassette built on the existing SUPABRAND fixture in
the public corpus in the repository root (`../sources/`, S01–S25). It keeps every identity of that fixture (company,
subbrands VELA / PICO / FIELD / DOCKGRID, the six products, signatures, claims C01–C18,
evidence E01–E18, partner grants, campaigns, people) and extends it with company, market,
audience, competitor, sales, legal, project, research and communication knowledge, plus
Task Profiles. It is a development and test dataset for a downstream brand-knowledge
resolver (SUPACORE). It contains no benchmark questions, retrieval rules, answer templates or
expected answers.

## The fictional world in one page

- **Company.** SUPABRAND Mobility SE, Vienna, founded 2016, privately held, around 1,240 FTE
  (fictional), 2025 group net revenue EUR 120.0 million (fixture dossier E03). Assembly in
  Vienna and Brno, service hubs in Munich, Lyon and Utrecht, sales offices in seven cities.
- **Brand.** Purpose "room to move" (Spielraum), master signature "Make room for moving."
  (since 2025-09-01, replaced "Move beyond."), locale signatures for de-DE, de-CH, fr, it-IT,
  endorsed subbrands with their own signatures.
- **Products (range release 26.3, from 2026-07-01).** City C1 DAILY and City C2 (12 markets),
  VELA A8 (12 markets), FIELD F4 cargo (10 markets, fleet enquiry only), PICO G1 scooter
  (7 markets), DOCKGRID N6 charging node (7 markets, business enquiry only). VELA A9 is a
  future-valid pre-release record (from 2027-03-01).
- **Markets.** AT, DE, CH, FR, IT, ES, NL, PL, CZ, GB, US, KR with market profiles, a core-market
  price list (2026, and a future-valid 2027 list), locale and address rules, and a Korean
  consumer display name override for VELA A8.
- **Claims.** C01–C18 as §17.1 claim records with evidence references: global, market-specific
  (C11 US only, C12 DE, C16 AT/DE), product-specific, evidence-dependent, expired (C13, C15),
  a French consumer override of C06 that requires a legal clause, and an unverified draft
  (C18) whose evidence record has `state: unknown`. Three `rules`-family prohibitions.
- **Partners.** ORBITAL MESH (grant 2024-04-01 to 2026-12-31, B2B and corporate channels only,
  review outcome pending) and VIAFORMA (grant expired 2025-06-30).
- **Projects.** Campaign AC-26 (running), spring campaign 2025 (historical), N6 pilot AT/DE
  2025, German trade fair 2026, website relaunch 2026, SECOND MILE network DE 2026, PICO social
  campaign, Professional Systems sales enablement, Lyon scooter pilot, Kraków municipal pilot
  discussion (endorsement pending), VELA A9 launch 2027 (embargoed).
- **Open items.** German F4 service-carton type size (6 pt vs 7 pt), UK battery take-back panel,
  ORBITAL MESH commuter portrait image rights, Supa Grotesk font licence, ORBITAL MESH grant
  review outcome. All are `state: unknown` records with caveats.

## Layout

| Path | Content |
|---|---|
| `records/00-world.yaml` | Manifest header and `knowledgeVocabulary` (13 domains, 7 aliases). |
| `records/01-brand.yaml` … `13-communication.yaml` | Knowledge Records grouped by domain, one `elements:` list per file. |
| `task-profiles/*.yaml` | Nine Task Profile documents (`kind: obds-task-profile`, `schemaVersion: "4.2.0"`): six approved, two draft, one superseded. |
| `requests/*.yaml` | Fourteen request contexts used to exercise the resolver (profile, single-valued scope, optional `asOf`, `expectBlocked`, `draftOk`). |
| `tools/build.py` | Assembles and seals `manifest.yaml`, validates it with the OBDS reference implementation, validates and resolves the Task Profiles, writes `validation-result.json` and `inventory.md`. |
| `tools/negative_check.py` | Mutates the built manifest in memory and proves that the validators reject the mutations. |
| `manifest.yaml` | Generated, sealed OBDS manifest (profiles `obds-foundation` + `obds-knowledge-records`). Do not edit by hand. |
| `inventory.md` | Generated inventory: records by domain, authority, market, family, state; validity; precedence groups; dependencies; caveats; Task Profiles with hashes; resolution runs. |
| `validation-result.json` | Generated validation and resolution output. |
| `ASSUMPTIONS.md` | Intentionally synthetic assumptions and design decisions. |

## How the records use OBDS 4.2.0

- Every record is an ordinary Brand Element with `domain`, `authority`, optional `dependsOn`,
  `relatedTo`, `caveats`. Facts (`nature: fact`, `state: defined`) and `rules`-family elements
  carry generated value contracts (`brand-identity.schema.json` 1.0.0 for facts,
  `rule.schema.json` 3.0.0 for rules). Knowledge notes use `nature: knowledge` without a contract.
- Market, locale, audience and product overrides share a `subject` with the global record and
  win by narrower scope (§10.2). Overlapping scopes are kept nested or disjoint because
  precedence is authority-blind and content-blind.
- Validity is half-open (`validity.to` is the first instant the record no longer applies).
- Unverified records always carry caveats; `state: unknown` records carry caveats and no value.
- Approved Task Profiles carry `governance.approval.approvedContentHash` =
  `sha256_id(profile without governance.approval)`. `taskProfileHash` in the inventory is
  `sha256_id` of the whole profile document, the value a consumer would bind together with
  `id` and `version`.

## Validate

Clone the OBDS repository (tag `v4.2.0`) and install its reference dependencies, then:

```sh
cd synthetic-world
python3 tools/build.py --obds-repo /path/to/obds --seal
python3 tools/negative_check.py --obds-repo /path/to/obds
```

Expected: `elements=142 contracts=16 profiles=9 requests=14 ok=True` and `negative check PASS`.
The snapshot instant is 2026-10-21T12:00:00Z (`AS_OF` in `tools/build.py`); requests may set
their own `asOf`.

## Not in scope

No SUPACORE code, no changes to OBDS, no benchmark questions, no retrieval or answer logic.
