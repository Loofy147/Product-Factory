import argparse
import json
from pathlib import Path

from .engine import run_preflight


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preflight a submission evidence directory against requirements JSON."
    )
    parser.add_argument("requirements", type=Path, help="Path to requirements JSON")
    parser.add_argument("evidence", type=Path, help="Directory containing evidence files")
    parser.add_argument("--output", type=Path, help="Write JSON report to this path")
    args = parser.parse_args()

    requirements = json.loads(args.requirements.read_text(encoding="utf-8"))
    report = run_preflight(requirements, args.evidence)
    payload = {
        "summary": report.summary,
        "findings": [finding.__dict__ for finding in report.findings],
        "manifest": report.manifest,
    }
    rendered = json.dumps(payload, indent=2, sort_keys=True)

    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)

    return 0 if report.summary["FAIL"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
