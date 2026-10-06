# Run — Submission Preflight v0.1.0

**Date:** 2026-10-06  
**Run status:** PASS  
**Evidence class:** EXPERIMENTALLY_SUPPORTED

## Environment

- Python 3.13.5
- pytest 9.0.2

## Tests

5/5 passed.

Covered behaviors:
1. required present evidence -> PASS
2. required missing evidence -> FAIL
3. wrong file type -> FAIL
4. optional missing evidence -> UNKNOWN
5. evidence path traversal attempt -> rejected

## CLI smoke test

Input:
- requirements JSON with 2 required files and 1 optional file
- evidence directory containing both required files

Observed:
- PASS: 2
- FAIL: 0
- UNKNOWN: 1
- SHA-256 manifest generated for both observed files
- CLI returned exit code 0

## Important boundary

This run proves the deterministic v0.1 implementation, not customer value.

Commercial validation remains OPEN.

## Next discriminating test

Use real submission/tender evidence packages and measure:
- known defect detection
- false positives
- unknown preservation
- time reduction
- willingness to pay
