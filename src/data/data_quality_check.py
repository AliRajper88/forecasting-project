from data_ingestion import load_data

demand, inventory, pricing = load_data()

print("Missing values (Demand):")
print(demand.isnull().sum())

print("\nMissing values (Inventory):")
print(inventory.isnull().sum())

print("\nMissing values (Pricing):")
print(pricing.isnull().sum())