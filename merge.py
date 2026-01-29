import pandas as pd

files = [
    ("Exporters-of-Crude-Petroleum-1996.xlsx", 1996),
    ("Exporters-of-Crude-Petroleum-2001.xlsx", 2001),
    ("Exporters-of-Crude-Petroleum-2006.xlsx", 2006),
    ("Exporters-of-Crude-Petroleum-2011.xlsx", 2011),
    ("Exporters-of-Crude-Petroleum-2016.xlsx", 2016),
    ("Exporters-of-Crude-Petroleum-2020.xlsx", 2020),
]

dfs = []

for file, year in files:
    df = pd.read_excel(file)
    df["Year"] = year
    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

merged.to_excel("Crude_Petroleum_Exports_1996_2020.xlsx", index=False)
