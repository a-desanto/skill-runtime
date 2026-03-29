def collect_admin_mfa_evidence():
    # Placeholder logic – replace with real API queries later
    evidence = [
        {"user": "admin1", "mfa_enabled": True},
        {"user": "admin2", "mfa_enabled": False}
    ]

    compliant = all(u["mfa_enabled"] for u in evidence)
    confidence = 0.9 if compliant else 0.7

    return {
        "evidence": evidence,
        "compliant": compliant,
        "confidence": confidence
    }
