# Submission Preflight — v0.2.0

**Status:** EXPERIMENTALLY_SUPPORTED (deterministic implementation only)

## Product

A submission-readiness engine that answers:

> "Can I submit this package without an obvious evidence/format failure?"

It is not an RFP writer. The wedge is **final-mile verification**.

## Current deterministic core

Input:
- requirements JSON
- evidence directory

Checks:
- required file existence
- optional evidence -> UNKNOWN
- expected file type
- evidence path containment
- SHA-256 evidence manifest

Outputs:
- PASS / FAIL / UNKNOWN
- per-requirement findings
- evidence manifest

## Strengthening plan

### 1. Requirement rule packs
Represent reusable requirements for:
- tender
- procurement
- grant
- vendor onboarding
- compliance submission
- application packages

Each rule pack is versioned.

### 2. Evidence graph
Model:

`requirement -> expected evidence -> observed artifact -> checks -> finding`

This allows one document to satisfy several requirements while preserving provenance.

### 3. Expiry and temporal checks
Examples:
- certificate age
- license expiration
- insurance validity
- document issue window

### 4. Cross-document consistency
Detect conflicts in:
- legal name
- address
- registration number
- amounts
- dates
- signatory identity

### 5. Submission manifest
Generate:
- exact file list
- requirement coverage
- blocker list
- UNKNOWN list
- artifact digests
- rule-pack version

### 6. Signed/reportable output
Future report should be exportable as:
- human PDF/HTML
- machine JSON
- immutable evidence manifest

### 7. Multi-channel packaging

Potential:
- direct upload utility
- web app
- browser extension
- consultant/agency package
- API
- white-label
- marketplace integration

## Moat hypothesis

The defensibility is not the LLM.

Potential moat:
- versioned rule packs
- benchmark corpus
- evidence provenance
- deterministic verification layer
- reusable submission history
- domain-specific failure knowledge

## Current validation

- 5/5 local unit tests passed
- CLI smoke test passed
- CI failure found and corrected at dependency-install layer
- commercial value: OPEN
- real-world accuracy benchmark: OPEN

## Kill test

Use real submission packages.

Continue only if the engine materially reduces final-preflight effort while preserving conservative UNKNOWN handling and producing actionable findings.
