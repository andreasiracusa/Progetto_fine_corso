from pathlib import Path
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

suppliers = pd.read_csv(RAW_DIR / "suppliers.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
orders = pd.read_csv(RAW_DIR / "orders.csv")
order_items = pd.read_csv(RAW_DIR / "order_items.csv")

datasets = {
    "suppliers": suppliers,
    "products": products,
    "orders": orders,
    "order_items": order_items,
}

print("Controllo valori nulli:")
for name, df in datasets.items():
    print(f"- {name}: {int(df.isna().sum().sum())}")

print("Controllo duplicati:")
for name, df in datasets.items():
    print(f"- {name}: {int(df.duplicated().sum())}")

orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["order_month"] = orders["order_date"].dt.strftime("%Y-%m")
orders["order_date"] = orders["order_date"].dt.strftime("%Y-%m-%d")

numeric_columns = {
    "products": ["cost_price", "selling_price", "stock_quantity"],
    "order_items": ["quantity", "unit_price"],
    "suppliers": ["delivery_days", "reliability_score"],
}
for column in numeric_columns["products"]:
    products[column] = pd.to_numeric(products[column])
for column in numeric_columns["order_items"]:
    order_items[column] = pd.to_numeric(order_items[column])
for column in numeric_columns["suppliers"]:
    suppliers[column] = pd.to_numeric(suppliers[column])

missing_supplier = ~products["supplier_id"].isin(suppliers["supplier_id"])
missing_order = ~order_items["order_id"].isin(orders["order_id"])
missing_product = ~order_items["product_id"].isin(products["product_id"])
print("Controllo relazioni:")
print(f"- product senza supplier: {int(missing_supplier.sum())}")
print(f"- order_item senza order: {int(missing_order.sum())}")
print(f"- order_item senza product: {int(missing_product.sum())}")

products["margin"] = (products["selling_price"] - products["cost_price"]).round(2)
products["margin_percentage"] = (products["margin"] / products["selling_price"]).round(4)
products["stock_value"] = (products["stock_quantity"] * products["cost_price"]).round(2)
products["stock_status"] = np.where(
    products["stock_quantity"] < 20, "Low Stock",
    np.where(products["stock_quantity"] <= 80, "Medium Stock", "High Stock")
)
order_items["revenue"] = (order_items["quantity"] * order_items["unit_price"]).round(2)

sales_analysis = (
    order_items
    .merge(orders, on="order_id", how="left")
    .merge(products, on="product_id", how="left")
    .merge(suppliers, on="supplier_id", how="left")
)[[
    "order_id", "order_date", "order_month", "order_status", "customer_id", "country_x",
    "product_id", "product_name", "category", "brand", "supplier_id", "supplier_name",
    "quantity", "unit_price", "revenue", "cost_price", "selling_price", "margin",
    "margin_percentage", "stock_quantity", "stock_status", "delivery_days", "reliability_score"
]].rename(columns={"country_x": "country"})

suppliers.to_csv(PROCESSED_DIR / "suppliers.csv", index=False)
products.to_csv(PROCESSED_DIR / "products.csv", index=False)
orders.to_csv(PROCESSED_DIR / "orders.csv", index=False)
order_items.to_csv(PROCESSED_DIR / "order_items.csv", index=False)
sales_analysis.to_csv(PROCESSED_DIR / "sales_analysis.csv", index=False)

print("File salvati in data/processed/")
for file_name, df in {
    "suppliers.csv": suppliers,
    "products.csv": products,
    "orders.csv": orders,
    "order_items.csv": order_items,
    "sales_analysis.csv": sales_analysis,
}.items():
    print(f"- {file_name}: {len(df)} righe")
