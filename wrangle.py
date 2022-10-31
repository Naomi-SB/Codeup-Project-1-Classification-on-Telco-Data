import pandas as pd
import seaborn as sns
from pydataset import data
import numpy as np
import os

from sklearn.model_selection import train_test_split

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

def prep_telco_data(df):


    # code that fixes white space fro total charges column
    df['total_charges']=df['total_charges'].str.strip()
    df['total_charges']=df['total_charges'].replace(' ', '')
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors = 'coerce')
   
    #code that bins monthly charges
    bins = [0, 20, 35, 50, 75, 100, 120]
    labels = ['0-20', '21-35', '36-50', '51-75', '76-100', '101-120']
    df['charge_bins'] = pd.cut(x= df['monthly_charges'], bins = bins, labels = labels, include_lowest = True)


    # code to rename internet services to internet
    df.rename(columns = {'internet_service_type_id': 'internet'}, inplace = True)
    
    # code that encodes with(yes/no/neither)
    df['multiple_lines']= df.multiple_lines.map({'Yes':1, 'No':0, 'No phone service': 0})
    df['internet'] = df.internet.map({1:1, 2:1, 3: 0})
    df['online_security'] = df.online_security.map({'Yes':1, 'No':0, 'No internet service': 0})
    df['device_protection'] = df.device_protection.map({'Yes':1, 'No':0, 'No internet service': 0})
    df['tech_support'] = df.tech_support.map({'Yes':1, 'No':0, 'No internet service': 0})
    df['streaming_tv'] = df.streaming_tv.map({'Yes':1, 'No':0, 'No internet service': 0})
    df['streaming_movies'] = df.streaming_movies.map({'Yes':1, 'No':0, 'No internet service': 0})
    df['online_backup'] = df.online_backup.map({'Yes':1, 'No':0, 'No internet service': 0})
    
    #code to create household columns
    df['single_house'] = (df.dependents == 'No') & (df.partner == 'No')
    df['dual_house'] = (df.dependents == 'No') & (df.partner == 'Yes')
    df['family_house'] = (df.dependents == 'Yes') & (df.partner == 'Yes')
    df['single_head_house'] = (df.dependents == 'Yes') & (df.partner == 'No')
    
    #code to create dummies
    dummy_df = pd.get_dummies(df[['single_house', 'dual_house', 'family_house', 'single_head_house','gender', 'partner', 'dependents', 'phone_service', 'paperless_billing', 'churn']], dummy_na = False, drop_first = True)
    df = pd.concat([df, dummy_df], axis = 1)
    
    #code to create focus features
    df['ihs'] = df.streaming_movies + df.streaming_tv + df.multiple_lines + df.phone_service_Yes + df.internet
    df['ooss'] = df.online_security + df.online_backup + df.device_protection + df.tech_support
    
    return df


# function to split data set into train, validate, test
def split_telco_data(df):

    train_validate, test_df = train_test_split(df, test_size=.2, 
                                        random_state=1989, 
                                        stratify=df.churn)
    train_df, validate_df = train_test_split(train_validate, test_size=.3, 
                                   random_state=1989, 
                                   stratify=train_validate.churn)
    
    return train_df, validate_df, test_df

# function to split data into X_train, y_train, X_validate, y_validate, X_test, and y_test
def final_split(df, target):
    X_train, X_validate, X_test = slpit_telco_data(df, target)
    
    #remember that for this project the target is churn
    y_train = train[target]
    y_validate = validate[target]
    y_test = test[target]
    
    #code to remove 'target' as a column
    train.drop(columns = target, inplace = True)
    validate.drop(columns = target, inplace = True)
    test.drop(columns = target, inplace = True)
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test




    