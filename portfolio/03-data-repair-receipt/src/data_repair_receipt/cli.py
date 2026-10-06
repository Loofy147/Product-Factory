import argparse
import json
from pathlib import Path

from .repair import repair_rows


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Repair safe whitespace defects and emit a before/after receipt."
    )
    parser.add_argument("input", type=Path, help="JSON file containing an array of row objects")
    parser.add_argument("--fields", required=True, help="Comma-separated fields to normalize")
    parser.add_argument("--output", type=Path, required=True, help="Output JSON path")
    args = parser.parse_args()

    rows = json.loads(args.input.read_text(encoding="utf-8"))
    result = repair_rows(
        rows, [field.strip() for field in args.fields.split(",") if field.strip()]
    )
    payload = {
        "changed_cells": result.changed_cells,
        "before_sha256": result.before_sha256,
        "after_sha256": result.after_sha256,
        "rows": result.rows,
    }
    args.output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "
", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
