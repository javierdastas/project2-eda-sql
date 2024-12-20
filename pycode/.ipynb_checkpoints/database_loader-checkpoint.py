import pandas as pd
import pymysql


# Conneto to DataBase Management System (RDBMS)
def connect_to_database(db_config):
    '''
        Stablish the DataBase Management System (RDBMS) connection.
        Arguments:
            db_config (dict): DataBase (RDBMS) access information.
        Return:
            (list) : Return a list with the connection (cnx) object and the cursor object related with the RDBMS.
    '''
    cnx = pymysql.connect(user=db_config['user'], password=db_config['pwd'], host=db_config['server']) # Authentication
    if cnx.open: # Check if the DBMS connection was realized
        print("\nRDBMS Connection open")
    else:
        print("\nRDBMS Connection is not successfully open")

    cursor = cnx.cursor()
    return [cnx, cursor]


# Create the DataBase
def create_database(db_name, cursor):
    '''
        Create the Database.
        
        Arguments:
            db_name (str): Database Name
            cursor (obj): Database cursor
    '''        
    query = f"DROP DATABASE IF EXISTS {db_name};" # Drop the Database
    print('* Drop Database command executed.')

    query = f"CREATE DATABASE IF NOT EXISTS {db_name};" # Create the Database
    cursor.execute(query)
    print(f'* Database {db_name.upper()} created.')


# Create Tables 
def create_tables(db_name, cursor):
    '''
        Create the tables into the Database.
        
        Arguments:
            db_name (str): Database Name
            cursor (obj): Database cursor
        Returns:
            (int): Number of tables created
    '''      
    store_qry = f"""CREATE TABLE IF NOT EXISTS {db_name}.stores (
        Store INT PRIMARY KEY,
        Type VARCHAR(50) NOT NULL,
        Size INT NOT NULL
    );"""
    cursor.execute(store_qry) # Create Store Table
    print('* "stores" tables created') 

    feature_qry = f"""CREATE TABLE IF NOT EXISTS {db_name}.features (
        Store INT,
        `Date` DATE NOT NULL,
        Temperature FLOAT NOT NULL,
        Fuel_Price FLOAT NOT NULL,
        MarkDown1 FLOAT NOT NULL DEFAULT 0,
        MarkDown2 FLOAT NOT NULL DEFAULT 0,
        MarkDown3 FLOAT NOT NULL DEFAULT 0,
        MarkDown4 FLOAT NOT NULL DEFAULT 0,
        MarkDown5 FLOAT NOT NULL DEFAULT 0,
        CPI FLOAT NOT NULL DEFAULT 0,
        Unemployment FLOAT NOT NULL DEFAULT 0,
        IsHoliday VARCHAR(10),
        PRIMARY KEY (Store, Date) 
    );"""
    cursor.execute(feature_qry) # Create Feature Table
    print('* "features" tables created')

    
    sales_qry = f"""CREATE TABLE IF NOT EXISTS {db_name}.sales (
        Store INT,
        Dept INT NOT NULL,
        `Date` DATE NOT NULL,
        Weekly_Sales FLOAT NOT NULL,
        IsHoliday  VARCHAR(10),
        PRIMARY KEY (Store, Dept, Date) 
    );"""
    cursor.execute(sales_qry) # Create Feature Table
    print('* "sales" tables created')

    cursor.execute(f'SHOW TABLES in {db_name}')
    tables_in_database = cursor.fetchall()
    
    return len(tables_in_database)

# Load all DataSets Data
def database_loader(tables, table_names, db_config):
    '''
        Import all DataSets to the DataBase Tables.
        
        Arguments:
            tables (list): List of dataframes
            tables_names (list): Lista with tables names
    '''
    db_name, cnx, cursor = db_config # Set Database connection 

    # Delete all rows in tables before insert
    cursor.execute(f'delete from {db_name}.stores') # Delete all rows form Stores Table
    cursor.execute(f'delete from {db_name}.features') # Delete all rows from Features Table
    cursor.execute(f'delete from {db_name}.sales') # Delete all rows from Sales Table
    
    # Insert rows from dataframes into the tables
    for index, table in enumerate(tables):    ## Loop over tables
        columns = table.columns ## Needed to create our query as the insert into takes in the column names and the values as a parameter  
        param_1 = ", ".join(list(columns)) ## Creating the string for the list of columns
        param_2 = ("%s, " * len(columns))[:-2]  ## Creating the placeholder for the value
    
        query = f"INSERT INTO {db_name}.{table_names[index]}({param_1}) VALUES ({param_2})"
        print(f'Inserting into ... {table_names[index]}')
        
        for index, row in table.iterrows():
            cursor.execute(query, list(row))     ## Executing the query and passing the row as argument so that for each table,            

        print(f'   All Rows Inserted')
        
    cnx.commit() ## Commit al the Inserts into the DataBase
        
    if cnx.open: ## Close any pending connection or relation with the DataBase
        cursor.close()
        cnx.close()

