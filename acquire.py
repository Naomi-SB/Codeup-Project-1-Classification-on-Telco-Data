import env
import pandas as pd


def new_telco_data():
    '''
    This function reads the telco data from SQL into a df.
    '''
    sql_query = """
                select * from customers
                """
    # requires env file
    df = pd.read_sql(sql_query, env.get_db_url('telco_churn'))
    
    return df

def get_telco_data():
    
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df