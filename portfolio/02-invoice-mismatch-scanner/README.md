# Invoice Mismatch Scanner — v0.2.0

**Status:** EXPERIMENTALLY_SUPPORTED (deterministic implementation only)

## Product

A transaction-reconciliation utility for detecting inconsistencies across commercial records.

The long-term product is broader than "invoice vs order":

`Order -> Invoice -> Payment -> Refund -> Shipment -> Contract`

The first wedge remains deliberately small.

## Current deterministic core

Checks:
- missing invoice
- duplicate invoice identifier
- order ID mismatch
- amount mismatch
- currency mismatch

Current validation:
- 5/5 local unit tests passed

## Strengthening plan

### 1. Multi-record reconciliation
Add optional payment/refund/credit-note records.

### 2. Numeric tolerance rules
Handle:
- rounding
- tax
- discounts
- shipping
- currency conversion

Every tolerance must be explicit and versioned.

### 3. Exception classification
Separate:
- hard mismatch
- explainable adjustment
- duplicate
- missing record
- UNKNOWN

### 4. Evidence receipt
For every finding:
- source record identifiers
- compared fields
- expected/observed values
- rule version
- result digest

### 5. Batch economics
Support:
- CSV
- JSON
- API later

Output a compact exception queue rather than a generic dashboard.

## Distribution

Potential:
- direct utility
- Shopify/commerce ecosystem
- accounting/ERP integrations
- finance agencies
- B2B API
- batch processing service

Shopify's Operations category currently lists 496 apps and includes workflow automation, analytics and bulk-edit tooling; this is strong evidence of a real distribution ecosystem but also means our wedge must stay narrow. citeturn461623search2

## Moat hypothesis

- domain-specific reconciliation rules
- reusable exception taxonomy
- evidence receipts
- customer-specific tolerance history
- explainable deterministic output

## Kill test

Keep only if real datasets show a meaningful volume of costly mismatches and users prefer an exception-focused product over manually reconciling in spreadsheets/accounting software.
