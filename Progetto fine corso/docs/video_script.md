# Script video progetto - 3 minuti

## 0:00 - 0:20 | Introduzione

Ciao, in questo video presento il mio progetto di Data Analysis: Analisi Dati per E-commerce in Reselling.

Il progetto simula un caso aziendale in cui un e-commerce vende prodotti forniti da vendor esterni. L’obiettivo è analizzare prodotti, ordini, stock e fornitori per ricavare insight utili alle decisioni commerciali.

## 0:20 - 0:50 | Problema di business

In un modello di reselling, i prodotti provengono da fornitori diversi. Ogni fornitore può avere prezzi, disponibilità, tempi di consegna e affidabilità differenti.

Il problema è trasformare dati grezzi e separati in informazioni strutturate, così da capire quali categorie vendono di più, quali prodotti generano margine e quali fornitori performano meglio.

## 0:50 - 1:20 | Dataset e strumenti

Il progetto utilizza quattro dataset principali: suppliers, products, orders e order_items.

Ho utilizzato Python e Pandas per la pulizia e trasformazione dei dati, SQLite e SQL per la modellazione e interrogazione del database, Power BI per la dashboard finale e GitHub per documentare il progetto.

## 1:20 - 1:55 | Pipeline dati

La pipeline parte dai file CSV grezzi. I dati vengono caricati, controllati e puliti con Python.

Successivamente vengono create metriche calcolate come revenue, margin, margin percentage, stock value e stock status. I dati puliti vengono poi caricati in un database SQLite relazionale.

## 1:55 - 2:30 | Analisi e dashboard

Attraverso SQL e Power BI vengono analizzati i principali KPI: fatturato totale, numero di ordini, vendite per categoria, prodotti migliori, margine medio, prodotti con stock basso e performance dei fornitori.

La dashboard è organizzata in tre sezioni: overview generale, analisi prodotti e analisi fornitori.

## 2:30 - 3:00 | Conclusione

Il progetto mostra un flusso completo di Data Analysis: dai dati grezzi agli insight finali.

L’analisi permette di individuare prodotti ad alto potenziale, categorie più redditizie, fornitori più performanti e criticità legate allo stock. Possibili sviluppi futuri includono l’integrazione con dati reali, aggiornamenti automatici e analisi predittive.