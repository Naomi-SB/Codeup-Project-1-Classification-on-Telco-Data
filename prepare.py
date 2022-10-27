import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

# function to split data set into train, validate, test
def split_telco_data(df):
    
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test


#function to prepare dataframe
def prep_frame(df):
    # code that fixes white space fro total charges column
    df['total_charges']=df['total_charges'].str.strip()
    df['total_charges']=df['total_charges'].replace(' ', '')
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors = 'coerce')
   
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
    
    #code to return split data
    train, validate, test = split_telco_data(df)
    
    return train, validate, test


def single_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'No')]
    return df

def dual_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'Yes')]
    return df

def family_house(df):
    f = df[(df.dependents == 'No') & (df.partner == 'Yes')]
    return df

def single_head_house(df):
    df = df[(df.dependents == 'Yes') & (df.partner == 'No')]
    return df


