# Function to clean and format column names
def clean_column_name(col_name):
    # Make all lowercase
    col_name = col_name.lower()

    # Remove special characters and replace spaces with underscores
    col_name = "".join(e for e in col_name if e.isalnum() or e.isspace()).replace(
        " ", "_"
    )

    # Remove extra spaces
    col_name = "_".join(col_name.split())

    return col_name
