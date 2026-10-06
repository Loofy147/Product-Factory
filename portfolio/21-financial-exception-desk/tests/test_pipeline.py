from financial_exception_desk.pipeline import build_exception_desk


def test_compound_pipeline_reconciles_validates_and_repairs_with_receipt():
    orders = [
        {"order_id": "O1", "invoice_id": "I1", "amount": 100, "currency": "EUR"},
    ]
    invoices = [
        {"invoice_id": "I1", "order_id": "O1", "amount": 90, "currency": "EUR"},
    ]
    rows = [
        {"id": "A", "vendor": "  Acme  "},
        {"id": "A", "vendor": "Beta"},
    ]

    result = build_exception_desk(
        orders=orders,
        invoices=invoices,
        rows=rows,
        repair_fields=["vendor"],
        required_fields=("id", "vendor"),
        unique_key="id",
    )

    assert result["status"] == "FAIL"
    assert result["summary"] == {
        "invoice_failures": 1,
        "row_validation_errors": 1,
        "changed_cells": 1,
    }
    assert result["invoice_findings"][0]["reasons"] == ["AMOUNT_MISMATCH"]
    assert result["row_errors"] == [
        {"row": 3, "field": "id", "reason": "DUPLICATE_KEY"},
    ]
    assert result["repair_receipt"]["changed_cells"] == 1
    assert result["repair_receipt"]["before_sha256"] != result["repair_receipt"]["after_sha256"]
    assert rows[0]["vendor"] == "  Acme  "
