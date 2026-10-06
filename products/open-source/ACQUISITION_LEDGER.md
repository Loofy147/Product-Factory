# Open-Source Acquisition Ledger v0.1

We use permissively licensed open-source products as downstream bases.

## Compliance policy

For every downstream product:
- pin an exact upstream commit
- retain upstream license and attribution in the downstream source distribution
- keep an upstream provenance record
- mark our modifications
- do not reuse upstream trademarks/branding unless separately permitted
- do not imply upstream endorsement
- review third-party dependency licenses before commercial distribution

## Acquired bases

| Base | Upstream | License | Pinned commit | Our product layer |
|---|---|---|---|---|
| Webdog | context-dot-dev/webdog | MIT | 426158f543fbaf591f7248f1be62ebfa8b4d695c | Web Signal Intelligence |
| Excalidraw | excalidraw/excalidraw | MIT | ed10ac7dca7e40f3f4a31269b4bfba980d0db41e | Evidence Canvas |
| Memos | usememos/memos | MIT | f7a61867315ff7d3b2cd7347adfc161f32022227 | Private Knowledge Stream |
| Umami | umami-software/umami | MIT | ec0ff50388c264ed8ce46f00967e92f7e71476ae | Privacy Analytics Studio |
| Grist Community | gristlabs/grist-core | Apache-2.0 | 3bc6578b06efe1e22c9cd3648f5311059e07739e | Operations Grid |

These are downstream products, not claims of original authorship of upstream code.


## Newly acquired bases — 2026-10-06

| Base | Upstream | License | Pinned commit | Planned product layer | Source verification |
|---|---|---|---|---|---|
| Appsmith | appsmithorg/appsmith | Apache-2.0 | f8385f49bc09169ed7fe84ac81fb3b709ee36ada | Operations App Packs | GitHub LICENSE/README |
| Agent Browser | vercel-labs/agent-browser | Apache-2.0 | 6d3e22c673a44271d0c213c2fef722e0aeba627d | Browser Action Gate | GitHub LICENSE/README |
| Gatus | TwiN/gatus | Apache-2.0 | 1cf79275cd7bd761f19ca731bd5cd24cdec37797 | Reliability Evidence Monitor | GitHub LICENSE/README |
| Uptime Kuma | louislam/uptime-kuma | MIT | 2a4d7635a9146bd26abbeeef41e6fd833c615e92 | Customer Status Monitor | GitHub LICENSE/README |
| Lambda ERP | lambdadevelopment/lambda-erp | Apache-2.0 | 979fc7fb6ee89edfdd1d4248b80c138c0d150243 | ERP Verification Pack | GitHub LICENSE/README |

### Acquisition notes

- Appsmith: low-code internal tools/admin panels; Apache-2.0.
- Agent Browser: browser automation CLI for agents; Apache-2.0.
- Gatus: health monitoring and alerting; Apache-2.0.
- Uptime Kuma: self-hosted monitoring/status pages; MIT.
- Lambda ERP: AI-native ERP with invoice/inventory/accounting workflows; Apache-2.0.

Pin records are reproducibility anchors only. Commercial distribution still requires review of third-party dependency licenses, trademarks, notices, and the exact contents of the pinned tree.
