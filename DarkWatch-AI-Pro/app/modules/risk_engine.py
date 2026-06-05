def calculate_risk(breaches):
    score = 0
    reasons = []

    for breach in breaches:
        classes = [c.lower() for c in breach.get("data_classes", [])]
        if "passwords" in classes:
            score += 35
            reasons.append("Password exposure detected")
        if "email addresses" in classes:
            score += 15
            reasons.append("Email address exposed")
        if "ip addresses" in classes:
            score += 10
            reasons.append("IP address exposure detected")
        if breach.get("verified"):
            score += 10

    score = min(score, 100)

    if score >= 75:
        level = "Critical"
        action = "Reset passwords immediately, enable MFA, review login activity, and monitor identity misuse."
    elif score >= 45:
        level = "High"
        action = "Change affected passwords, enable MFA, and watch for phishing attempts."
    elif score >= 20:
        level = "Medium"
        action = "Use unique passwords and monitor suspicious emails."
    else:
        level = "Low"
        action = "No major exposure detected in the current data source."

    return {
        "score": score,
        "level": level,
        "reasons": sorted(set(reasons)),
        "recommendation": action
    }
