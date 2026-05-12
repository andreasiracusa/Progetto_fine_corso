# Descrizione del dataset

Il progetto utilizza quattro file CSV che simulano i dati di un e-commerce basato su reselling.

## 1. suppliers.csv

Contiene le informazioni relative ai fornitori esterni.

| Colonna | Descrizione |
|---|---|
| supplier_id | Identificativo univoco del fornitore |
| supplier_name | Nome del fornitore |
| country | Paese del fornitore |
| delivery_days | Giorni medi di consegna |
| reliability_score | Punteggio di affidabilità del fornitore |

## 2. products.csv

Contiene il catalogo prodotti.

| Colonna | Descrizione |
|---|---|
| product_id | Identificativo univoco del prodotto |
| supplier_id | Identificativo del fornitore associato |
| sku | Codice prodotto |
| product_name | Nome del prodotto |
| category | Categoria del prodotto |
| brand | Marchio del prodotto |
| cost_price | Prezzo di acquisto |
| selling_price | Prezzo di vendita |
| stock_quantity | Quantità disponibile a magazzino |
| last_update | Data dell’ultimo aggiornamento del prodotto |

## 3. orders.csv

Contiene le informazioni generali sugli ordini.

| Colonna | Descrizione |
|---|---|
| order_id | Identificativo univoco dell’ordine |
| order_date | Data dell’ordine |
| customer_id | Identificativo del cliente |
| order_status | Stato dell’ordine |
| country | Paese del cliente |

## 4. order_items.csv

Contiene le righe prodotto associate agli ordini.

| Colonna | Descrizione |
|---|---|
| order_item_id | Identificativo univoco della riga ordine |
| order_id | Identificativo dell’ordine |
| product_id | Identificativo del prodotto acquistato |
| quantity | Quantità acquistata |
| unit_price | Prezzo unitario di vendita |

## Relazioni tra le tabelle

- `suppliers.supplier_id` è collegato a `products.supplier_id`
- `products.product_id` è collegato a `order_items.product_id`
- `orders.order_id` è collegato a `order_items.order_id`