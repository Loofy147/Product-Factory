from dataclasses import dataclass

@dataclass(frozen=True)
class Signal:
    severity: str
    reasons: tuple[str, ...]

HIGH = ("price", "pricing", "terms", "privacy", "security", "status", "outage", "deadline")
MEDIUM = ("feature", "availability", "product", "policy", "release", "version")

def classify(title: str, diff: str) -> Signal:
    text = f"{title} {diff}".lower()
    high = tuple(sorted({k for k in HIGH if k in text}))
    medium = tuple(sorted({k for k in MEDIUM if k in text}))
    if high:
        return Signal("critical", high)
    if medium:
        return Signal("actionable", medium)
    return Signal("low_noise", ())
