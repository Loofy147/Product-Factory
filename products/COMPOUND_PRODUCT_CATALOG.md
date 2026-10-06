# Compound Product Catalog v0.1

**Date:** 2026-10-06

## Purpose

Product Factory is allowed to combine several existing products when the combination creates a tighter buyer workflow rather than a larger generic platform.

A compound product is:

`input -> component A -> component B -> evidence/state -> buyer outcome`

It is not a requirement to merge repositories or create shared infrastructure.

## Epistemic rule

All commercial-value statements below are **INFERENCE** until validated with real users, real inputs, or payment.

Technical composition claims are **ESTABLISHED** when they refer only to components already present in Product Factory.

No compound product is promoted to **EXPERIMENTALLY_SUPPORTED** until its actual end-to-end path has been executed and observed.

## Composition tests

A proposed compound must satisfy at least 5 of 7 checks:

1. Same buyer or tightly adjacent buyer.
2. Shared input or directly chained output.
3. Clear state transition between components.
4. One combined outcome is materially more useful than separate tools.
5. At least one reusable distribution surface.
6. Components can remain independently replaceable.
7. A narrow kill test can falsify the compound without killing unrelated products.

Reject compounds that mainly create:
- generic dashboards
- all-in-one platforms
- duplicated AI features
- unnecessary accounts/RBAC/integrations
- shared code before reuse is proven

## Ranked compound candidates

| Rank | Compound | Components | Buyer | Combined outcome | Architecture score | Status |
|---|---|---|---|---|---:|---|
| 1 | Bid Evidence Factory | Submission Preflight + Procurement Pack Builder + Document Consistency Checker + Evidence Canvas | bid/procurement teams | compile and verify a submission package with visible evidence coverage and contradictions | 12/14 | INFERENCE |
| 2 | Web Change Intelligence | Web Signal Intelligence + Website Change Sentinel + Research Evidence Pack + Private Knowledge Stream | operators, agencies, researchers | detect meaningful web changes, preserve evidence, and turn them into decisions | 12/14 | INFERENCE |
| 3 | Financial Exception Desk | Invoice Mismatch Scanner + Data Repair Receipt + Operations Grid + Vendor Renewal Reconciler | SMB finance/procurement ops | detect exceptions, safely repair data, preserve proof, and surface renewal risk | 11/14 | INFERENCE |
| 4 | Research Decision Pack | Research Evidence Pack + Evidence Canvas + Private Knowledge Stream + Web Signal Intelligence | analysts/consultants/engineering teams | move from captured evidence to structured decision with traceable provenance | 11/14 | INFERENCE |
| 5 | Agent Release Gate | Agent Acceptance Test + AI Output Validator + Web Action Receipt + Private Knowledge Stream | agent builders/operators | gate an agent run on state-based acceptance and retain an execution record | 11/14 | INFERENCE |
| 6 | Website Release Guard | Accessibility Preflight + Website Change Sentinel + Web Action Receipt | agencies/web teams | detect release changes, verify accessibility, and retain proof of the performed action | 10/14 | INFERENCE |
| 7 | Marketplace Launch Guard | Marketplace Listing Preflight + Web Signal Intelligence + Accessibility Preflight | sellers/agencies | validate listings before launch and detect consequential changes after launch | 10/14 | INFERENCE |
| 8 | Vendor Renewal Control | Vendor Renewal Reconciler + Invoice Mismatch Scanner + Web Signal Intelligence | finance/procurement | reconcile expected commercial terms with observed invoices and external changes | 10/14 | INFERENCE |
| 9 | Digital Product Control | Digital License Manager + Operations Grid + Privacy Analytics Studio | digital-product owners/agencies | issue entitlements, operate catalog data, and inspect aggregate product usage | 9/14 | INFERENCE |
| 10 | Submission Evidence Stream | Submission Preflight + Evidence Canvas + Private Knowledge Stream | bid/compliance teams | keep a living evidence/decision record around a submission | 9/14 | INFERENCE |

## Why these are different products

### 1. Bid Evidence Factory

Input:
- requirement set
- source documents
- reusable rule pack

Flow:
`requirements -> pack assembly -> consistency checks -> preflight -> evidence map -> final package`

Candidate SKU:
- per submission
- consultant bundle
- API/white-label later

Hard kill test:
A real package must contain enough omissions/conflicts that the buyer saves meaningful final-review effort.

### 2. Web Change Intelligence

Input:
- monitored URLs/domains

Flow:
`observe -> diff -> classify -> preserve evidence -> decision stream`

Candidate SKU:
- monitored source bundle
- agency multi-client plan
- API

Hard kill test:
A meaningful share of detected changes must be actionable rather than noise, and users must retain or act on the alerts.

### 3. Financial Exception Desk

Input:
- invoices
- orders/transactions
- vendor data
- operational rows

Flow:
`reconcile -> exception queue -> repair proposal -> approval -> receipt -> renewal risk`

Candidate SKU:
- batch credits
- agency service
- direct B2B

Hard kill test:
Real datasets must show recurring costly exceptions and customers must prefer the exception workflow over manual spreadsheet reconciliation.

### 4. Research Decision Pack

Input:
- web evidence
- notes
- claims
- diagrams

Flow:
`capture -> classify -> map evidence -> contradiction -> decision -> durable stream`

Candidate SKU:
- research pack
- team workspace
- consultant template bundle

Hard kill test:
A user must be able to reuse the generated evidence/decision package in a subsequent decision without redoing the collection.

### 5. Agent Release Gate

Input:
- agent run
- expected states
- produced outputs
- action receipts

Flow:
`run -> output validation -> state acceptance -> action verification -> decision/evidence record`

Candidate SKU:
- developer CLI
- CI gate
- API

Hard kill test:
Inject known bad outputs or invalid states and prove the gate rejects them without relying on subjective LLM approval.

## Architectural boundary

Compound products should compose at the **artifact/state boundary** whenever possible:

`A output -> normalized contract -> B input`

Do not initially compose by importing internal implementation details across product directories.

Preferred:
- JSON artifacts
- receipts
- manifests
- versioned rule packs
- deterministic result objects

Avoid:
- shared mutable databases
- hidden global state
- product-specific imports across unrelated products
- one giant application

## Launch batches

### Batch C1 — evidence/compliance

Primary:
- Bid Evidence Factory
- Website Release Guard

Reason:
- strong adjacency among existing verification/evidence assets
- narrow buyer outcome
- direct upload/agency/API distribution options

### Batch C2 — web intelligence

Primary:
- Web Change Intelligence
- Marketplace Launch Guard

Reason:
- same observation substrate
- multiple buyer segments
- SaaS/API/agency distribution

### Batch C3 — commercial operations

Primary:
- Financial Exception Desk
- Vendor Renewal Control

Reason:
- transaction, vendor, and spreadsheet workflows naturally meet
- measurable exception counts
- potential recurring usage

### Batch C4 — AI/developer

Primary:
- Agent Release Gate

Reason:
- concentrated technical wedge
- API/CLI/CI distribution
- existing verification philosophy fits without requiring a general agent platform

## Current frontier

**ESTABLISHED**
- Product Factory has independent build products and downstream open-source overlays.
- The existing products expose several reusable artifacts: findings, receipts, manifests, structured timelines, validated rows, and change classifications.

**INFERENCE**
- The highest-leverage next step is compound validation, not adding many more standalone products.
- The four launch batches above have stronger internal coherence than the full 20-product catalog treated independently.

**OPEN**
- willingness to pay
- acquisition cost
- retention
- support burden
- channel eligibility
- legal/contractual distribution rights for each commercial-source component
- end-to-end technical composability for each compound

## Decision rule

Do not create a new shared platform for the compounds.

Implement the smallest end-to-end path for one compound, execute it on real inputs, record evidence, and only then extract reusable contracts or libraries.


## New compound opportunities — 2026-10-06

| Rank | Compound | Components | Buyer | Why the combination matters | Status |
|---|---|---|---|---|---|
| 11 | SMB Finance Control Room | Financial Exception Desk + Operations App Packs + Privacy Analytics Studio | SMB finance/ops | exception queue + operator UI + aggregate reporting | INFERENCE |
| 12 | Agent Execution Assurance | Browser Action Gate + Agent Acceptance Test + AI Output Validator + Web Action Receipt | agent builders | links action execution to postcondition acceptance and proof | INFERENCE |
| 13 | Service & Change Intelligence | Reliability Evidence Monitor + Web Change Intelligence + Private Knowledge Stream | agencies / SaaS operators | joins service health, external changes and durable operational context | INFERENCE |
| 14 | ERP Migration Assurance | ERP Verification Pack + Financial Exception Desk + Data Repair Receipt | ERP implementers | validates imported commercial data and preserves repair proof | INFERENCE |
| 15 | Operational Decision Workspace | Operations App Packs + Evidence Canvas + Private Knowledge Stream | SMB teams / consultants | turns operational records into evidence-backed decisions | INFERENCE |

### Portfolio-composition rule

A new compound should reuse at least two independent product outputs before any shared platform code is introduced.

The compound itself is a SKU hypothesis, not permission to merge the underlying products.
