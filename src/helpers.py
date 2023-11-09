import pandas as pd


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


# Function to find the table in the excel file
def find_table(df):
    df = df.dropna(how="all").dropna(how="all", axis=1)
    headers = df.iloc[0]
    new_df = pd.DataFrame(df.values[1:], columns=headers)

    return new_df
