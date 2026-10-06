# Browser Action Gate

**Source:** OPEN-SOURCE DOWNSTREAM (Agent Browser + existing Web Action Receipt)  
**Status:** HYPOTHESIS  
**Buyer:** agent builders, automation teams, QA operators

## Wedge

Turn browser automation from "the click happened" into:

`planned action -> browser execution -> observed state -> receipt -> acceptance`

The product should reject ambiguous success states.

## Initial distribution

- CLI
- developer API
- CI gate
- agent tool package

## Kill test

Inject known failure states (wrong page, blocked click, stale selector, missing postcondition) and require deterministic rejection.
