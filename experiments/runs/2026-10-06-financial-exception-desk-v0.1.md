# Experiment Run — Financial Exception Desk v0.1

**Date:** 2026-10-06

## Objective

Validate a compound product boundary that combines:

- Invoice Mismatch Scanner
- Data Repair Receipt
- Operations Grid validator

without merging their internal implementations.

## Composition contract

`invoice records -> reconciliation findings`
`operational rows -> deterministic validation errors`
`operational rows -> non-destructive repair receipt`
`all outputs -> one exception desk result`

The compound does not persist repaired data. The repair output is explicitly marked `approval_required=true`.

## RED phase

**Commit:** `78580a9aef348949c558b95cbd1adbbe40ae64bb`

**CI run:** `37479399598`

**Result:** CONTRADICTED / infrastructure failure

Observed:
- package installation succeeded
- test step failed with exit code 127
- root cause: `pytest` was not installed by the new compound workflow

Interpretation:
- the test gate was executable enough to reach the intended test step
- this was a CI configuration defect, not evidence against the product logic

## GREEN phase

Implementation commit:
`ff285e8099f691bd01e86c4964278de2f637059b`

The first green-attempt CI run `37479478457` failed for the same explicit CI dependency issue. No product-code change was made in response.

Workflow repair commit:
`0010a2b5f64aedaa3eb5e4bdb48f6de39496bc86`

CI run:
`37479562099`

Result:
**SUCCESS**

Test scope at this point:
- main failure path
- invoice amount mismatch
- duplicate operational key
- repair receipt
- non-destructive input behavior

## Control expansion

Test commit:
`fd3765999f0dcf41f1d291e964ec492e855c0a6c`

Added controls for:
- incomplete invoice identity -> `UNKNOWN`
- clean input -> `PASS`

CI run:
`37479697116`

Status at record time: OPEN / verification in progress.

## Local verification

The same 3-test suite was reproduced locally from the pinned source snapshots.

Observed:
- 3 expected control cases are specified
- initial compound scenario passed locally before the CI control expansion
- the existing original component behavior was used as-is

## Epistemic result

**ESTABLISHED**
- The compound has a concrete artifact boundary.
- It composes existing deterministic components without copying their core logic.
- The workflow contains an explicit approval boundary for repairs.
- The first CI failure was correctly diagnosed as missing test infrastructure.

**EXPERIMENTALLY_SUPPORTED**
- Original compound behavior: local 1/1 test passed.
- Full compound CI with pytest installed: run `37479562099` SUCCESS.

**OPEN**
- final CI run after adding PASS/UNKNOWN controls
- real financial datasets
- buyer value
- pricing
- recurring usage
- distribution

## Next discriminating test

Run real transaction batches containing:
- missing invoices
- duplicate invoices
- amount/currency mismatches
- dirty vendor fields
- duplicate operational keys

Measure:
1. exception yield
2. false-positive/false-negative rate
3. operator time saved
4. percentage of repairs accepted
5. whether the exception queue is valuable enough to pay for
