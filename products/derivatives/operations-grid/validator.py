from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class RowError:
    row: int
    field: str
    reason: str

def validate(rows: Iterable[dict], required: tuple[str, ...], unique_key: str) -> list[RowError]:
    errors: list[RowError] = []
    seen: set[object] = set()
    for idx, row in enumerate(rows, start=2):
        for field in required:
            value = row.get(field)
            if value is None or (isinstance(value, str) and not value.strip()):
                errors.append(RowError(idx, field, "MISSING_REQUIRED"))
        key = row.get(unique_key)
        if key in seen and key not in (None, ""):
            errors.append(RowError(idx, unique_key, "DUPLICATE_KEY"))
        if key not in (None, ""):
            seen.add(key)
    return errors
