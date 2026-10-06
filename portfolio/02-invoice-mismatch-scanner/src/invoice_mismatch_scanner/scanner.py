from dataclasses import dataclass


@dataclass(frozen=True)
class Finding:
    order_id: str
    invoice_id: str | None
    reasons: list[str]


@dataclass(frozen=True)
class Report:
    findings: list[Finding]

    @property
    def summary(self) -> dict[str, int]:
        return {
            "PASS": sum(not f.reasons for f in self.findings),
            "FAIL": sum(bool(f.reasons) for f in self.findings),
        }


def scan(orders: list[dict], invoices: list[dict]) -> Report:
    by_invoice: dict[str, list[dict]] = {}
    for invoice in invoices:
        by_invoice.setdefault(str(invoice["invoice_id"]), []).append(invoice)

    findings: list[Finding] = []
    for order in orders:
        order_id = str(order["order_id"])
        invoice_id = str(order["invoice_id"])
        matches = by_invoice.get(invoice_id, [])
        if not matches:
            findings.append(Finding(order_id, invoice_id, ["INVOICE_MISSING"]))
            continue
        if len(matches) > 1:
            findings.append(Finding(order_id, invoice_id, ["DUPLICATE_INVOICE_ID"]))
            continue

        invoice = matches[0]
        reasons: list[str] = []
        if invoice.get("order_id") != order_id:
            reasons.append("ORDER_ID_MISMATCH")
        if invoice.get("amount") != order.get("amount"):
            reasons.append("AMOUNT_MISMATCH")
        if invoice.get("currency") != order.get("currency"):
            reasons.append("CURRENCY_MISMATCH")
        findings.append(Finding(order_id, invoice_id, reasons))

    return Report(findings)
