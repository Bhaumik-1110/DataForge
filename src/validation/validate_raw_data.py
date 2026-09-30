import pandas as pd

# --------------------------------------------------
# DATAFORGE - RAW DATA VALIDATION
# --------------------------------------------------

file_path = "Data/Raw/Amazon Sale Report.csv"

# Load raw data
df = pd.read_csv(file_path, low_memory=False)

print("=" * 60)
print("DATAFORGE - DATA QUALITY REPORT")
print("=" * 60)

# --------------------------------------------------
# 1. BASIC DATASET CHECK
# --------------------------------------------------

print(f"\nRows checked: {len(df)}")
print(f"Columns found: {len(df.columns)}")


# --------------------------------------------------
# 2. REQUIRED COLUMN CHECK
# --------------------------------------------------

required_columns = [
    "Order ID",
    "Date",
    "Status",
    "Fulfilment",
    "Sales Channel ",
    "ship-service-level",
    "Style",
    "SKU",
    "Category",
    "Size",
    "ASIN",
    "Courier Status",
    "Qty",
    "currency",
    "Amount",
    "ship-city",
    "ship-state",
    "ship-postal-code",
    "ship-country",
    "promotion-ids",
    "B2B",
    "fulfilled-by"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if not missing_columns:
    print("\n[PASS] Required columns are present")
else:
    print("\n[FAIL] Missing required columns:")
    for column in missing_columns:
        print(f"  - {column}")


# --------------------------------------------------
# 3. UNEXPECTED COLUMN CHECK
# --------------------------------------------------

unexpected_columns = [
    column for column in df.columns
    if column not in required_columns
]

if not unexpected_columns:
    print("\n[PASS] No unexpected columns found")
else:
    print("\n[WARNING] Unexpected columns found:")
    for column in unexpected_columns:
        print(f"  - {column}")


# --------------------------------------------------
# 4. DUPLICATE ROW CHECK
# --------------------------------------------------

duplicate_count = df.duplicated().sum()

if duplicate_count == 0:
    print("\n[PASS] No complete duplicate rows found")
else:
    print(f"\n[WARNING] Duplicate rows found: {duplicate_count}")


# --------------------------------------------------
# 5. MISSING VALUE CHECK
# --------------------------------------------------

print("\nMissing value summary:")

missing_values = df.isnull().sum()

for column, count in missing_values.items():

    if count > 0:
        percentage = (count / len(df)) * 100

        print(
            f"  {column}: "
            f"{count} missing "
            f"({percentage:.2f}%)"
        )


# --------------------------------------------------
# 6. DATE VALIDATION
# --------------------------------------------------

parsed_dates = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

invalid_dates = parsed_dates.isna().sum()

if invalid_dates == 0:
    print("\n[PASS] All dates are valid")
else:
    print(f"\n[WARNING] Invalid dates found: {invalid_dates}")


# --------------------------------------------------
# 7. QUANTITY VALIDATION
# --------------------------------------------------

numeric_qty = pd.to_numeric(
    df["Qty"],
    errors="coerce"
)

invalid_qty = numeric_qty.isna().sum()

if invalid_qty == 0:
    print("\n[PASS] Quantity column contains valid numbers")
else:
    print(f"\n[WARNING] Invalid quantities found: {invalid_qty}")


# --------------------------------------------------
# 8. AMOUNT VALIDATION
# --------------------------------------------------

numeric_amount = pd.to_numeric(
    df["Amount"],
    errors="coerce"
)

invalid_amount = numeric_amount.isna().sum()

print(f"\nAmount values that cannot be interpreted as numbers: {invalid_amount}")


# --------------------------------------------------
# END
# --------------------------------------------------

print("\n" + "=" * 60)
print("DATA QUALITY CHECK COMPLETE")
print("=" * 60)