import os
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def save_data(df, filename, file_format="csv"):
    """
    Saves a DataFrame to disk in the specified format.
    
    Parameters:
    - df: pandas DataFrame
    - filename: str, path without extension
    - file_format: str, one of ["csv", "parquet", "json"]
    """

    # Ensure output directory exists
    output_dir = os.path.dirname(filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        logging.info(f"Created directory: {output_dir}")

    try:
        if file_format == "csv":
            df.to_csv(f"{filename}.csv", index=False)
        elif file_format == "parquet":
            df.to_parquet(f"{filename}.parquet", index=False)
        elif file_format == "json":
            df.to_json(f"{filename}.json", orient="records", lines=True)
        else:
            raise ValueError("Unsupported file format. Choose csv, parquet, or json.")

        logging.info(f"Data successfully saved as {filename}.{file_format}")

    except Exception as e:
        logging.error(f"Error saving file: {e}")
        raise
