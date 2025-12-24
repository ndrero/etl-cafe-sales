# Dirty Cafe Sales Dataset

## Overview

This repository contains a synthetic cafe sales dataset inspired by a dataset available on Kaggle. The data was intentionally designed to include common real-world issues such as missing fields, inconsistent formatting, and invalid entries. This makes it a suitable resource for practicing data cleaning, ETL development, and exploratory data analysis.

The dataset simulates 10,000 point-of-sale transactions from a fictional cafe, covering items sold, payment information, locations, and timestamps.

---

## File Information

* **File:** `dirty_cafe_sales.csv`
* **Rows:** 10,000
* **Columns:** 8

---

## Column Summary

The dataset includes the following fields:

* **Transaction ID** — A unique identifier for each record.
* **Item** — The product purchased; some values may be missing or intentionally corrupted.
* **Quantity** — Number of units bought; may contain invalid values.
* **Price Per Unit** — Unit price of the item.
* **Total Spent** — The total amount paid for the transaction.
* **Payment Method** — Payment type used; includes inconsistent values.
* **Location** — Where the transaction took place (for example, in-store or takeaway).
* **Transaction Date** — Date of the sale; some entries may have incorrect or inconsistent formats.

---

## Dataset Characteristics

The data includes a variety of imperfections meant to simulate a real operational environment:

* Missing and null values in multiple columns
* Inconsistent categories such as `"UNKNOWN"` or `"ERROR"`
* Occasional mismatches between quantity, unit price, and total paid
* Dates that may require formatting or validation

Such issues provide opportunities to practice:

* Data validation
* Outlier detection
* Type conversion
* Standardization of categorical data
* Error handling in ETL processes

---

## Menu Items and Expected Price Ranges

To guide quality checks during cleaning, the dataset assumes approximate price ranges for typical cafe items:

| Item     | Typical Price ($) |
| -------- | ----------------- |
| Coffee   | ~2.0              |
| Tea      | ~1.5              |
| Sandwich | ~4.0              |
| Salad    | ~5.0              |
| Cake     | ~3.0              |
| Cookie   | ~1.0              |
| Smoothie | ~4.0              |
| Juice    | ~3.0              |

---

## Suggested Cleaning and Preparation Steps

Below are general recommendations for working with the dataset:

1. **Handle missing values**

   * Impute numeric fields with statistical measures
   * Set missing categorical values to `"Unknown"` or an appropriate label

2. **Correct invalid or inconsistent entries**

   * Replace placeholders like `"ERROR"` or `"UNKNOWN"`
   * Validate quantities and prices

3. **Normalize date information**

   * Convert all timestamps to ISO format
   * Identify or flag dates that cannot be parsed

4. **Feature engineering (optional)**

   * Extract weekday, month, or hour from the date
   * Classify transactions by type or location

---

## Usage

The dataset is suitable for:

* Practicing Python data cleaning or ETL scripting
* Demonstrating notebook-based EDA
* Testing data pipelines
* Building feature engineering examples and tutorials

---

If you want, I can also generate:

* A second README describing your ETL architecture
* A notebook template for cleaning the dataset
* A full Python ETL structure using modules and logging
