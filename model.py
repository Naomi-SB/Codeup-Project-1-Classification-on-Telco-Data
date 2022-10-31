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

def churn_pie(train_df):
    
    churn = train_df[train_df.churn =='Yes']
    not_churn = train_df[train_df.churn == 'No']
    
    values = [len(churn), len(not_churn)]
    
    plt.pie(values, labels = ['churn customers', 'loyal customers'], autopct='%.2f')
    plt.title('Percentage of Customers Who Have Churned')
    plt.show()
    
    
def household_type_visualization(train_df):
    
    sns.set()
    fig, axes = plt.subplots(2,2)
    
    sns.histplot(data=train_df, x = "churn", hue = "single_house", ax = axes[0,0])
    sns.histplot(data=train_df, x = "churn", hue = "dual_house", ax = axes[1,0])
    sns.histplot(data=train_df, x = "churn", hue = "family_house", ax = axes[0,1])
    sns.histplot(data=train_df, x = "churn", hue = "single_head_house", ax = axes[1,1])
    
def service_group_breakdown(train_df):
    sns.set()
    fig, axes = plt.subplots(2,1)
    sns.displot(data=train_df, x="ihs", hue ="churn", ax = axes[0,1])
    sns.displot(data=train_df, x="ooss", hue ="churn", ax = axes[0,0])
    
    
def OOSS_breakdown(train_df):
    labels = ['online security', 'online backup', 'device protection', 'tech support']
    sizes = [train_df.online_security, train_df.online_backup, train_df.device_protection, train_df.tech_support]
    plt.pie(size, labels = labels)
    plt.title("Percentages of Out of Sight Services")
    plt.show()
    
    
    