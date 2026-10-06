# ERP Verification Pack

**Source:** OPEN-SOURCE DOWNSTREAM (Lambda ERP + existing financial utilities)  
**Status:** HYPOTHESIS  
**Buyer:** SMB finance teams, ERP implementation partners, accounting operators

## Wedge

Do not compete as another ERP.

Package a verification layer around:
- invoice/import checks
- transaction reconciliation
- safe data repair
- evidence receipts

## Composition

`ERP records -> reconciliation -> repair proposal -> receipt -> exception queue`

The ERP remains the system of record; the verification layer is independently replaceable.

## Kill test

Real migration/import batches must surface costly exceptions that the existing ERP workflow does not make obvious.
