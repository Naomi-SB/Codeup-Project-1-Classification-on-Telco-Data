import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
   
    
    ########################################## QUESTION ONE #################################
def churn_pie(train_df):
    
    churn = train_df[train_df.churn =='Yes']
    not_churn = train_df[train_df.churn == 'No']
    
    values = [len(churn), len(not_churn)]
    
    plt.pie(values, labels = ['churn customers', 'loyal customers'], autopct='%.2f')
    plt.title('Percentage of Customers Who Have Churned')
    plt.show()
    
   ########################################## QUESTION TWO #################################
    
    ### VIZ
def household_type_visualization(train_df):
    
    sns.set()
    plt.figure(figsize = (20,8))
    
    plt.subplot(221)
    sns.barplot(data = train_df, y = "churn_Yes", x="single_house")
    plt.title('single household')
    
    plt.subplot(222)
    sns.barplot(data = train_df, y = "churn_Yes", x="dual_house")
    plt.title('dual household')
    
    plt.subplot(223)
    sns.barplot(data = train_df, y = "churn_Yes", x="family_house")
    plt.title('family household')
    
    plt.subplot(224)
    sns.barplot(data = train_df, y = "churn_Yes", x="single_head_house")
    plt.title('sinlge head household')
    
    ### CODE
def house_ttest(df):
    alpha = 0.05
    churn_sample_single = df[df.churn == 'Yes'].single_house
    overall_churn_mean = df.churn.mean()

    t, p = stats.ttest_1samp(churn_sample_single, overall_churn_mean)
    if p/2 > alpha:
        print("We acknowledge there is no relationship")
    elif t < 0:
        print("We acknowledge there is no relationship")
    else:
        print("We acknowledge there is a relationship")

#the churn rate among single people is higher than the churn rate among the gen pop

 ########################################## QUESTION THREE #################################    
    
    ### VIZ
def service_group_breakdown(train_df):
    sns.set()
    plt.figure(figsize = (20, 8))
    
    plt.subplot(221)
    sns.barplot(data = train_df, y = "churn_Yes", x = "ihs")
    plt.title("In Hand Services")
    
    plt.subplot(222)
    sns.barplot(data = train_df, x = "ooss", y = "churn_Yes")
    plt.title("Out of Sight Services")

    ### CODE
    
    
    
########################################## QUESTION FOUR #################################
    
    ### VIZ
def OOSS_breakdown(train_df):
    
    OS = train_df[train_df.online_security == 1]
    OB = train_df[train_df.online_backup == 1]
    DP = train_df[train_df.device_protection == 1]
    TS = train_df[train_df.tech_support == 1]
    
    values = [len(OS), len(OB), len(DP), len(TS)]
    
    plt.pie(values, labels = ['online security', 'online backup', 'device protection', 'tech support'], autopct='%.2f')
    
    plt.title("Percentages of Out of Sight Services")
    plt.show()
    
    ### CODE
    
    
    
    
###################################################
    
    
def single_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'No')]
    return df

def dual_house(df):
    df = df[(df.dependents == 'No') & (df.partner == 'Yes')]
    return df

def family_house(df):
    df = df[(df.dependents == 'Yes') & (df.partner == 'Yes')]
    return df

def single_head_house(df):
    df = df[(df.dependents == 'Yes') & (df.partner == 'No')]
    return df


    