import re

PII_PATTERNS = {
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'phone': r'\+?1?\d{9,15}',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b'
}

def detect_pii(data):
    detected_pii = {}
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, data)
        if matches:
            detected_pii[pii_type] = matches
    return detected_pii
