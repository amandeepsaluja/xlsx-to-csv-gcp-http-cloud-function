# Excel to CSV Cloud Function

This is a simple cloud function that converts an Excel file to CSV and stores it in a Google Cloud Storage bucket. It is written in Python 3.11.

## Parameters in the request body

| Parameter           | Description                                                 | Required |
| ------------------- | ----------------------------------------------------------- | :------: |
| source_excel_bucket | GCS Bucket where Excel file is located                      |    ✅    |
| source_excel_file   | Path to Excel file in the bucket                            |    ✅    |
| source_sheet_name   | Sheet Name in the Excel (defaults to first)                 |    ❌    |
| target_csv_bucket   | GCS Bucket where CSV file be written for further processing |    ✅    |
| target_csv_file     | Path to CSV file in the bucket                              |    ✅    |
| job_source          | Source of the job                                           |    ✅    |
| job_time            | Job timestamp (defaults to current EST time)                |    ❌    |
