# Open-Source Product Bases

These upstream projects are pinned as Git submodules under `products/open-source/`.

They are not represented as our original work.

For every downstream product:
- upstream source is pinned to an exact commit
- upstream license/attribution remains part of the source distribution
- our derivative layer lives under `products/derivatives/`
- our branding must remain distinct from upstream branding unless separate trademark permission exists

## Reproducible checkout

```bash
git clone --recurse-submodules https://github.com/Loofy147/Product-Factory.git
git submodule update --init --recursive
```

See `ACQUISITION_LEDGER.md` for provenance and licenses.
