# Cafe Sales — ETL & Analytics Pipeline

This project implements a complete **ETL (Extract, Transform, Load)** pipeline for cafe sales data, followed by a **Gold layer** optimized for analytics and a set of **business-focused analyses**.

---

## Project Goals

* Build a structured ETL pipeline (Bronze → Silver → Gold)
* Clean, normalize, and enrich raw sales data
* Persist curated datasets as Parquet files
* Load the Gold layer into DuckDB
* Enable business and exploratory analysis
* Apply professional logging and error handling

---

## Architecture

```
Raw CSV (Bronze)
      ↓
Extractor
      ↓
Transformer (Silver)
      ↓
Transformer (Gold)
      ↓
Parquet Files
      ↓
DuckDB Warehouse
      ↓
Analytics & Reporting
```

---

## Project Structure

```
project/
│
├── extract.py        # Data ingestion
├── transform.py     # Cleaning, validation, enrichment
├── load.py          # Parquet persistence
├── database.py      # DuckDB loading
├── main.py          # ETL orchestration
├── analysis.py      # Business & exploratory analysis
│
├── data/
│   ├── bronze/      # Raw CSV files
│   ├── silver/      # Cleaned datasets
│   └── gold/        # Analytics-ready datasets
│
├── logs/             # Runtime logs (ignored by Git)
├── analysis.sql      # Business queries
└── README.md
```

---

## Pipeline Layers

### Bronze (Raw)

* Raw CSV ingestion
* No transformations
* Preserves original data

### Silver (Cleaned)

* Column normalization
* Deduplication
* Type casting
* Missing value handling
* Error and missing flags
* Value inference

### Gold (Analytics)

* Filters invalid rows
* Business-ready columns
* Time features (month, weekday)
* Removes technical flags
* Optimized for reporting

---

## Key Business Analyses

1. Total revenue
2. Revenue by month
3. Revenue by weekday
4. Top 10 items by revenue
5. Top 10 items by quantity sold
6. Average ticket size
7. Payment method distribution
8. In-store vs Takeaway comparison
9. Seasonality by item
10. Data quality overview

---

## How to Run

### Install dependencies

```bash
pip install pandas numpy duckdb pyarrow
```

---

### Run the ETL pipeline

```bash
python main.py
```

This will:

* Read raw files from `data/bronze/`
* Generate Silver and Gold Parquet files
* Load Gold data into DuckDB
* Log execution steps

---

### Run the analysis

```bash
python analysis.py
```

---

## DuckDB

The Gold layer is loaded into DuckDB for analytical querying.

Database file:

```
data/warehouse.duckdb
```

---

## Logging

* Centralized logging configuration
* Logs stored in `logs/etl.log`
* Levels: INFO, WARNING, ERROR
* Full stacktrace on failures

---

## Ignored Files

The following are not versioned:

* Parquet files
* DuckDB files
* Logs

See `.gitignore`.

---

## Kaggle Dataset

The dataset used in this project was sourced from Kaggle. It contains dirty cafe sales data suitable for practising data cleaning, transformation, and analytics.

Original dataset link:
https://www.kaggle.com/datasets/ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training/data

---

## Author

Developed as a learning and portfolio project.

---

