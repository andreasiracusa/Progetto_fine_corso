-- Schema SQLite del progetto e-commerce in reselling

DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

-- Tabella fornitori
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    supplier_name TEXT NOT NULL,
    country TEXT NOT NULL,
    delivery_days INTEGER NOT NULL,
    reliability_score REAL NOT NULL
);

-- Tabella prodotti
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    supplier_id INTEGER NOT NULL,
    sku TEXT NOT NULL UNIQUE,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    brand TEXT NOT NULL,
    cost_price REAL NOT NULL,
    selling_price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    last_update TEXT NOT NULL,
    FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
);

-- Tabella ordini
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT NOT NULL,
    customer_id INTEGER NOT NULL,
    order_status TEXT NOT NULL,
    country TEXT NOT NULL
);

-- Tabella righe ordine
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders (order_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);
