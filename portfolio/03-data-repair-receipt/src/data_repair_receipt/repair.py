from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any


@dataclass(frozen=True)
class RepairResult:
    rows: list[dict[str, Any]]
    changed_cells: int
    before_sha256: str
    after_sha256: str


def _digest(rows: list[dict[str, Any]]) -> str:
    payload = json.dumps(
        rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return sha256(payload).hexdigest()


def repair_rows(rows: list[dict[str, Any]], fields: list[str]) -> RepairResult:
    before = [dict(row) for row in rows]
    after = [dict(row) for row in rows]
    changed = 0

    for row in after:
        for field in fields:
            value = row.get(field)
            if isinstance(value, str) and value:
                cleaned = value.strip()
                if cleaned != value:
                    row[field] = cleaned
                    changed += 1

    return RepairResult(
        rows=after,
        changed_cells=changed,
        before_sha256=_digest(before),
        after_sha256=_digest(after),
    )
