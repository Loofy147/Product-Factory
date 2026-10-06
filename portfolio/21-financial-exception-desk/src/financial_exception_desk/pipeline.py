from __future__ import annotations

from typing import Any

from data_repair_receipt.repair import repair_rows
from invoice_mismatch_scanner.scanner import scan
from validator import validate as validate_rows


def _required_invoice_fields_present(
    orders: list[dict[str, Any]], invoices: list[dict[str, Any]]
) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []

    for index, order in enumerate(orders, start=1):
        for field in ("order_id", "invoice_id"):
            if field not in order:
                errors.append(
                    {
                        "source": "orders",
                        "row": str(index),
                        "field": field,
                        "reason": "MISSING_REQUIRED_INPUT",
                    }
                )

    for index, invoice in enumerate(invoices, start=1):
        if "invoice_id" not in invoice:
            errors.append(
                {
                    "source": "invoices",
                    "row": str(index),
                    "field": "invoice_id",
                    "reason": "MISSING_REQUIRED_INPUT",
                }
            )

    return errors


def build_exception_desk(
    *,
    orders: list[dict[str, Any]],
    invoices: list[dict[str, Any]],
    rows: list[dict[str, Any]],
    repair_fields: list[str],
    required_fields: tuple[str, ...],
    unique_key: str,
) -> dict[str, Any]:
    input_errors = _required_invoice_fields_present(orders, invoices)

    repair = repair_rows(rows, repair_fields)
    row_errors = validate_rows(rows, required_fields, unique_key)

    if input_errors:
        return {
            "schema_version": "0.1",
            "status": "UNKNOWN",
            "input_errors": input_errors,
            "invoice_findings": [],
            "row_errors": [
                {"row": e.row, "field": e.field, "reason": e.reason}
                for e in row_errors
            ],
            "repair_receipt": {
                "approval_required": True,
                "changed_cells": repair.changed_cells,
                "before_sha256": repair.before_sha256,
                "after_sha256": repair.after_sha256,
                "rows": repair.rows,
            },
            "summary": {
                "invoice_failures": 0,
                "row_validation_errors": len(row_errors),
                "changed_cells": repair.changed_cells,
            },
        }

    invoice_report = scan(orders, invoices)
    invoice_findings = [
        {
            "order_id": finding.order_id,
            "invoice_id": finding.invoice_id,
            "reasons": finding.reasons,
        }
        for finding in invoice_report.findings
        if finding.reasons
    ]

    row_error_payload = [
        {"row": error.row, "field": error.field, "reason": error.reason}
        for error in row_errors
    ]

    status = "FAIL" if invoice_findings or row_error_payload else "PASS"

    return {
        "schema_version": "0.1",
        "status": status,
        "input_errors": [],
        "invoice_findings": invoice_findings,
        "row_errors": row_error_payload,
        "repair_receipt": {
            "approval_required": True,
            "changed_cells": repair.changed_cells,
            "before_sha256": repair.before_sha256,
            "after_sha256": repair.after_sha256,
            "rows": repair.rows,
        },
        "summary": {
            "invoice_failures": len(invoice_findings),
            "row_validation_errors": len(row_error_payload),
            "changed_cells": repair.changed_cells,
        },
    }
