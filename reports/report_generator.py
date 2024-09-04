import json
import pdfkit

def generate_json_report(detected_pii, risk_score):
    report = {
        'detected_pii': detected_pii,
        'risk_score': risk_score
    }
    with open('report.json', 'w') as f:
        json.dump(report, f)

def generate_pdf_report(detected_pii, risk_score):
    html_report = f"""
    <h1>PII Detection Report</h1>
    <p>Risk Score: {risk_score}</p>
    <pre>{json.dumps(detected_pii, indent=2)}</pre>
    """
    pdfkit.from_string(html_report, 'report.pdf')
