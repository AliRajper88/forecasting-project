import pandas as pd

# Load parquet file
df = pd.read_parquet("FreshRetailNet-50k/data/train.parquet")

# Save as CSV
df.to_csv("train.csv", index=False)

print(df.head())