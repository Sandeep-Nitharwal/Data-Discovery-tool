import re

PII_PATTERNS = {
    'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    'phone': r'\+?1?\d{9,15}',
    'ssn': r'\b\d{3}-\d{2}-\d{4}\b'
}

PII_COLUMNS = {
    "name": r"(?i)(name|first_name|last_name|full_name|surname|middle_name)",
    "email": r"(?i)(email|e_mail|mail_address|email_address)",
    "phone": r"(?i)(phone|phone_number|mobile|mobile_number|contact_number|telephone)",
    "address": r"(?i)(address|addr|street|postal|zipcode|zip_code|city|state|country)",
    "date_of_birth": r"(?i)(dob|birth_date|date_of_birth|birthday|birth_day)",
    "identification": r"(?i)(id|ssn|passport|pan|aadhaar|national_id|social_security)",
    "username": r"(?i)(user_name|username|account|login|user_id|userid)",
    "gender": r"(?i)(gender|sex)",
    "password": r"(?i)(password|passcode|pwd)",
    "financial": r"(?i)(credit_card|cc_number|card_number|bank_account|account_number|iban|swift|ifsc|routing_number|account_balance)",
    "social_media": r"(?i)(social_media|twitter|facebook|linkedin|instagram|profile_url|profile_link|handle)",
    "ip_address": r"(?i)(ip_address|ipv4|ipv6|ip)",
    "geolocation": r"(?i)(location|geo|gps|latitude|longitude|lat|lng|long|altitude)",
    "health": r"(?i)(health|medical|insurance|diagnosis|treatment|patient|doctor|medication)",
    "employment": r"(?i)(employee|employer|job_title|job_role|occupation|workplace|company|salary|income|position)",
    "education": r"(?i)(education|degree|school|college|university|gpa|grade|course)",
    "family": r"(?i)(mother|father|parent|spouse|partner|marital_status|sibling|child|family_member|relationship)",
    "biometric": r"(?i)(biometric|fingerprint|retina|iris|face|facial_recognition|voice_print)",
    "nationality": r"(?i)(nationality|citizen|citizenship|residency|visa)",
    "tax": r"(?i)(tax|tin|vat|gst|taxpayer_id|tax_id)",
    "driver_license": r"(?i)(driver_license|driving_license|dl_number)",
    "vehicle": r"(?i)(vehicle|car|registration|license_plate|vin|vehicle_id)"
}

def detect_pii(data, schema):
    detected_pii = {}
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, data)
        if matches:
            detected_pii[pii_type] = matches
    
    detected_pii_columns = {}
    if schema:
        for pii_type, pattern in PII_COLUMNS.items():
            matches = re.findall(pattern, schema)
            if matches:
                detected_pii_columns[pii_type] = matches

    return detected_pii, detected_pii_columns

print(detect_pii("", "['email', 'Name', 'aadhaar_NO, 'phone_number', 'address']"))