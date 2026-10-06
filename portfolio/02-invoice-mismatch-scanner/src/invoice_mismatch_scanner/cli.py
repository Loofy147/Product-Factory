import argparse
import csv
import json
from decimal import Decimal
from pathlib import Path

from .scanner import scan


def _load(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if "amount" in row:
            row["amount"] = Decimal(row["amount"])
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare order records with invoice records.")
    parser.add_argument("orders", type=Path)
    parser.add_argument("invoices", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = scan(_load(args.orders), _load(args.invoices))
    payload = {
        "summary": report.summary,
        "findings": [
            {"order_id": f.order_id, "invoice_id": f.invoice_id, "reasons": f.reasons}
            for f in report.findings
        ],
    }
    rendered = json.dumps(payload, indent=2, default=str)
    if args.output:
        args.output.write_text(rendered + "
", encoding="utf-8")
    else:
        print(rendered)
    return 0 if report.summary["FAIL"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
