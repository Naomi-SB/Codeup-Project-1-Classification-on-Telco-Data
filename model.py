import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import sklearn.preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, ConfusionMatrixDisplay

import wrangle as w
import explore as e
   
    

################         create new dataframe with model features      #####################
    
    #train_X, validate_X, test_X, train_y, validate_y, test_y = m.final_split(model_ready_data, "churn")f
    
def model_dataframe(df):
    # building households
    df['single_house'] = (df.dependents == 'No') & (df.partner == 'No')
    df['dual_house'] = (df.dependents == 'No') & (df.partner == 'Yes')
    df['family_house'] = (df.dependents == 'Yes') & (df.partner == 'Yes')
    df['single_head_house'] = (df.dependents == 'Yes') & (df.partner == 'No')
    
    # creating focus feature
    df['ihs'] = df.streaming_movies + df.streaming_tv + df.multiple_lines + df.phone_service_Yes + df.internet

    
    # code to rename internet services to internet
    df.rename(columns = {'internet_service_type_id': 'internet'}, inplace = True)
    
    #drop columns
    
    df = df.drop(['partner', 'dependents', 'phone_service', 'multiple_lines', 'internet', 'streaming_tv', 'streaming_movies', 'monthly_charges', 'charge_bins', 'partner_Yes', 'dependents_Yes', 'phone_service_Yes', 'churn_Yes', 'ooss', 'online_backup', 'online_security', 'device_protection', 'tech_support'], axis = 1)
    
    return df

    train_X, validate_X, test_X, train_y, validate_y, test_y = m.final_split(model_ready_data, "churn")

    
    # function to split data into X_train, y_train, X_validate, y_validate, X_test, and y_test
    # this function is written to recieve model_dataframe and does not rely on the model_data function to slpit data
def final_split(df, target):
    train_X, validate_X, test_X = w.split_telco_data(df)
    
    #remember that for this project the target is churn
    train_y = train_X[target]
    validate_y = validate_X[target]
    test_y = test_X[target]
    
    #code to remove 'target' as a column
    train_X.drop(columns = target, inplace = True)
    validate_X.drop(columns = target, inplace = True)
    test_X.drop(columns = target, inplace = True)
    
    return train_X, validate_X, test_X, train_y, validate_y, test_y    
    
    
################   THIS FUNCTION TAKES IN TRAIN, VALIDATE, AND TEST DATAFRAMES AND SPLITS THEM FOR MODELING   ###############    
    
    
    
def model_data (train,validate,test):
    '''Prepare train, validate, and test data for modeling'''

    # drop unused columns 
    keep_cols = ['ooss', 'single_house', 'dual_house', 'single_head_house', 'family_house', 'churn']

    train = train[keep_cols]
    validate = validate[keep_cols]
    test = test[keep_cols]
    
    # Split data into predicting variables (X) and target variable (y) and reset the index for each dataframe
    train_X = train.drop(columns='churn').reset_index(drop=True)
    train_y = train[['churn']].reset_index(drop=True)

    validate_X = validate.drop(columns='churn').reset_index(drop=True)
    validate_y = validate[['churn']].reset_index(drop=True)

    test_X = test.drop(columns='churn').reset_index(drop=True)
    test_y = test[['churn']].reset_index(drop=True)


    return train_X, validate_X, test_X, train_y, validate_y, test_y



##################################################################
################         DECISION TREE       #####################

def decision_tree(train_X, validate_X, train_y, validate_y):
    clf = DecisionTreeClassifier(max_depth = 5, random_state = 1989)
    clf = clf.fit(train_X, train_y)
    
    print(f"Accuracy of Decision Tree statistical model on training data is {clf.score(train_X, train_y)}")
    print(f"Accuracy of Decision Tree statistical model on validation data is {clf.score(validate_X, validate_y)}")
    
##################################################################
################         RANDOM FOREST       #####################    
    
def random_forest(train_X, validate_X, train_y, validate_y):
    rf = RandomForestClassifier(max_depth = 3, random_state = 1989)
    rf = rf.fit(train_X, train_y)
    
    print(f"Accuracy of Random Forest statistical model on training data is {rf.score(train_X, train_y)}")
    print(f"Accuracy of Random Forest statistical model on validation data is {rf.score(validate_X, validate_y)}")
    

##################################################################
################     LOGISTIC REGRESSION    #####################    
    
    
def log_reg(train_X, validate_X, train_y, validate_y):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(train_X, train_y)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logit.score(train_X, train_y)}")
    print(f"Accuracy of Logistic Regression on validate is {logit.score(validate_X, validate_y)}")
    
    
##################################################################
################     LOGISTIC REGRESSION FOR TEST DATA   #####################

def log_test(test_X, test_y):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    logit = LogisticRegression(solver='liblinear')
    logit.fit(test_X, test_y)

    # print result
    print(f"Accuracy of Logistic Regression on train is {logit.score(test_X, test_y)}")
  
    
    








