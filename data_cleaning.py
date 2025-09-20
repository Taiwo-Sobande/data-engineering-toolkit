import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans a pandas DataFrame:
    - Removes duplicate rows
    - Removes rows with missing values
    - Strips whitespace from string columns
    - Converts column names to lowercase and strips spaces
    - Standardizes date columns to datetime format
    - Fills numeric NaNs with 0
    - Drops columns that are completely empty
    """
    # 1. Drop completely empty columns
    df = df.dropna(axis=1, how='all')

    # 2. Drop duplicate rows
    df = df.drop_duplicates()

    # 3. Drop rows with missing values (optional - could also fill them instead)
    df = df.dropna()

    # 4. Standardize column names
    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]

    # 5. Strip whitespace from string/object columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()

    # 6. Convert any date-like columns to datetime
    for col in df.columns:
        if "date" in col or "time" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception:
                pass

    # 7. Fill NaNs in numeric columns with 0
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(0)

    return df
