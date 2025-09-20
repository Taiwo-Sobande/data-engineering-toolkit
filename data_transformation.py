def transform_data(df):
    """
  
    - Calculates total amount (quantity * price)
    - Creates discount and final price columns
    
    """

  
    # Add calculated column
    df["total_amount"] = df["quantity"] * df["price"]

    # Add discount column (e.g., 10% discount for orders above 1000)
    df["discount"] = df["total_amount"].apply(lambda x: x * 0.1 if x > 500 else 0)

    # Add final price after discount
    df["final_price"] = df["total_amount"] - df["discount"]

    return df
