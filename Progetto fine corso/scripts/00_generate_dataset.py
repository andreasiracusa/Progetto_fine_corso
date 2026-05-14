from pathlib import Path
import random
import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"

random.seed(42)
np.random.seed(42)

RAW_DIR.mkdir(parents=True, exist_ok=True)

categories = {
    "Electronics": ["Wireless Mouse", "Bluetooth Speaker", "Smart Plug", "USB-C Hub"],
    "Home": ["Storage Box", "Desk Lamp", "Wall Shelf", "Air Humidifier"],
    "Fitness": ["Yoga Mat", "Resistance Band", "Foam Roller", "Jump Rope"],
    "Beauty": ["Face Cleanser", "Hair Dryer", "Body Lotion", "Makeup Mirror"],
    "Office": ["Notebook Set", "Desk Organizer", "Monitor Stand", "Pen Kit"],
    "Green Living": ["Reusable Bottle", "Lunch Box", "Compost Bin", "Bamboo Cutlery"],
    "Kids": ["Puzzle Set", "Drawing Kit", "Night Light", "Toy Basket"],
    "Pet Care": ["Pet Bowl", "Pet Brush", "Cat Toy", "Dog Leash"],
}

suppliers = pd.DataFrame([
    [1, "TechNova Supplies", "Italy", 3, 4.8],
    [2, "EuroDigital Hub", "Germany", 5, 4.4],
    [3, "SmartLife Wholesale", "Spain", 6, 4.1],
    [4, "HomeStyle Distribution", "France", 4, 4.5],
    [5, "UrbanFit Partners", "Netherlands", 7, 3.9],
    [6, "BeautyPro Trade", "Italy", 2, 4.7],
    [7, "OfficePlus Vendor", "Germany", 5, 4.2],
    [8, "EcoTrend Supply", "Sweden", 6, 4.3],
    [9, "KidsWorld Source", "Poland", 8, 3.8],
    [10, "PetCare Central", "Belgium", 4, 4.6],
], columns=["supplier_id", "supplier_name", "country", "delivery_days", "reliability_score"])

supplier_map = {
    "Electronics": 1, "Home": 4, "Fitness": 5, "Beauty": 6,
    "Office": 7, "Green Living": 8, "Kids": 9, "Pet Care": 10
}
brand_map = {
    1: "TechNova", 4: "HomeStyle", 5: "UrbanFit", 6: "BeautyPro",
    7: "OfficePlus", 8: "EcoTrend", 9: "KidsWorld", 10: "PetCare"
}

products_data = []
product_id = 1
for category, names in categories.items():
    supplier_id = supplier_map[category]
    for i in range(14):
        name = f"{random.choice(names)} {i + 1}"
        cost_price = round(random.uniform(5, 80), 2)
        selling_price = round(cost_price * random.uniform(1.25, 1.9), 2)
        stock_quantity = random.choice([8, 12, 18, 25, 40, 60, 90, 120, 150])
        sku = f"{category[:2].upper()}-{product_id:03d}"
        last_update = pd.Timestamp("2025-12-01") + pd.Timedelta(days=random.randint(0, 120))
        products_data.append([
            product_id, supplier_id, sku, name, category, brand_map[supplier_id],
            cost_price, selling_price, stock_quantity, last_update.strftime("%Y-%m-%d")
        ])
        product_id += 1

products = pd.DataFrame(products_data, columns=[
    "product_id", "supplier_id", "sku", "product_name", "category", "brand",
    "cost_price", "selling_price", "stock_quantity", "last_update"
])

order_dates = pd.date_range("2025-08-01", "2026-03-31", freq="D")
statuses = ["Completed", "Completed", "Completed", "Processing", "Cancelled", "Returned"]
countries = ["Italy", "Germany", "France", "Spain", "Austria", "Netherlands"]
orders = pd.DataFrame({
    "order_id": range(1, 421),
    "order_date": np.random.choice(order_dates, 420),
    "customer_id": np.random.randint(1000, 1180, 420),
    "order_status": np.random.choice(statuses, 420),
    "country": np.random.choice(countries, 420)
}).sort_values("order_date").reset_index(drop=True)
orders["order_id"] = range(1, len(orders) + 1)
orders["order_date"] = pd.to_datetime(orders["order_date"]).dt.strftime("%Y-%m-%d")

weights = np.linspace(3, 0.2, len(products))
weights[-12:] = 0
weights = weights / weights.sum()
items = []
order_item_id = 1
for order_id in orders["order_id"]:
    for _ in range(random.randint(1, 4)):
        product_id = int(np.random.choice(products["product_id"], p=weights))
        product = products.loc[products["product_id"] == product_id].iloc[0]
        unit_price = round(product["selling_price"] * random.choice([1.0, 1.0, 0.98, 0.95]), 2)
        items.append([order_item_id, order_id, product_id, random.randint(1, 3), unit_price])
        order_item_id += 1

order_items = pd.DataFrame(items, columns=["order_item_id", "order_id", "product_id", "quantity", "unit_price"])
if len(order_items) > 1100:
    order_items = order_items.head(1100)

suppliers.to_csv(RAW_DIR / "suppliers.csv", index=False)
products.to_csv(RAW_DIR / "products.csv", index=False)
orders.to_csv(RAW_DIR / "orders.csv", index=False)
order_items.to_csv(RAW_DIR / "order_items.csv", index=False)

print("Dataset generato in data/raw/")
print(f"suppliers: {len(suppliers)}")
print(f"products: {len(products)}")
print(f"orders: {len(orders)}")
print(f"order_items: {len(order_items)}")
