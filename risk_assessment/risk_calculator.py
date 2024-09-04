PII_WEIGHTS = {
    'email': 1,
    'phone': 2,
    'ssn': 5,
    'PERSON': 3,
    'GPE': 2,
}

def calculate_risk(detected_pii):
    risk_score = 0
    for pii_type, pii_data in detected_pii.items():
        risk_score += len(pii_data) * PII_WEIGHTS.get(pii_type, 1)
    return risk_score
