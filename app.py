from connectors.database_connector import connect_to_database, fetch_data_from_database
from connectors.cloud_storage_connector import connect_to_s3, fetch_data_from_s3
from connectors.filesystem_connector import fetch_data_from_filesystem

from pii_detection.regex_detection import detect_pii
from pii_detection.nlp_detection import detect_pii_nlp
from risk_assessment.risk_calculator import calculate_risk
from reports.report_generator import generate_json_report, generate_pdf_report

# Example: Fetching data from the database
db_uri = 'postgresql://user:password@localhost/dbname'
connection = connect_to_database(db_uri)
data = fetch_data_from_database(connection, 'SELECT * FROM users')

# Example: Fetching data from S3
bucket_name = 'example-bucket'
file_key = 'example-data.csv'
s3_client = connect_to_s3(bucket_name)
data = fetch_data_from_s3(s3_client, bucket_name, file_key)

# PII Detection
detected_pii = detect_pii(data)
detected_pii_nlp = detect_pii_nlp(data)

# Risk Calculation
risk_score = calculate_risk({**detected_pii, **detected_pii_nlp})

# Report Generation
generate_json_report(detected_pii, risk_score)
generate_pdf_report(detected_pii, risk_score)
