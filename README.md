# Project Description 
  This is a project in exploration and discovery of various variables, and combinations of variables, that coincide with and could perhaps cause churn within the Telco phone/internet company. The telco data set includes features that describe the customers household and age demographics, what services they have, what their charges are, and how committed they are to remaining with the company.  
  
# Project Goal
  * discover drivers of churn
  * uncover relationships between demographics and churn
  * uncover relationships between service groups and churn
  
# Initial Thoughts
  * I initially thought that families would be less likely to churn and more likely to have services categorized as “in hand services”, as a result I thought that the “in hand services” would have a lower churn rate than “out of sight services”. My initial hypothesis is that the more “in hand services” or “out of sight” a customer has, the less likely they will be to churn, and that these service groupings would affect churn independent of one another. 
  
# The Plan
  * Acquire data from SQL via env.py file
  * Prepare data 
    *correct nulls
    * drop unnecessary columns
    * engineer columns for group exploration
  * Explore data
    * Anwer Questions: 
      1. What is the rate of churn of our customers?
      2. How does churn vary based on makeup of a household?
      3. Does churn rate vary between the two service type groups?
      4. What is the percentage breakdown of the Out of Sight Service group?
  * Develop a Model to Predict if a Customer Will Churn
    * use chosen features
    * evaluate models on train and validate data sets
    * select the best model and use the test data set
    
 # Data Dictionary
 |Term |Definition |
|:--- |:--- |
| Out of Sight Service | returns a count of how many of the add-on options online backup, online security, device protection, and tech support someone has |
|In Hand Services | returns a count of how many of the add-on service options of phone service, internet, streaming tv, streaming movies, and multiple lines a customer has |
|Single House| A household qualifies as single if the listed customer has no partner and no dependents|
|Dual House| A household qualifies as dual if the listed customer has a partner but is listed as not having dependents|
|Single Head House| A household is considered single head if the listed customer has dependents but does not have a partner|
|Family House| A household qualifies as a family house if the listed customer has a partner and dependents|

# Steps to Reproduce
  1. clone this repository
  2. Acquire data via env.py file
  3. Run the notebook
  
# Takeaways
The takeaways from this project are that categorizing household types based upon members and service groups based upon add-ons is a worthwhile venture with proper data analytics and statistical analysis. There is relationship between the engineered features and the target feature of churn. A major takeaway is this model is not conducive to determining predictors of churn. 

# Recommendations
I would recommend we explore better modeling strategies that categorize and analyze various groupings of features and testing for relationship to one another and correlation
 to churn.
