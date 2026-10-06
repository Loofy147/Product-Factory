from data_repair_receipt.repair import repair_rows


def test_repairs_trim_and_reports_exact_changes():
    rows = [
        {"email": " alice@example.com ", "name": " Alice "},
        {"email": "bob@example.com", "name": "Bob"},
    ]
    result = repair_rows(rows, fields=["email", "name"])
    assert result.rows[0]["email"] == "alice@example.com"
    assert result.rows[0]["name"] == "Alice"
    assert result.changed_cells == 2


def test_does_not_change_empty_or_non_string_values():
    rows = [{"email": "", "count": 3, "name": None}]
    result = repair_rows(rows, fields=["email", "count", "name"])
    assert result.rows == rows
    assert result.changed_cells == 0


def test_receipt_contains_before_after_digests():
    rows = [{"email": " Alice@example.com ", "name": "Alice"}]
    result = repair_rows(rows, fields=["email"])
    assert result.before_sha256
    assert result.after_sha256
    assert result.before_sha256 != result.after_sha256


def test_repair_is_non_destructive_to_input():
    rows = [{"name": " Alice "}]
    repair_rows(rows, fields=["name"])
    assert rows == [{"name": " Alice "}]
