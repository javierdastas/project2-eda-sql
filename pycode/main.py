# Import necessary libraries
import pandas as pd
from datasets_loader import load_datasets, datasets_description, datasets_analysis, data_standarization
from database_loader import connect_to_database, create_database, create_tables, database_loader

# DataBase or RDBMS Access Configuration
database_config = {
    "server":"localhost", # database server name or ip address
    "user":"root", # database user account with privileges
    "pwd":"root", # password for the user
}

database_name = "retail_data" # Database name
datasets_path = "" # DataSet Path

# DataSets Path
features_file_path = ""
sales_file_path = ""
stores_file_path = ""

# Dictionary with DataSets Names
dict_datasets = {}


tables = [] # List of DataFrames
table_names = [] # Name of Tables

# Setup all variables
def setup():
    global table_names
    datasets_path = "../datasets/"
    
    # Define file paths en un Diccionario
    dict_datasets['features'] = f"{datasets_path}features_dataset.csv"
    dict_datasets['sales'] = f"{datasets_path}sales_dataset.csv"
    dict_datasets['stores'] = f"{datasets_path}stores_dataset.csv"

    table_names = list(dict_datasets.keys()) # ['stores', 'features', 'sales'] # Name of Tables


# ETL DataSets Process
def etl_process():
    # ETL Process
    global tables

    print('\nETL - DataSets process started ...')
    tables = load_datasets(dict_datasets) # Load DataSets
    datasets_description(tables) # Display DataFrames Description
    datasets_analysis(tables) # Data Analysis
    data_standarization(tables) # Data Standarization
    print('\nETL - DataSets process ended')

# Database Process
def database_import():    
    print('\nDatabase creation process started ...')
    connection, cursor = connect_to_database(database_config) # Connect to Database Management System (RDBMS)
    create_database(database_name, cursor) # Create the DataBase if Exists Drop
    n_tables = create_tables(database_name, cursor) # Create the DataBase Tables
    print(f'{n_tables} Tables created\n')
    database_loader(tables, table_names, (database_name, connection, cursor)) # All Tables Inserts
    print('\nDatabase creation process rocess ended')    

# Main Code Function
def main():
    setup()
    etl_process()
    database_import()

if __name__=="__main__":
    main()