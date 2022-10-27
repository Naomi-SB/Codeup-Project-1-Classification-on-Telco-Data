import pandas as pd
import seaborn as sns
from pydataset import data
import numpy as np
import os
import wrangle as w

from env import get_db_url

#turn off pink warning boxes
import warnings
warnings.filterwarnings("ignore")



def get_telco_data():
    '''
    This function reads the telco data from the Codeup db into a df.
    '''
    # Create SQL query.
    sql_query = 'SELECT * FROM customers'
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_db_url('telco_churn'))
    
    return df

def get_titanic_data():
    return pd.read_sql('SELECT * FROM passengers', get_connection('titanic_db'))

def raw_telco_data():
    return pd.read_sql('SELECT * FROM customers', get_db_url('telco_churn'))