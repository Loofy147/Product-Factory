# Reliability Evidence Monitor

Downstream product layer over Gatus and Uptime Kuma.

## Deterministic wedge

Normalize service observations into:
- healthy
- degraded
- incident

Then emit an auditable receipt containing the observed state, previous state and reasons.

The layer deliberately does not replace the upstream monitoring engines.
