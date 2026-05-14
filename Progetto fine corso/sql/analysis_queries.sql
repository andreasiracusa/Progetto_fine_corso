-- Query analitiche principali per SQLite

-- 1. Fatturato totale netto
SELECT ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned');

-- 2. Numero totale di ordini
SELECT COUNT(*) AS total_orders
FROM orders;

-- 3. Fatturato per mese
SELECT substr(o.order_date, 1, 7) AS order_month,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY substr(o.order_date, 1, 7)
ORDER BY order_month;

-- 4. Fatturato per categoria
SELECT p.category,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY p.category
ORDER BY revenue DESC;

-- 5. Top 10 prodotti per fatturato
SELECT p.product_name,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 6. Top 10 prodotti per quantità venduta
SELECT p.product_name,
       SUM(oi.quantity) AS units_sold
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY p.product_id, p.product_name
ORDER BY units_sold DESC
LIMIT 10;

-- 7. Margine medio per categoria
SELECT category,
       ROUND(AVG(selling_price - cost_price), 2) AS avg_margin
FROM products
GROUP BY category
ORDER BY avg_margin DESC;

-- 8. Performance dei fornitori per fatturato
SELECT s.supplier_name,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
JOIN suppliers s ON s.supplier_id = p.supplier_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned')
GROUP BY s.supplier_id, s.supplier_name
ORDER BY revenue DESC;

-- 9. Performance dei fornitori per margine medio prodotto
SELECT s.supplier_name,
       ROUND(AVG(p.selling_price - p.cost_price), 2) AS avg_margin
FROM products p
JOIN suppliers s ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.supplier_name
ORDER BY avg_margin DESC;

-- 10. Prodotti con stock basso
SELECT product_id, product_name, category, stock_quantity
FROM products
WHERE stock_quantity < 20
ORDER BY stock_quantity ASC;

-- 11. Prodotti invenduti
SELECT p.product_id, p.product_name, p.category
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.product_id IS NULL
ORDER BY p.product_id;

-- 12. Valore teorico dello stock
SELECT ROUND(SUM(stock_quantity * cost_price), 2) AS stock_value
FROM products;

-- 13. Confronto tra affidabilità fornitore e revenue generata
SELECT s.supplier_name,
       s.reliability_score,
       ROUND(SUM(oi.quantity * oi.unit_price), 2) AS revenue
FROM suppliers s
JOIN products p ON p.supplier_id = s.supplier_id
LEFT JOIN order_items oi ON oi.product_id = p.product_id
LEFT JOIN orders o ON o.order_id = oi.order_id
WHERE o.order_status NOT IN ('Cancelled', 'Returned') OR o.order_status IS NULL
GROUP BY s.supplier_id, s.supplier_name, s.reliability_score
ORDER BY s.reliability_score DESC, revenue DESC;

-- 14. Ordini per paese
SELECT country, COUNT(*) AS total_orders
FROM orders
GROUP BY country
ORDER BY total_orders DESC;

-- 15. Tasso di ordini cancellati o restituiti
SELECT ROUND(
    100.0 * SUM(CASE WHEN order_status IN ('Cancelled', 'Returned') THEN 1 ELSE 0 END) / COUNT(*),
    2
) AS cancelled_or_returned_rate
FROM orders;
