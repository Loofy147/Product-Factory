from reliability_evidence_monitor.monitor import assess


def test_down_service_is_critical_and_emits_receipt():
    result = assess(
        {
            "service": "checkout",
            "status": "down",
            "status_code": 503,
            "latency_ms": 1800,
            "previous_status": "up",
        }
    )

    assert result["severity"] == "critical"
    assert result["state"] == "incident"
    assert result["reasons"] == ["HTTP_5XX", "STATUS_CHANGED", "SERVICE_DOWN"]
    assert result["receipt"]["service"] == "checkout"
    assert result["receipt"]["observed_status"] == "down"
    assert result["receipt"]["previous_status"] == "up"


def test_high_latency_without_failure_is_degraded():
    result = assess(
        {
            "service": "api",
            "status": "up",
            "status_code": 200,
            "latency_ms": 1500,
            "previous_status": "up",
        },
        latency_threshold_ms=1000,
    )

    assert result["severity"] == "actionable"
    assert result["state"] == "degraded"
    assert result["reasons"] == ["LATENCY_THRESHOLD"]


def test_healthy_service_is_low_noise_with_stable_state():
    result = assess(
        {
            "service": "api",
            "status": "up",
            "status_code": 200,
            "latency_ms": 120,
            "previous_status": "up",
        }
    )

    assert result["severity"] == "low_noise"
    assert result["state"] == "healthy"
    assert result["reasons"] == []
