import functions_framework

import pandas as pd

from google.cloud import storage
from helpers import clean_column_name, find_table
from io import BytesIO


@functions_framework.http
def convert_excel_to_csv(request):
    print("Starting Excel to CSV conversion...")

    # Get parameters from the request
    request_json = request.get_json()

    if (
        request_json
        and "source_excel_bucket" in request_json
        and "source_excel_file" in request_json
        and "target_csv_bucket" in request_json
        and "target_csv_file" in request_json
        and "job_source" in request_json
    ):
        source_excel_bucket = request_json["source_excel_bucket"]
        source_excel_file = request_json["source_excel_file"]
        source_sheet_name = request_json.get("source_sheet_name", 0)
        target_csv_bucket = request_json["target_csv_bucket"]
        target_csv_file = request_json["target_csv_file"]
        job_source = request_json["job_source"]
        job_time = request_json.get("job_time", pd.Timestamp.now(tz="America/Toronto"))
    else:
        return "Invalid request. Required parameters are missing.", 400

    print(request_json)

    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()

    # Download the Excel file from GCS
    bucket = storage_client.bucket(source_excel_bucket)
    blob = bucket.blob(source_excel_file)
    blob_result = blob.download_as_bytes()

    print("Downloaded Excel file from GCS.")

    # Convert the Excel file to CSV
    df = pd.read_excel(BytesIO(blob_result), sheet_name=source_sheet_name)
    new_df = find_table(df)

    # updating column names and converting to a dictionary
    new_df.columns = [clean_column_name(col) for col in new_df.columns]

    # Add metadata columns
    new_df["job_source"] = job_source
    new_df["input_excel"] = f"gs://{source_excel_bucket}/{source_excel_file}"
    new_df["output_csv"] = f"gs://{target_csv_bucket}/{target_csv_file}"
    new_df["job_time"] = job_time

    # Convert the DataFrame to a CSV string
    csv_data = new_df.to_csv(index=False)

    # Upload the CSV to GCS
    bucket = storage_client.bucket(target_csv_bucket)
    csv_blob = bucket.blob(target_csv_file)
    csv_blob.upload_from_string(csv_data, content_type="text/csv")

    return (
        f"Excel file '{source_excel_file}' converted to CSV and saved as '{target_csv_file}' in GCS bucket '{target_csv_bucket}'.",
        200,
    )
