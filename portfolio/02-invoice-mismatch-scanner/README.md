# Invoice Mismatch Scanner — v0.1.0

**Status:** EXPERIMENTALLY_SUPPORTED (implementation only)

Deterministically compares order records with invoice records and produces actionable mismatch reasons.

Current checks:
- missing invoice
- duplicate invoice identifier
- order ID mismatch
- amount mismatch
- currency mismatch

Validation:
- local test suite: 5/5 passed

Commercial validation remains OPEN.

The product deliberately reports explicit failure reasons rather than using an LLM to guess whether two financial records are equivalent.
