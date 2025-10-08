import pandas as pd
import os

DATA_PATH = "data/player.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"File not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH, low_memory=False)
print("Loaded player.csv successfully")
print(f"Shape: {df.shape}\n")

print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head(), "\n")

print("Null values per column:")
print(df.isnull().sum(), "\n")

print("Duplicate rows:", df.duplicated().sum())
print("Unique player IDs:", df['id'].nunique(), "\n")

print("Active vs Inactive:")
print(df['is_active'].value_counts(), "\n")

df['first_name'] = df['first_name'].fillna('')

output_path = "outputs/clean_player.csv"
df.to_csv(output_path, index=False)
print(f"Cleaned dataset saved → {output_path}")