from classifier import classify

def test_pricing_change_is_critical():
    s = classify("Pricing page changed", "Monthly price changed from 99 to 79")
    assert s.severity == "critical"
    assert "pricing" in s.reasons or "price" in s.reasons

def test_feature_change_is_actionable():
    s = classify("Product page changed", "New feature added")
    assert s.severity == "actionable"

def test_cookie_noise_is_low_noise():
    s = classify("Homepage changed", "Cookie timestamp updated")
    assert s.severity == "low_noise"
