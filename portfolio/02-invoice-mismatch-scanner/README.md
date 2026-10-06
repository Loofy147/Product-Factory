# Invoice Mismatch Scanner — v0.1.0

Deterministically compares order records with invoice records and produces actionable mismatch reasons.

Current checks:
- missing invoice
- duplicate invoice identifier
- order ID mismatch
- amount mismatch
- currency mismatch

The product deliberately reports explicit failure reasons rather than using an LLM to guess whether two financial records are equivalent.

Validation:
- local test suite: 5/5 passed
