# Data Repair Receipt — v0.1.0

**Status:** EXPERIMENTALLY_SUPPORTED (implementation only)

A deterministic repair utility that makes approved data changes and emits cryptographic before/after evidence.

Current repair:
- trim surrounding whitespace in explicitly selected string fields

Receipt:
- changed cell count
- before SHA-256
- after SHA-256
- repaired rows

Validation:
- local test suite: 4/4 passed

The input is not mutated in memory.

This is deliberately narrow. Future repair rules must each have their own tests and explicit approval semantics.

Commercial validation remains OPEN.
