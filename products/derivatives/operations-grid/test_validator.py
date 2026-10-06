from validator import validate

def test_detects_missing_required_and_duplicate_key():
    rows = [
        {"id": "A", "name": ""},
        {"id": "A", "name": "Alice"},
    ]
    errors = validate(rows, ("id", "name"), "id")
    assert [(e.row, e.field, e.reason) for e in errors] == [
        (2, "name", "MISSING_REQUIRED"),
        (3, "id", "DUPLICATE_KEY"),
    ]
