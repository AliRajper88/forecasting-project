def load_and_normalize(path, dataset_name):

    df = pd.read_csv(path)

    print(f"\n{dataset_name} Columns:", df.columns)

    # -----------------------------
    # DEMAND DATASET
    # -----------------------------
    if dataset_name == "demand":
        df['date'] = pd.to_datetime(df['Date'])

        df = df.rename(columns={
            'Store ID': 'store_id',
            'Product ID': 'product_id',
            'Sales Quantity': 'sales'
        })

        df['price'] = df['Price']
        df['promo'] = df['Promotions']

    # -----------------------------
    # INVENTORY DATASET
    # -----------------------------
    elif dataset_name == "inventory":

        df = df.rename(columns={
            'Store ID': 'store_id',
            'Product ID': 'product_id'
        })

        df['date'] = None
        df['sales'] = None
        df['price'] = None
        df['promo'] = None

    # -----------------------------
    # PRICING DATASET
    # -----------------------------
    elif dataset_name == "pricing":

        df = df.rename(columns={
            'Store ID': 'store_id',
            'Product ID': 'product_id'
        })

        df['date'] = None
        df['sales'] = None
        df['price'] = df['Price']
        df['promo'] = None

    # -----------------------------
    # ADD DATASET LABEL
    # -----------------------------
    df['dataset'] = dataset_name

    return df[['date','store_id','product_id','sales','price','promo','dataset']]

if __name__ == "__main__":

    import pandas as pd
    import os

    # Load datasets
    demand = load_and_normalize(
        "data/raw/kaggle/demand_forecasting.csv",
        "demand"
    )

    inventory = load_and_normalize(
        "data/raw/kaggle/inventory_monitoring.csv",
        "inventory"
    )

    pricing = load_and_normalize(
        "data/raw/kaggle/pricing_optimization.csv",
        "pricing"
    )

    # Combine
    final_df = pd.concat([demand, inventory, pricing], ignore_index=True)

    # View data
    print(final_df.head(10))

    # Save file
    os.makedirs("data/processed", exist_ok=True)
    final_df.to_csv("data/processed/unified_data.csv", index=False)

    print("\nSaved to data/processed/unified_data.csv")