# Analisi Dati per E-commerce in Reselling

Progetto finale di Data Analysis focalizzato su una pipeline dati semplice: generazione dataset CSV, pulizia con Pandas, caricamento in SQLite e query SQL per analisi e futura dashboard Power BI.

## Obiettivo

Simulare un piccolo e-commerce in reselling per analizzare:

- fatturato;
- performance per categoria;
- prodotti più venduti;
- prodotti con stock basso o invenduti;
- performance dei fornitori.

## Struttura minima del progetto

- `scripts/00_generate_dataset.py`: genera i CSV grezzi in `data/raw/`
- `scripts/02_etl_processing.py`: pulisce i dati e crea i CSV in `data/processed/`
- `scripts/01_create_database.py`: crea `database/ecommerce_reselling.db`
- `sql/create_tables.sql`: schema SQLite
- `sql/analysis_queries.sql`: query analitiche

## Strumenti usati

- Python
- Pandas
- NumPy
- SQLite
- Pathlib

## Pipeline dati

1. Generazione dei file CSV grezzi.
2. Pulizia e trasformazione dei dati.
3. Creazione delle metriche analitiche.
4. Esportazione dei file processati.
5. Creazione e popolamento del database SQLite.
6. Analisi con query SQL e collegamento a Power BI.

## Come eseguire il progetto

```bash
python -m venv .venv
```

Su Windows:

```bash
.venv\Scripts\activate
```

Installazione librerie:

```bash
pip install pandas numpy
```

Esecuzione pipeline:

```bash
python scripts/00_generate_dataset.py
python scripts/02_etl_processing.py
python scripts/01_create_database.py
```

## Output principali

- CSV grezzi: `data/raw/`
- CSV processati: `data/processed/`
- Database SQLite: `database/ecommerce_reselling.db`

## Uso in Power BI

Power BI può collegarsi:

- ai CSV in `data/processed/`, in particolare `sales_analysis_powerbi.csv`;
- oppure al database SQLite per usare direttamente le query SQL del progetto.
