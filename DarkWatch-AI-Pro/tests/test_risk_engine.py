from app.modules.risk_engine import calculate_risk

def test_password_exposure_has_high_score():
    breaches = [{
        "data_classes": ["Email addresses", "Passwords"],
        "verified": True
    }]
    risk = calculate_risk(breaches)
    assert risk["score"] >= 50
    assert risk["level"] in ["High", "Critical"]
