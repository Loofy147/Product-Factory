# Portfolio Status v0.5

**Date:** 2026-10-06

## Operating decision

We are building a multi-product, multi-channel catalog.

Source models:
- BUILD
- BUY / RESELL
- WHITE-LABEL / LICENSE
- BUNDLE / COMPOSE
- OPEN-SOURCE DOWNSTREAM

## Current portfolio

01 Submission Preflight — EXPERIMENTALLY_SUPPORTED implementation
02 Invoice Mismatch Scanner — EXPERIMENTALLY_SUPPORTED implementation
03 Data Repair Receipt — EXPERIMENTALLY_SUPPORTED implementation
04 Web Action Receipt — HYPOTHESIS
05 Agent Acceptance Test — RESEARCH PROTOTYPE CANDIDATE
06 Document Consistency Checker — HYPOTHESIS
07 Digital License Manager — HYPOTHESIS
08 Procurement Pack Builder — HYPOTHESIS
09 AI Output Validator — HYPOTHESIS
10 Marketplace Listing Preflight — HYPOTHESIS
11 Website Change Sentinel — HYPOTHESIS
12 Research Evidence Pack — HYPOTHESIS
13 SOP Drift Detector — HYPOTHESIS
14 Vendor Renewal Reconciler — HYPOTHESIS
15 Accessibility Preflight — HYPOTHESIS
21 Financial Exception Desk — EXPERIMENTALLY_SUPPORTED implementation / commercial value OPEN

## Open-source downstream products

16 Web Signal Intelligence
- upstream: context-dot-dev/webdog
- license: MIT
- pinned commit: 426158f543fbaf591f7248f1be62ebfa8b4d695c
- status: EXPERIMENTALLY_SUPPORTED overlay
- our wedge: change-significance classification

17 Evidence Canvas
- upstream: excalidraw/excalidraw
- license: MIT
- pinned commit: ed10ac7dca7e40f3f4a31269b4bfba980d0db41e
- status: HYPOTHESIS / productized template layer
- our wedge: evidence/decision canvas workflows

18 Private Knowledge Stream
- upstream: usememos/memos
- license: MIT
- pinned commit: f7a61867315ff7d3b2cd7347adfc161f32022227
- status: EXPERIMENTALLY_SUPPORTED overlay
- our wedge: structured decision/evidence timeline

19 Privacy Analytics Studio
- upstream: umami-software/umami
- license: MIT
- pinned commit: ec0ff50388c264ed8ce46f00967e92f7e71476ae
- status: HYPOTHESIS / productized report layer
- our wedge: packaged privacy-first reporting

20 Operations Grid
- upstream: gristlabs/grist-core
- license: Apache-2.0
- pinned commit: 3bc6578b06efe1e22c9cd3648f5311059e07739e
- status: EXPERIMENTALLY_SUPPORTED overlay
- our wedge: validated SMB operational templates

## Commercial-source pilots

### Travel eSIM Resale
Candidate supplier: Airalo Partners
Model: BUY / RESELL
Status: CANDIDATE — onboarding, rights and unit economics OPEN

### Service Business OS
Candidate platform: HighLevel
Model: WHITE-LABEL / LICENSE
Status: CANDIDATE — account economics, niche and acquisition OPEN

## Open-source compliance rule

Every downstream product must:
1. pin an upstream commit
2. preserve upstream license and attribution
3. mark our modifications
4. avoid upstream trademark/branding unless separately authorized
5. avoid implying endorsement
6. verify third-party dependency licenses before commercial distribution

## Execution rule

Do not return to broad market research as the default.

The next work:
1. strengthen the acquired products with product-specific overlays
2. add CI for downstream overlays
3. choose launch batches across different source models
4. test real distribution and payment
5. keep provenance and negative evidence


## Compound frontier

Added `products/COMPOUND_PRODUCT_CATALOG.md`.

The current execution frontier is not "add more products". It is to validate whether several existing products create materially stronger buyer outcomes when composed at explicit artifact/state boundaries.

Priority compounds:
- Bid Evidence Factory
- Web Change Intelligence
- Financial Exception Desk
- Research Decision Pack
- Agent Release Gate

No new shared platform is authorized merely to support these compounds.


## Portfolio expansion — 2026-10-06

21 Financial Exception Desk — EXPERIMENTALLY_SUPPORTED implementation / commercial value OPEN
22 Operations App Packs — HYPOTHESIS
23 Browser Action Gate — HYPOTHESIS
24 Reliability Evidence Monitor — EXPERIMENTALLY_SUPPORTED deterministic overlay / commercial value OPEN
25 ERP Verification Pack — HYPOTHESIS

Five additional OSS bases are pinned:
- Appsmith
- Agent Browser
- Gatus
- Uptime Kuma
- Lambda ERP

The next selection criterion is opportunity coverage: buyer, channel, source model and measurable outcome, not technical novelty alone.
