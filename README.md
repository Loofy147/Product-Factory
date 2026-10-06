# Product Factory

Operating workspace for a portfolio of small, sellable digital products.

**Status:** v0.1 working charter — 2026-10-06

## Mission

Build multiple small products, expose them to real demand and distribution, measure real behavior/payment, then kill weak products and scale winners.

We are not optimizing for discovering one perfect idea before building. We are optimizing for a repeatable product-discovery and product-production loop.

## Current portfolio

1. Submission Preflight
2. Invoice Mismatch Scanner
3. Data Repair Receipt
4. Web Action Receipt
5. Agent Acceptance Test
6. Document Consistency Checker
7. Digital License Manager
8. Procurement Pack Builder
9. AI Output Validator

These are **hypotheses**, not commitments.

## Core loop

Market signals → hypothesis → smallest sellable pilot → distribution → usage/payment evidence → kill / iterate / double-down.

## Workspace

- `charter/` — operating rules, decisions, experiment protocol
- `portfolio/` — product-specific working material
- `research/` — market and customer evidence
- `experiments/` — experiment records and run outputs
- `benchmarks/` — datasets, baselines, evaluation results
- `shared-tools/` — reusable utilities only after reuse is proven
- `.github/` — CI and repository automation

## Independence rule

Products remain logically independent. Shared code, schemas, or infrastructure are extracted only after repeated reuse has been demonstrated.

The Product Factory repository is a control plane, not a forced monorepo for all products.
