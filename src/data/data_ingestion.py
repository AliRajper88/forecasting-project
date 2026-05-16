import pandas as pd
import os
from pathlib import Path

# ── Dynamic base paths (works on any computer, any OS) ────────
BASE = Path(__file__).resolve().parents[2]
RAW  = BASE / "data" / "raw" / "kaggle"
PROC = BASE / "data" / "processed"


def load_and_normalize(path, dataset_name):

    df = pd.read_csv(path)

    print(f"\n{dataset_name} Columns:", df.columns)

    # -----------------------------
    # DEMAND DATASET
    # -----------------------------
    if dataset_name == "demand":
        df['date'] = pd.to_datetime(df['Date'])

        df = df.rename(columns={
            'Store ID':       'store_id',
            'Product ID':     'product_id',
            'Sales Quantity': 'sales'
        })

        df['price'] = df['Price']
        df['promo'] = df['Promotions']

    # -----------------------------
    # INVENTORY DATASET
    # -----------------------------
    elif dataset_name == "inventory":

        df = df.rename(columns={
            'Store ID':   'store_id',
            'Product ID': 'product_id'
        })

        df['date']  = None
        df['sales'] = None
        df['price'] = None
        df['promo'] = None

    # -----------------------------
    # PRICING DATASET
    # -----------------------------
    elif dataset_name == "pricing":

        df = df.rename(columns={
            'Store ID':   'store_id',
            'Product ID': 'product_id'
        })

        df['date']  = None
        df['sales'] = None
        df['price'] = df['Price']
        df['promo'] = None

    # -----------------------------
    # ADD DATASET LABEL
    # -----------------------------
    df['dataset'] = dataset_name

    return df[['date', 'store_id', 'product_id', 'sales', 'price', 'promo', 'dataset']]


if __name__ == "__main__":

    # ── Load datasets using pathlib paths ─────────────────────
    demand = load_and_normalize(
        RAW / "demand_forecasting.csv",
        "demand"
    )

    inventory = load_and_normalize(
        RAW / "inventory_monitoring.csv",
        "inventory"
    )

    pricing = load_and_normalize(
        RAW / "pricing_optimization.csv",
        "pricing"
    )

    # ── Combine all three ─────────────────────────────────────
    final_df = pd.concat([demand, inventory, pricing], ignore_index=True)

    # ── Preview ───────────────────────────────────────────────
    print(final_df.head(10))

    # ── Save to processed folder ──────────────────────────────
    PROC.mkdir(parents=True, exist_ok=True)
    final_df.to_csv(PROC / "unified_data.csv", index=False)

    print("\nSaved to data/processed/unified_data.csv")