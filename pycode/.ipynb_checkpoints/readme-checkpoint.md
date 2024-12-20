# Project 2 Business Challenge: EDA and SQL - Python Code

## Overview

This folder contains the Python scripts that implement the core processes of the **Data Analysis Project** hosted in the repository [project2-eda-sql](https://github.com/javierdastas/project2-eda-sql). These scripts focus on automating and executing:

- **ETL (Extract, Transform, Load):** Efficiently processing raw data and preparing it for upload to RDBMS.
- **EDA (Exploratory Data Analysis):** Identifying patterns, trends, and data quality issues.
- **DataBase Data Loader:** Releational Database creation and data loader.

These scripts are designed for production and operational use, complementing the detailed, exploratory work presented in the [notebooks](https://github.com/javierdastas/project2-eda-sql/tree/main/notebooks) folder.

---

## Scripts Included

### 1. **Automation Process**

- **Script:** `main.py`
- **Description:**
  - Automates the extraction of raw data from source files and data import to the DataBase.
  - Loads the processed data into structured formats for further analysis or RDBMS load.

### 2. **ETL and EDA Process**

- **Script:** `datasets_loader.py`
- **Description:**
  - Implements descriptive statistics and summary.
  - Performs data transformations, such as cleaning, formatting, and normalization.
  - Identifies data distributions, correlations, and anomalies.
  - Generates key insights for further exploration or reporting.
  
### 3. **DataBase Process**

- **Script:** `database_loader.py`
- **Description:**
  - Automates the creation of the database and tables.
  - Import DataSets to database tables.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/javierdastas/project2-eda-sql.git
   ```
2. Navigate to the `pycode` folder:
   ```bash
   cd project2-eda-sql/pycode
   ```
3. Edit the code in lines 8 to 10 with your database (RDBMS) information:
   ```bash
    # DataBase or RDBMS Access Configuration
    database_config = {
        "server" : "your-computer", # database server name or ip address, localhost for your computer
        "user" : "your-username", # database user account with privileges
        "pwd" : "your-password", # password for the user
    }
   ```
4. Run the `main` script:
   ```bash
   python main.py
   ```
---

## Relation to Jupyter Notebooks

While the scripts in this folder are optimized for operational use, the [notebooks folder](https://github.com/javierdastas/project2-eda-sql/tree/main/notebooks):

- Provides detailed step-by-step explanations for each process.
- Focuses on the educational and exploratory aspects of the project.
- Serves as a complementary resource for understanding the logic implemented in these scripts.

---

## Contact

For questions or further details, please contact the project team via the repository's Issues or Discussions section.
