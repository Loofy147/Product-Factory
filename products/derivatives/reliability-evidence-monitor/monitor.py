from __future__ import annotations

from typing import Any


def assess(
    observation: dict[str, Any],
    *,
    latency_threshold_ms: int = 1000,
) -> dict[str, Any]:
    service = str(observation.get("service", ""))
    status = str(observation.get("status", "")).lower()
    previous_status = str(observation.get("previous_status", "")).lower()
    status_code = observation.get("status_code")
    latency_ms = observation.get("latency_ms")

    reasons: list[str] = []

    if isinstance(status_code, int) and status_code >= 500:
        reasons.append("HTTP_5XX")

    if previous_status and previous_status != status:
        reasons.append("STATUS_CHANGED")

    if status in {"down", "failed", "unreachable"}:
        reasons.append("SERVICE_DOWN")

    if (
        isinstance(latency_ms, (int, float))
        and latency_ms > latency_threshold_ms
        and status not in {"down", "failed", "unreachable"}
    ):
        reasons.append("LATENCY_THRESHOLD")

    if any(reason in reasons for reason in ("HTTP_5XX", "SERVICE_DOWN")):
        state = "incident"
        severity = "critical"
    elif reasons:
        state = "degraded"
        severity = "actionable"
    else:
        state = "healthy"
        severity = "low_noise"

    return {
        "service": service,
        "state": state,
        "severity": severity,
        "reasons": reasons,
        "receipt": {
            "service": service,
            "observed_status": status,
            "previous_status": previous_status or None,
            "status_code": status_code,
            "latency_ms": latency_ms,
        },
    }
