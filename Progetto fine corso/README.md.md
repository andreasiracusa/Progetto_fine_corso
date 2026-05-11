# Analisi Dati per E-commerce in Reselling

## Panoramica del progetto

Questo progetto si concentra sull’analisi dei dati relativi a un modello e-commerce basato sul reselling.

L’obiettivo è trasformare dati grezzi relativi a fornitori, prodotti e ordini in dataset strutturati, tabelle SQL e insight analitici utili per supportare decisioni operative e commerciali.

Il focus del progetto non è lo sviluppo di un’applicazione, ma la costruzione di un flusso completo di Data Analysis: raccolta dati, pulizia, trasformazione, modellazione del database, analisi SQL e visualizzazione tramite dashboard.

## Problema di business

In un modello e-commerce basato su reselling, i prodotti vengono forniti da venditori esterni. Prezzi, disponibilità, tempi di consegna e affidabilità dei fornitori possono variare in modo significativo.

L’analisi ha l’obiettivo di rispondere a domande come:

- quali categorie generano più fatturato;
- quali prodotti hanno i margini migliori;
- quali fornitori performano meglio;
- quali prodotti hanno stock basso;
- quali prodotti non stanno vendendo;
- qual è il valore teorico del magazzino.

Queste informazioni possono supportare decisioni relative all’ottimizzazione del catalogo, alla gestione dei fornitori e al monitoraggio dello stock.

## Dataset

Il progetto utilizza quattro file CSV principali:

- `suppliers.csv`: contiene le informazioni sui fornitori;
- `products.csv`: contiene il catalogo prodotti;
- `orders.csv`: contiene le informazioni sugli ordini;
- `order_items.csv`: contiene le righe prodotto associate agli ordini.

## Strumenti utilizzati

- Python
- Pandas
- SQLite
- SQL
- Power BI
- VS Code
- GitHub

## Pipeline dei dati

Il flusso del progetto è il seguente:

```text
File CSV grezzi
      ↓
Pulizia dati con Python e Pandas
      ↓
Creazione di metriche calcolate
      ↓
Caricamento in database SQLite
      ↓
Analisi tramite query SQL
      ↓
Dashboard Power BI
      ↓
Insight finali