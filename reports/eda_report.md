
# EDA Report — Phase 2
# IRS-1: AI-Driven Demand Intelligence
# Generated: 2026-05-28 18:38

## 1. DATASET OVERVIEW

### Kaggle Inventory Optimization Dataset
- Source: kaggle.com/datasets/suvroo/inventory-optimization-for-retail
- Files: demand_forecasting.csv, inventory_monitoring.csv, pricing_optimization.csv
- After merging: 4,592 rows, 72 columns
- Date range: 2024-01-01 to 2024-12-30
- Unique stores: 99
- Unique products: 1918

### FreshRetailNet-50K Dataset
- Source: HuggingFace — fresh produce daily transactions
- Rows: 4,500,000 | Columns: 39
- Date range: 2024-03-28 to 2024-06-25
- Unique stores: 898
- Unique products: 865
- Mean rows per product: 5,202 (suitable for LSTM/TFT)

## 2. DATA QUALITY

### Missing Values
- Kaggle: 41,978 missing values before imputation
  Fixed by: forward-fill + backward-fill + median fill
  After fix: 0 missing values
- FreshRetailNet: 50,000 missing (lag_1 NaN at series start)
  Fixed by: ffill + bfill
  After fix: 0 missing values

### Outlier Detection
- Kaggle IQR outliers: 0 (data already clean)
- Kaggle Isolation Forest: 230 rows flagged (5%)
- FreshRetailNet IQR: flagged and winsorized
- FreshRetailNet ISO Forest: flagged as is_outlier feature
- Treatment: Winsorization (cap not remove) for time series

## 3. FEATURE ENGINEERING

### Time Features
- year, month, day, day_of_week, is_weekend, quarter, week_of_year

### Lag Features
- Kaggle: lag_1, lag_2, lag_3
- FreshRetailNet: lag_1, lag_2, lag_3, lag_7, lag_14

### Rolling Window Features
- Kaggle: rolling_mean_2, rolling_std_2, rolling_mean_3, rolling_std_3
- FreshRetailNet: rolling_mean_3, rolling_std_3, rolling_mean_7, rolling_std_7, rolling_mean_14, rolling_std_14

### Seasonality Features
- Fourier terms: sin_1, cos_1, sin_2, cos_2, sin_3, cos_3

### External Features
- Holiday flags (FreshRetailNet: holiday_flag, activity_flag)
- Weather (avg_temperature, avg_humidity, avg_wind_level)
- Discount signals
- Macroeconomic (CPI, unemployment_rate, consumer_confidence)
- Geographical distance features

## 4. ABC-XYZ CLASSIFICATION

### Kaggle Dataset
- A class (top 70% revenue): 3,720 products
- B class (70-90% revenue): 854 products
- C class (bottom 10%): 1,491 products
- X class (CV < 0.5 stable): dominant in AX segment
- AX segment: 2,432 rows (high value, stable demand)

### FreshRetailNet
- AX: 10 products (stable high-value produce)
- CZ: 53 products (volatile low-value produce)
- High Z-class reflects perishable demand volatility

## 5. KEY FINDINGS

1. Kaggle data averages 2.4 rows per product — sparse
   Solution: lag_1/2/3 used instead of longer windows

2. FreshRetailNet averages 5,202 rows per product — rich
   Suitable for LSTM (30+ rows) and TFT (50+ rows)

3. Sales distribution: approximately uniform 0-1 (scaled)

4. Promotional events correlate with 15-20% sales increase

5. Seasonality: clear weekly patterns in FreshRetailNet

## 6. SAVED FILES
- demand_features_v2.csv: 4,592 rows, 72 cols
- fresh_features.csv: 4,500,000 rows, 39 cols
- product_segments.csv: 6,065 Kaggle products classified
- fresh_segments.csv: 865 FreshRetailNet products classified
- feature_columns.json: 56 ML features defined
