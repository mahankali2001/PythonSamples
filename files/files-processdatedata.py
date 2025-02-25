# import sys
# sys.path.append('/path/to/ace_tools_directory')  # Add this line with the correct path
import pandas as pd
from dateutil import parser
# import ace_tools as tools

def clean_date(date_str):
    try:
        return parser.parse(date_str).strftime('%Y-%m-%d')  # Standardize format
    except ValueError:
        return "Invalid Date"  # Handle bad dates

def process_file(file_path):
    df = pd.read_csv(file_path)

    # Normalize dates
    df["date_of_birth"] = df["date_of_birth"].apply(clean_date)

    print(df)

    # Sort data by date_of_birth
    df = df.sort_values(by="date_of_birth", ascending=False)

    print(df)

    # Save cleaned file
    df.to_csv("../data/cleaned_data.csv", index=False)
    print("✅ Processed data saved to 'cleaned_data.csv'")

    return df

# 🔹 Example Usage
file_path = "../data/employee.csv"
cleaned_df = process_file(file_path)

# # Display the processed DataFrame
# tools.display_dataframe_to_user(name="Cleaned Data", dataframe=cleaned_df)
