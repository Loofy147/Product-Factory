# Product Catalog v0.3

## Portfolio design

We are building **many products × many channels × multiple source models**.

Source models:
- BUILD
- BUY / RESELL
- WHITE-LABEL / LICENSE
- BUNDLE / COMPOSE
- OPEN-SOURCE DOWNSTREAM

The objective is portfolio-level revenue, learning rate, margin, distribution resilience and option value.

## Catalog

| # | Product | Domain | Source | Primary buyer | Best initial channel | Strongest wedge |
|---|---|---|---|---|---|---|
| 01 | Submission Preflight | Procurement / Documents | BUILD | Bid teams | Direct B2B | final-mile submission verification |
| 02 | Invoice Mismatch Scanner | Finance / Commerce | BUILD / BUNDLE | SMB finance ops | Direct / agencies | explainable transaction exceptions |
| 03 | Data Repair Receipt | Data / Ops | BUILD | Analysts / ops | Direct utility | safe repair + cryptographic receipt |
| 04 | Web Action Receipt | Browser / Ops | BUILD / BUNDLE | SMB teams | Extension | proof that a web action completed |
| 05 | Agent Acceptance Test | AI / Developer | BUILD | Agent builders | API / developer | state-based acceptance tests |
| 06 | Document Consistency Checker | Documents | BUILD | Teams / agencies | Upload utility | cross-document contradiction detection |
| 07 | Digital License Manager | Digital commerce | BUILD / WHITE-LABEL | Product owners | API / direct | issue + validate entitlements |
| 08 | Procurement Pack Builder | Procurement | BUILD / BUNDLE | Suppliers / contractors | Direct B2B | requirement-to-pack compilation |
| 09 | AI Output Validator | AI / Operations | BUILD / BUNDLE | AI users | API / extension | validate output before downstream use |
| 10 | Marketplace Listing Preflight | E-commerce | BUILD / BUNDLE | Sellers | Marketplace ecosystem | pre-publish listing correctness |
| 11 | Website Change Sentinel | Web / Intelligence | BUILD | Agencies / operators | Direct SaaS | meaningful change detection |
| 12 | Research Evidence Pack | Research / Consulting | BUILD / BUNDLE | Analysts / consultants | Browser + direct | provenance and reusable evidence |
| 13 | SOP Drift Detector | Operations / Knowledge | BUILD / BUNDLE | Process teams | Browser + B2B | detect procedure drift |
| 14 | Vendor Renewal Reconciler | Finance / Procurement | BUILD / BUNDLE | SMB finance / procurement | Direct B2B | expected-vs-observed commercial exceptions |
| 15 | Accessibility Preflight | Web / Quality | BUILD / BUNDLE | Agencies / web teams | Extension / CI | pre-release gating with evidence |
| 16 | Web Signal Intelligence | Web / Monitoring | OPEN-SOURCE DOWNSTREAM | Operators / agencies | SaaS / API | classify meaningful change vs noise |
| 17 | Evidence Canvas | Research / Decisions | OPEN-SOURCE DOWNSTREAM | Teams / consultants | Direct / marketplace | opinionated evidence/decision diagrams |
| 18 | Private Knowledge Stream | Research / Knowledge | OPEN-SOURCE DOWNSTREAM | Researchers / engineering teams | Direct / extension | structured decision/evidence timeline |
| 19 | Privacy Analytics Studio | Analytics | OPEN-SOURCE DOWNSTREAM | Agencies / SMBs | Direct / self-hosted | packaged privacy-first reporting |
| 20 | Operations Grid | Operations / Data | OPEN-SOURCE DOWNSTREAM | SMB ops teams | Direct / templates | validated operational spreadsheet workflows |

## Open-source downstream bases

Pinned, reproducible upstream bases are recorded in:
`products/open-source/ACQUISITION_LEDGER.md`

Upstream code is not represented as original authorship by Product Factory.
Our product layer is the packaging, workflows, templates, rules, adapters and other modifications we add.

## Portfolio balancing

### Transactional utilities
03, 06, 10, 11

### SMB operations
02, 13, 14, 20

### B2B / procurement
01, 08, 15

### Developer / AI infrastructure
05, 07, 09

### Research / knowledge
12, 17, 18

### Privacy / analytics
19

### Browser-native distribution
04, 10, 11, 12, 13, 15

## Selection rules

A product moves forward when it has:
- clear buyer
- concrete painful event
- measurable output
- at least one credible distribution channel
- viable unit economics
- manageable support
- lawful/contractually valid source model
- a reason not to be immediately replaced by a generic AI feature

A product is not promoted merely because it is technically interesting.

## Strength multiplier

For each promising product, improve one or more of:
- deterministic correctness
- evidence/provenance
- workflow compression
- domain-specific rule packs
- reusable integrations
- distribution access
- lower support burden
- superior unit economics
- proprietary benchmark/data


## Compound product layer

The portfolio now permits **compound products**: narrow workflows that chain independent products through explicit artifacts/state contracts.

See `products/COMPOUND_PRODUCT_CATALOG.md`.

Current priority compounds:
1. Bid Evidence Factory
2. Web Change Intelligence
3. Financial Exception Desk
4. Research Decision Pack
5. Agent Release Gate

Compound status remains **INFERENCE** until end-to-end execution on real inputs is observed.
