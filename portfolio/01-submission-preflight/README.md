# Submission Preflight — v0.1.0

**Status:** EXPERIMENTALLY_SUPPORTED (implementation only)

A deterministic preflight engine for checking whether a submission evidence directory satisfies explicit requirements.

## Current scope

Input:
- requirements JSON
- evidence directory

Checks:
- required file exists
- optional evidence remains UNKNOWN when absent
- expected file type matches
- evidence path cannot escape the evidence directory
- evidence is hashed into a SHA-256 manifest

Outputs:
- PASS / FAIL / UNKNOWN summary
- per-requirement findings
- evidence manifest

Run:

```bash
PYTHONPATH=src python -m submission_preflight.cli requirements.json ./evidence --output report.json
```

Exit code:
- 0 = no blocking failures
- 2 = one or more blocking failures

## Validation

- 5/5 local tests passed
- CLI smoke test passed
- commercial value remains OPEN

## Deliberate boundary

v0.1 does not infer semantic compliance. It never converts uncertainty into PASS.

Next experimental layers:
1. deterministic metadata checks
2. dates / expiry
3. naming / size constraints
4. semantic evidence checks with explicit UNKNOWN handling
5. real document/PDF fixtures
