# Data Repair Receipt — v0.2.0

**Status:** EXPERIMENTALLY_SUPPORTED (deterministic implementation only)

## Product

A controlled data-repair utility:

`Detect -> Propose -> Approve -> Repair -> Verify -> Receipt`

The product is intentionally not a "clean my data with AI" black box.

## Current deterministic core

Repair:
- trim surrounding whitespace in selected string fields

Receipt:
- changed-cell count
- before SHA-256
- after SHA-256
- repaired rows

Validation:
- 4/4 local unit tests passed
- input remains unmodified

## Strengthening plan

### 1. Repair recipe library
Initial safe recipes:
- whitespace
- case normalization
- date normalization
- phone normalization
- email normalization
- duplicate-key handling

Each recipe must have explicit preconditions.

### 2. Dry-run diff
Before mutation:
- show exact affected cells
- count changes
- show rejected/ambiguous cells

### 3. Approval boundary
No destructive change without explicit approval.

### 4. Rollback artifact
Store:
- before digest
- after digest
- changed-row identifiers
- recipe version
- reversible patch when feasible

### 5. Portable inputs
Prioritize:
- CSV
- XLSX
- JSON
- later API/database adapters

### 6. Product packaging

Potential:
- one-file repair
- batch credits
- recurring cleanup
- CLI
- API
- spreadsheet extension
- agency/data-ops service

## Moat hypothesis

The moat is the combination of:
- safe repair recipes
- explainability
- receipts
- rollback
- benchmark corpus of repair edge cases

## Kill test

If customers prefer one-shot AI cleaning despite requiring manual review, or the safe-repair constraints make the product too slow to justify payment, narrow or kill the pilot.
