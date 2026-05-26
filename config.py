# ================================
# config.py — Project Configuration
# IRS-1: AI-Driven Demand Intelligence
# ================================
from pathlib import Path

# ── Auto-detect project root ──────────────────────────────────────
# Works on ANY computer — no hardcoded paths needed
PROJECT_ROOT = Path(__file__).resolve().parent

# ── Data paths ────────────────────────────────────────────────────
RAW_PATH       = PROJECT_ROOT / "data" / "raw"
KAGGLE_PATH    = RAW_PATH / "kaggle"
FRESH_PATH     = RAW_PATH / "freshretailnet"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"
MODELS_PATH    = PROJECT_ROOT / "models"

# ── Key processed files ───────────────────────────────────────────
KAGGLE_ENCODED   = PROCESSED_PATH / "kaggle_unified_encoded.csv"
FRESH_PROCESSED  = PROCESSED_PATH / "fresh_processed.csv"
DEMAND_FEATURES  = PROCESSED_PATH / "demand_features_v2.csv"
PRODUCT_SEGMENTS = PROCESSED_PATH / "product_segments.csv"
FEATURE_COLUMNS  = PROCESSED_PATH / "feature_columns.json"
MODEL_RESULTS    = PROCESSED_PATH / "model_results.csv"

# ── Create folders if they do not exist ───────────────────────────
for path in [RAW_PATH, KAGGLE_PATH, FRESH_PATH,
             PROCESSED_PATH, MODELS_PATH]:
    path.mkdir(parents=True, exist_ok=True)
