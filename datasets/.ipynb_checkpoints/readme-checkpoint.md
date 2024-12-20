# Datasets Details

## Overview

This folder contains the datasets used for the development of data analysis reports. The description or lexicon of the data is located in the notebook **`data_description.ipynb`** [notebooks](https://github.com/javierdastas/project2-eda-sql/tree/main/notebooks) and in this text. To use this dataset as the **single source of truth (SSOT)** for the study, analysis and visualization of this project, these datasets were imported into a relational database.

To automate the process of importing datasets into the database, a Python code was used. This code is located in the repository folder at [pycode](https://github.com/javierdastas/project2-eda-sql/tree/main/pycode).

---

## Description of `Retail Data` Datasets 

### The Dataset contain historical sales data from 45 stores

## Content
The Retail Data provide an historical sales data for 45 stores located in different regions - each store contains a number of departments. The company also runs several promotional markdown events throughout the year. These markdowns precede prominent holidays, the four largest of which are the Super Bowl, Labor Day, Thanksgiving, and Christmas. The weeks including these holidays are weighted five times higher in the evaluation than non-holiday weeks.

## Stores (stores_dataset.csv)
Anonymized information about the 45 stores, indicating the type and size of store
- Store - the store number
- Type - Type of store
- Size - Size of the store

---

## Features (features_dataset.csv)
Contains additional data related to the store, department, and regional activity for the given dates.

- Store - the store number
- Date - the week
- Temperature - average temperature in the region
- Fuel_Price - cost of fuel in the region
- MarkDown1-5 - anonymized data related to promotional markdowns. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA
- CPI - the consumer price index
- Unemployment - the unemployment rate
- IsHoliday - whether the week is a special holiday week

---

## Sales (sales_dataset.csv)
Historical sales data, which covers to 2010-02-05 to 2012-11-01. Within this tab you will find the following fields:

- Store - the store number
- Dept - the department number
- Date - the week
- Weekly_Sales -  sales for the given department in the given store
- IsHoliday - whether the week is a special holiday week

---

## Data Relationships and Integrity

- **Primary Relationship**: The datasets are joined using `Store` number.
- **Key Insights**:
  - Each Store record corresponds to one or multiple Features and Sales records.

---

## How to Use

- **Dataset for ETL, EDA and Database Process**: Use `Business Challenge - EDA and SQL.ipynb` in [notebooks](https://github.com/javierdastas/project2-eda-sql/tree/main/notebooks) folder for all process.
- A [pycode folder](https://github.com/javierdastas/project2-eda-sql/tree/main/pycode) implement similar processes but in a more streamlined and production-oriented manner.
