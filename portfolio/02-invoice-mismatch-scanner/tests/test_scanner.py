from invoice_mismatch_scanner.scanner import scan


def test_matching_order_and_invoice_pass():
    orders = [{"order_id": "O1", "invoice_id": "I1", "amount": 100, "currency": "USD"}]
    invoices = [{"invoice_id": "I1", "order_id": "O1", "amount": 100, "currency": "USD"}]
    report = scan(orders, invoices)
    assert report.summary == {"PASS": 1, "FAIL": 0}


def test_amount_mismatch_is_failure():
    orders = [{"order_id": "O2", "invoice_id": "I2", "amount": 100, "currency": "USD"}]
    invoices = [{"invoice_id": "I2", "order_id": "O2", "amount": 90, "currency": "USD"}]
    report = scan(orders, invoices)
    assert report.summary == {"PASS": 0, "FAIL": 1}
    assert report.findings[0].reasons == ["AMOUNT_MISMATCH"]


def test_missing_invoice_is_failure():
    orders = [{"order_id": "O3", "invoice_id": "I3", "amount": 50, "currency": "EUR"}]
    report = scan(orders, [])
    assert report.findings[0].reasons == ["INVOICE_MISSING"]


def test_duplicate_invoice_id_is_failure():
    orders = [{"order_id": "O4", "invoice_id": "I4", "amount": 50, "currency": "EUR"}]
    invoices = [
        {"invoice_id": "I4", "order_id": "O4", "amount": 50, "currency": "EUR"},
        {"invoice_id": "I4", "order_id": "O4", "amount": 50, "currency": "EUR"},
    ]
    report = scan(orders, invoices)
    assert report.findings[0].reasons == ["DUPLICATE_INVOICE_ID"]


def test_report_marks_multiple_mismatches():
    orders = [{"order_id": "O5", "invoice_id": "I5", "amount": 100, "currency": "USD"}]
    invoices = [{"invoice_id": "I5", "order_id": "O9", "amount": 90, "currency": "EUR"}]
    report = scan(orders, invoices)
    assert report.findings[0].reasons == [
        "ORDER_ID_MISMATCH",
        "AMOUNT_MISMATCH",
        "CURRENCY_MISMATCH",
    ]
