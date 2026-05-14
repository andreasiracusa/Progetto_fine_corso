from pathlib import Path
import sqlite3
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
DB_DIR = BASE_DIR / "database"
SQL_FILE = BASE_DIR / "sql" / "create_tables.sql"
DB_FILE = DB_DIR / "ecommerce_reselling.db"

DB_DIR.mkdir(parents=True, exist_ok=True)
if DB_FILE.exists():
    DB_FILE.unlink()

connection = sqlite3.connect(DB_FILE)
connection.execute("PRAGMA foreign_keys = ON;")

with open(SQL_FILE, "r", encoding="utf-8") as file:
    connection.executescript(file.read())

tables = {
    "suppliers": pd.read_csv(RAW_DIR / "suppliers.csv"),
    "products": pd.read_csv(RAW_DIR / "products.csv"),
    "orders": pd.read_csv(RAW_DIR / "orders.csv"),
    "order_items": pd.read_csv(RAW_DIR / "order_items.csv"),
}

for table_name, dataframe in tables.items():
    dataframe.to_sql(table_name, connection, if_exists="append", index=False)

print("Database creato correttamente:")
for table_name in tables:
    total_rows = connection.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
    print(f"- {table_name}: {total_rows} righe")

connection.close()
print(f"File salvato in: {DB_FILE}")
