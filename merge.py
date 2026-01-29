from pathlib import Path
import pandas as pd

# Project root = where this script lives
BASE_DIR = Path(__file__).resolve().parent

# Dataset folder
DATASET_DIR = BASE_DIR / "dataset"

files = [
    ("Exporters-of-Crude-Petroleum-1996-Click-to-Select-a-Country.xlsx", 1996),
    ("Exporters-of-Crude-Petroleum-2001-Click-to-Select-a-Country.xlsx", 2001),
    ("Exporters-of-Crude-Petroleum-2006-Click-to-Select-a-Country.xlsx", 2006),
    ("Exporters-of-Crude-Petroleum-2011-Click-to-Select-a-Country.xlsx", 2011),
    ("Exporters-of-Crude-Petroleum-2016-Click-to-Select-a-Country.xlsx", 2016),
    ("Exporters-of-Crude-Petroleum-2020-Click-to-Select-a-Country.xlsx", 2020),
]

dfs = []

for filename, year in files:
    file_path = DATASET_DIR / filename
    df = pd.read_excel(file_path)
    df["Year"] = year
    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

output_path = BASE_DIR / "Crude_Petroleum_Exports_1996_2020.xlsx"
merged.to_excel(output_path, index=False)

print("Merge complete:", output_path)
