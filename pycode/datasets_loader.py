## This Python Code is used to do the ETL Processes of DataSets
import pandas as pd

# Load datasets into pandas DataFrames
def load_datasets(datasets):
    '''
        Load datasets into pandas DataFrames.
        
        Input:
            datasets (dict): A dictionary with datasets path
        Return:
            (list): Returns al dataframes (or datasets)
    '''
    features_dataset = pd.read_csv(datasets['features'])
    sales_dataset = pd.read_csv(datasets['sales'])
    stores_dataset = pd.read_csv(datasets['stores'])
    
    return [features_dataset, sales_dataset,stores_dataset]


# Display the DataSets Description
def datasets_description(tables):
    '''
        Display the DataSets Description.
        
        Arguments:
            tables (list): DataFrames (datasets) objects.
    '''
    features_dataset, sales_dataset, stores_dataset = tables    
    # Display the first few rows of each dataset to ensure they are loaded correctly
    print("Features Dataset:")
    print(features_dataset.head(), "\n")
    
    print("Sales Dataset:")
    print(sales_dataset.head(), "\n")
    
    print("Stores Dataset:")
    print(stores_dataset.head(), "\n")
    
    # Check the structure of the datasets
    print("Features Dataset Info:")
    features_dataset.info()
    
    print("\nSales Dataset Info:")
    sales_dataset.info()
    
    print("\nStores Dataset Info:")
    stores_dataset.info()
    

# Display a DataSets Data Analysis
def datasets_analysis(tables):
    '''
        Display a DataSets Data Analysis.
        
        Arguments:
            tables (list): DataFrames (datasets) objects.
    '''
    features_dataset, sales_dataset, stores_dataset = tables
    # Check for duplicate rows in each dataset
    print("\nDuplicate Rows in Features Dataset:", features_dataset.duplicated().sum())
    print("Duplicate Rows in Sales Dataset:", sales_dataset.duplicated().sum())
    print("Duplicate Rows in Stores Dataset:", stores_dataset.duplicated().sum())

    print("\nMissing Values in Features Dataset:")
    print(features_dataset.isnull().sum())
    
    print("\nMissing Values in Sales Dataset:")
    print(sales_dataset.isnull().sum())
    
    print("\nMissing Values in Stores Dataset:")
    print(stores_dataset.isnull().sum())


# Set the nulls MarkDowns to 0, Check Missing Values, Convert Date Formats
def data_standarization(tables):
    '''
        DataSets Data normalization and standarization. 
        Set the nulls MarkDowns to 0, Check Missing Values, Convert Date Formats
        
        Arguments:
            tables (list): DataFrames (datasets) objects.
    '''    
    features_dataset, sales_dataset, stores_dataset = tables

    markdowns_columns = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
    # Handle missing values in MarkDown1–MarkDown5 by replacing with 0
    features_dataset[markdowns_columns] = features_dataset[markdowns_columns].fillna(0)
    
    # Handle missing values in CPI and Unemployment using forward-fill
    features_dataset['CPI'] = features_dataset['CPI'].ffill()
    features_dataset['Unemployment'] = features_dataset['Unemployment'].ffill()
    
    # Verify missing values have been handled
    print(features_dataset.isnull().sum())


    # Convert 'Date' column in Features dataset to datetime
    features_dataset['Date'] = pd.to_datetime(features_dataset['Date'], format='%d/%m/%Y')
    
    # Convert 'Date' column in Sales dataset to datetime
    sales_dataset['Date'] = pd.to_datetime(sales_dataset['Date'], format='%d/%m/%Y')
    
    # Verify the conversion
    print("\n",features_dataset['Date'].head(),"\n")
    print("\n",sales_dataset['Date'].head())



