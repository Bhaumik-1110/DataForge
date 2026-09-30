import pandas as pd

# Path to the raw dataset
file_path = "Data/Raw/Amazon Sale Report.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Display basic information
print("DATAFORGE - RAW DATA INSPECTION")
print("=" * 50)

print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())