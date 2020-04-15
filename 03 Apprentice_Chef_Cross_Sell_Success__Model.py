# timeit

# Student Name : Jaisanker Venugopalan Nair
# Cohort       : 3

# Note: You are only allowed to submit ONE final model for this assignment.

# importing timeit
import timeit

 

code_to_test =  """

################################################################################
# Import Packages
################################################################################

# use this space for all of your package imports
import pandas                  as pd                             # data science essentials
import matplotlib.pyplot       as plt                            # essential graphical output
import seaborn                 as sns                            # enhanced graphical output
import numpy                   as np                             # fundamental package in python
from   sklearn.model_selection import train_test_split           # train/test split
from   sklearn.linear_model    import LogisticRegression         # Logistic Regression
from   sklearn.metrics         import roc_auc_score              # roc_auc_score


################################################################################
# Load Data
################################################################################

# use this space to load the original dataset
# MAKE SURE TO SAVE THE ORIGINAL FILE AS original_df
# Example: original_df = pd.read_excel('Apprentice Chef Dataset.xlsx')

original_df = pd.read_excel('Apprentice_Chef_Dataset.xlsx')



################################################################################
# Feature Engineering and (optional) Dataset Standardization
################################################################################

# use this space for all of the feature engineering that is required for your
# final model

# if your final model requires dataset standardization, do this here as well
# Flagging the missing values by creating a new column (missing_columnname) using a for loop
for col in original_df:
    if original_df[col].isnull().astype(int).sum() > 0:
        original_df['MISSING_'+col] = original_df[col].isnull().astype(int)

# creating an imputation value and imputing 'FAMILY_NAME'
fill = 'Unavailable'
original_df['FAMILY_NAME'] = original_df['FAMILY_NAME'].fillna(fill)

# outlier flags - LO stands for lower thresholds and *****_HI stands for Upper limits that we want to set falgs for
TOTAL_MEALS_ORDERED_LO = 10
TOTAL_MEALS_ORDERED_HI = 400

UNIQUE_MEALS_PURCH_LO = 2
UNIQUE_MEALS_PURCH_HI = 9

CONTACTS_W_CUSTOMER_SERVICE_LO = 3
CONTACTS_W_CUSTOMER_SERVICE_HI = 10

PRODUCT_CATEGORIES_VIEWED_LO = 1
PRODUCT_CATEGORIES_VIEWED_HI = 10

AVG_TIME_PER_SITE_VISIT_LO = 0
AVG_TIME_PER_SITE_VISIT_HI = 250

MOBILE_NUMBER_LO = 0 
MOBILE_NUMBER_HI = 1

CANCELLATIONS_BEFORE_NOON_LO = 0
CANCELLATIONS_BEFORE_NOON_HI = 9

CANCELLATIONS_AFTER_NOON_LO = 0
CANCELLATIONS_AFTER_NOON_HI = 3

TASTES_AND_PREFERENCES_LO = 0
TASTES_AND_PREFERENCES_HI = 1

PC_LOGINS_LO = 4.5
PC_LOGINS_HI = 6.5

MOBILE_LOGINS_LO = 0.5
MOBILE_LOGINS_HI = 2.5

WEEKLY_PLAN_LO = 0
WEEKLY_PLAN_HI = 20

EARLY_DELIVERIES_LO = 0
EARLY_DELIVERIES_HI = 5

LATE_DELIVERIES_LO = 0
LATE_DELIVERIES_HI = 10

PACKAGE_LOCKER_LO = 0
PACKAGE_LOCKER_HI = 1

REFRIGERATED_LOCKER_LO = 0
REFRIGERATED_LOCKER_HI = 1

FOLLOWED_RECOMMENDATIONS_PCT_LO = 10
FOLLOWED_RECOMMENDATIONS_PCT_HI = 35

AVG_PREP_VID_TIME_LO = 0
AVG_PREP_VID_TIME_HI = 300

LARGEST_ORDER_SIZE_LO = 2
LARGEST_ORDER_SIZE_HI = 8 #6

MASTER_CLASSES_ATTENDED_LO = 0
MASTER_CLASSES_ATTENDED_HI = 6

MEDIAN_MEAL_RATING_LO = 4.5
MEDIAN_MEAL_RATING_HI = original_df['MEDIAN_MEAL_RATING'].quantile(0.8)

AVG_CLICKS_PER_VISIT_LO = 7.5
AVG_CLICKS_PER_VISIT_HI = 17.5

TOTAL_PHOTOS_VIEWED_LO = 0
TOTAL_PHOTOS_VIEWED_HI = 450

original_df['TH_TOTAL_MEALS_ORDERED'] = 0
c_hi = original_df.loc[0:,'TH_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] > TOTAL_MEALS_ORDERED_HI]
c_lo = original_df.loc[0:,'TH_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] < TOTAL_MEALS_ORDERED_LO]
original_df['TH_TOTAL_MEALS_ORDERED'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_TOTAL_MEALS_ORDERED'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_UNIQUE_MEALS_PURCH'] = 0
c_hi = original_df.loc[0:,'TH_UNIQUE_MEALS_PURCH'][original_df['UNIQUE_MEALS_PURCH'] > UNIQUE_MEALS_PURCH_HI]
c_lo = original_df.loc[0:,'TH_UNIQUE_MEALS_PURCH'][original_df['UNIQUE_MEALS_PURCH'] < UNIQUE_MEALS_PURCH_LO]
original_df['TH_UNIQUE_MEALS_PURCH'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_UNIQUE_MEALS_PURCH'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_CONTACTS_W_CUSTOMER_SERVICE'] = 0
c_hi = original_df.loc[0:,'TH_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] > CONTACTS_W_CUSTOMER_SERVICE_HI]
c_lo = original_df.loc[0:,'TH_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] < CONTACTS_W_CUSTOMER_SERVICE_LO]
original_df['TH_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_PRODUCT_CATEGORIES_VIEWED'] = 0
c_hi = original_df.loc[0:,'TH_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] > PRODUCT_CATEGORIES_VIEWED_HI]
c_lo = original_df.loc[0:,'TH_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] < PRODUCT_CATEGORIES_VIEWED_LO]
original_df['TH_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_AVG_TIME_PER_SITE_VISIT'] = 0
c_hi = original_df.loc[0:,'TH_AVG_TIME_PER_SITE_VISIT'][original_df['AVG_TIME_PER_SITE_VISIT'] > AVG_TIME_PER_SITE_VISIT_HI]
c_lo = original_df.loc[0:,'TH_AVG_TIME_PER_SITE_VISIT'][original_df['AVG_TIME_PER_SITE_VISIT'] < AVG_TIME_PER_SITE_VISIT_LO]
original_df['TH_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_MOBILE_NUMBER'] = 0
c_hi = original_df.loc[0:,'TH_MOBILE_NUMBER'][original_df['MOBILE_NUMBER'] >= MOBILE_NUMBER_HI]
c_lo = original_df.loc[0:,'TH_MOBILE_NUMBER'][original_df['MOBILE_NUMBER'] <= MOBILE_NUMBER_LO]
original_df['TH_MOBILE_NUMBER'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_MOBILE_NUMBER'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_CANCELLATIONS_BEFORE_NOON'] = 0
c_hi = original_df.loc[0:,'TH_CANCELLATIONS_BEFORE_NOON'][original_df['CANCELLATIONS_BEFORE_NOON'] > CANCELLATIONS_BEFORE_NOON_HI]
c_lo = original_df.loc[0:,'TH_CANCELLATIONS_BEFORE_NOON'][original_df['CANCELLATIONS_BEFORE_NOON'] < CANCELLATIONS_BEFORE_NOON_LO]
original_df['TH_CANCELLATIONS_BEFORE_NOON'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_CANCELLATIONS_BEFORE_NOON'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_CANCELLATIONS_AFTER_NOON'] = 0
c_hi = original_df.loc[0:,'TH_CANCELLATIONS_AFTER_NOON'][original_df['CANCELLATIONS_AFTER_NOON'] > CANCELLATIONS_AFTER_NOON_HI]
c_lo = original_df.loc[0:,'TH_CANCELLATIONS_AFTER_NOON'][original_df['CANCELLATIONS_AFTER_NOON'] < CANCELLATIONS_AFTER_NOON_LO]
original_df['TH_CANCELLATIONS_AFTER_NOON'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_CANCELLATIONS_AFTER_NOON'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_TASTES_AND_PREFERENCES'] = 0
c_hi = original_df.loc[0:,'TH_TASTES_AND_PREFERENCES'][original_df['TASTES_AND_PREFERENCES'] > TASTES_AND_PREFERENCES_HI]
c_lo = original_df.loc[0:,'TH_TASTES_AND_PREFERENCES'][original_df['TASTES_AND_PREFERENCES'] < TASTES_AND_PREFERENCES_LO]
original_df['TH_TASTES_AND_PREFERENCES'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_TASTES_AND_PREFERENCES'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_PC_LOGINS'] = 0
c_hi = original_df.loc[0:,'TH_PC_LOGINS'][original_df['PC_LOGINS'] > PC_LOGINS_HI]
c_lo = original_df.loc[0:,'TH_PC_LOGINS'][original_df['PC_LOGINS'] < PC_LOGINS_LO]
original_df['TH_PC_LOGINS'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_PC_LOGINS'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_MOBILE_LOGINS'] = 0
c_hi = original_df.loc[0:,'TH_MOBILE_LOGINS'][original_df['MOBILE_LOGINS'] > MOBILE_LOGINS_HI]
c_lo = original_df.loc[0:,'TH_MOBILE_LOGINS'][original_df['MOBILE_LOGINS'] < MOBILE_LOGINS_LO]
original_df['TH_MOBILE_LOGINS'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_MOBILE_LOGINS'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_WEEKLY_PLAN'] = 0
c_hi = original_df.loc[0:,'TH_WEEKLY_PLAN'][original_df['WEEKLY_PLAN'] > WEEKLY_PLAN_HI]
c_lo = original_df.loc[0:,'TH_WEEKLY_PLAN'][original_df['WEEKLY_PLAN'] < WEEKLY_PLAN_LO]
original_df['TH_WEEKLY_PLAN'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_WEEKLY_PLAN'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_EARLY_DELIVERIES'] = 0
c_hi = original_df.loc[0:,'TH_EARLY_DELIVERIES'][original_df['EARLY_DELIVERIES'] > EARLY_DELIVERIES_HI]
c_lo = original_df.loc[0:,'TH_EARLY_DELIVERIES'][original_df['EARLY_DELIVERIES'] < EARLY_DELIVERIES_LO]
original_df['TH_EARLY_DELIVERIES'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_EARLY_DELIVERIES'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_LATE_DELIVERIES'] = 0
c_hi = original_df.loc[0:,'TH_LATE_DELIVERIES'][original_df['LATE_DELIVERIES'] > LATE_DELIVERIES_HI]
c_lo = original_df.loc[0:,'TH_LATE_DELIVERIES'][original_df['LATE_DELIVERIES'] < LATE_DELIVERIES_LO]
original_df['TH_LATE_DELIVERIES'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_LATE_DELIVERIES'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_PACKAGE_LOCKER'] = 0
c_hi = original_df.loc[0:,'TH_PACKAGE_LOCKER'][original_df['PACKAGE_LOCKER'] >= PACKAGE_LOCKER_HI]
c_lo = original_df.loc[0:,'TH_PACKAGE_LOCKER'][original_df['PACKAGE_LOCKER'] <= PACKAGE_LOCKER_LO]
original_df['TH_PACKAGE_LOCKER'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_PACKAGE_LOCKER'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_REFRIGERATED_LOCKER'] = 0
c_hi = original_df.loc[0:,'TH_REFRIGERATED_LOCKER'][original_df['REFRIGERATED_LOCKER'] >= REFRIGERATED_LOCKER_HI]
c_lo = original_df.loc[0:,'TH_REFRIGERATED_LOCKER'][original_df['REFRIGERATED_LOCKER'] <= REFRIGERATED_LOCKER_LO]
original_df['TH_REFRIGERATED_LOCKER'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_REFRIGERATED_LOCKER'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_FOLLOWED_RECOMMENDATIONS_PCT'] = 0
c_hi = original_df.loc[0:,'TH_FOLLOWED_RECOMMENDATIONS_PCT'][original_df['FOLLOWED_RECOMMENDATIONS_PCT'] > FOLLOWED_RECOMMENDATIONS_PCT_HI]
c_lo = original_df.loc[0:,'TH_FOLLOWED_RECOMMENDATIONS_PCT'][original_df['FOLLOWED_RECOMMENDATIONS_PCT'] < FOLLOWED_RECOMMENDATIONS_PCT_LO]
original_df['TH_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_AVG_PREP_VID_TIME'] = 0
c_hi = original_df.loc[0:,'TH_AVG_PREP_VID_TIME'][original_df['AVG_PREP_VID_TIME'] > AVG_PREP_VID_TIME_HI]
c_lo = original_df.loc[0:,'TH_AVG_PREP_VID_TIME'][original_df['AVG_PREP_VID_TIME'] < AVG_PREP_VID_TIME_LO]
original_df['TH_AVG_PREP_VID_TIME'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_AVG_PREP_VID_TIME'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_LARGEST_ORDER_SIZE'] = 0
c_hi = original_df.loc[0:,'TH_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] > LARGEST_ORDER_SIZE_HI]
c_lo = original_df.loc[0:,'TH_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] < LARGEST_ORDER_SIZE_LO]
original_df['TH_LARGEST_ORDER_SIZE'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_LARGEST_ORDER_SIZE'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_MASTER_CLASSES_ATTENDED'] = 0
c_hi = original_df.loc[0:,'TH_MASTER_CLASSES_ATTENDED'][original_df['MASTER_CLASSES_ATTENDED'] > MASTER_CLASSES_ATTENDED_HI]
c_lo = original_df.loc[0:,'TH_MASTER_CLASSES_ATTENDED'][original_df['MASTER_CLASSES_ATTENDED'] < MASTER_CLASSES_ATTENDED_LO]
original_df['TH_MASTER_CLASSES_ATTENDED'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_MASTER_CLASSES_ATTENDED'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_MEDIAN_MEAL_RATING'] = 0
c_hi = original_df.loc[0:,'TH_MEDIAN_MEAL_RATING'][original_df['MEDIAN_MEAL_RATING'] > MEDIAN_MEAL_RATING_HI]
c_lo = original_df.loc[0:,'TH_MEDIAN_MEAL_RATING'][original_df['MEDIAN_MEAL_RATING'] < MEDIAN_MEAL_RATING_LO]
original_df['TH_MEDIAN_MEAL_RATING'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_MEDIAN_MEAL_RATING'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_AVG_CLICKS_PER_VISIT'] = 0
c_hi = original_df.loc[0:,'TH_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] > AVG_CLICKS_PER_VISIT_HI]
c_lo = original_df.loc[0:,'TH_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] < AVG_CLICKS_PER_VISIT_LO]
original_df['TH_AVG_CLICKS_PER_VISIT'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_AVG_CLICKS_PER_VISIT'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['TH_TOTAL_PHOTOS_VIEWED'] = 0
c_hi = original_df.loc[0:,'TH_TOTAL_PHOTOS_VIEWED'][original_df['TOTAL_PHOTOS_VIEWED'] > TOTAL_PHOTOS_VIEWED_HI]
c_lo = original_df.loc[0:,'TH_TOTAL_PHOTOS_VIEWED'][original_df['TOTAL_PHOTOS_VIEWED'] < TOTAL_PHOTOS_VIEWED_LO]
original_df['TH_TOTAL_PHOTOS_VIEWED'].replace(to_replace = c_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['TH_TOTAL_PHOTOS_VIEWED'].replace(to_replace = c_lo,
                                    value      = 1,
                                    inplace    = True)

# seperating email domain and name
email_list = []

# looping over each email address
for index, col in original_df.iterrows():
    
    # splitting email domain at '@'
    email_split = original_df.loc[index, 'EMAIL'].split(sep = '@')
    
    # appending email_lst with the results
    email_list.append(email_split)
    

# converting email_lst into a DataFrame 
email_df = pd.DataFrame(email_list)


# STEP 2: concatenating with original DataFrame

# # safety measure in case of multiple concatenations
# original_df = pd.read_excel("Apprentice_Chef_Dataset.xlsx")

# renaming column to concatenate
# print(email_df.columns )
email_df.columns = ['ID', 'EMAIL_DOMAIN']


# concatenating personal_email_domain with friends DataFrame
original_df = pd.concat([original_df, email_df.loc[:,'EMAIL_DOMAIN']],
                   axis = 1)


# printing value counts of personal_email_domain
# original_df.loc[: ,'email_domain'].value_counts()

# email domain types
professional_email_domains = ['@mmm.com','@amex.com','@apple.com','@boeing.com',
                              '@caterpillar.com','@chevron.com','@cisco.com','@cocacola.com',
                              '@disney.com','@dupont.com','@exxon.com','@ge.org','@goldmansacs.com',
                              '@homedepot.com','@ibm.com','@intel.com','@jnj.com','@jpmorgan.com',
                              '@mcdonalds.com','@merck.com','@microsoft.com','@nike.com',
                              '@pfizer.com','@pg.com','@travelers.com','@unitedtech.com','@unitedhealth.com',
                              '@verizon.com','@visa.com','@walmart.com']
personal_email_domains     = ['@gmail.com','@yahoo.com','@protonmail.com']
junk_email_domains         = ['@me.com','@aol.com','@hotmail.com','@live.com','@msn.com','@passport.com']


# email list
email_lst = []


# looping to group observations by domain type
for domain in original_df['EMAIL_DOMAIN']:
        if '@' + domain in professional_email_domains:
            email_lst.append('PROFESSIONAL_EMAIL')
            
        elif '@' + domain in personal_email_domains:
            email_lst.append('PERSONAL_EMAIL')
            
        elif '@' + domain in junk_email_domains:
            email_lst.append('JUNK_EMAIL')
            
        else:
            print('Unknown')


# concatenating with original DataFrame
original_df['DOMAIN'] = pd.Series(email_lst)


# checking results
# original_df['DOMAIN'].value_counts()

# one hot encoding for email domain 
stat = pd.get_dummies(original_df['DOMAIN'])

original_df = original_df.join([stat])

# Creating high medium and low thresholds to prepare for one hot encoding
original_df['FOLLOWED_RECO_RANGE'] = 0

for index, val in original_df.iterrows():
    if original_df.loc[index, 'FOLLOWED_RECOMMENDATIONS_PCT'] <= 30:
        original_df.loc[index, 'FOLLOWED_RECO_RANGE'] = 'LOW_FOLLOW_PCT'
    elif original_df.loc[index, 'FOLLOWED_RECOMMENDATIONS_PCT'] > 30 and original_df.loc[index, 'FOLLOWED_RECOMMENDATIONS_PCT'] <= 75:
        original_df.loc[index, 'FOLLOWED_RECO_RANGE'] = 'MEDIUM_FOLLOW_PCT'
    else:
        original_df.loc[index, 'FOLLOWED_RECO_RANGE'] = 'HIGH_FOLLOW_PCT'

# ONE HOT ENCODING FOLLOWED RECOMMENDATIONS
stat = pd.get_dummies(original_df['FOLLOWED_RECO_RANGE'])
original_df = original_df.join([stat])

# checks if the average order for an individual is more than 23 and flags it as 1 if true and 0 otherwise

original_df['REVENUE_PER_MEAL'] = original_df['REVENUE'] / original_df['TOTAL_MEALS_ORDERED']
original_df['REV_PER_MEAL_STATUS'] = 0

for index, val in original_df.iterrows():
    if original_df.loc[index, 'REVENUE_PER_MEAL'] <= 23:
        original_df.loc[index, 'REV_PER_MEAL_STATUS'] = 'LOW_BUY'
    else :
        original_df.loc[index, 'REVENUE_PER_MEAL'] > 23 
        original_df.loc[index, 'REV_PER_MEAL_STATUS'] = 'HIGH_BUY'
        
# ONE HOT ENCODING REVENUE PER MEAL
stat = pd.get_dummies(original_df['REV_PER_MEAL_STATUS'])
original_df = original_df.join([stat])

# checks if the average order for an individual is more than 23 and flags it as 1 if true and 0 otherwise

original_df['REV_MED_FOL_PCT'] = original_df['MEDIUM_FOLLOW_PCT'] * original_df['REVENUE']
original_df['REV_MED_FOL_PCT_STATUS'] = 0

for index, val in original_df.iterrows():
    if original_df.loc[index, 'REV_MED_FOL_PCT'] <= 623:
        original_df.loc[index, 'REV_MED_FOL_PCT_STATUS'] = 'LOW_REV_MED_FOL_PCT'
    elif original_df.loc[index, 'REV_MED_FOL_PCT'] > 623 and original_df.loc[index, 'REV_MED_FOL_PCT'] <= 1188:
        original_df.loc[index, 'REV_MED_FOL_PCT_STATUS'] = 'MEDIUM_REV_MED_FOL_PCT'
    else:
        original_df.loc[index, 'REV_MED_FOL_PCT_STATUS'] = 'HIGH_REV_MED_FOL_PCT'
        
# ONE HOT ENCODING
stat = pd.get_dummies(original_df['REV_MED_FOL_PCT_STATUS'])
original_df = original_df.join([stat])

#Create a column named with weekly meals by dividing total meals bought by number of weeks
original_df['WEEKLY_MEALS'] = original_df['TOTAL_MEALS_ORDERED']/52

original_df['DISC_STATUS'] = 0
original_df['DISC_STATUS_NO'] = 0

for index, val in original_df.iterrows():
    if original_df.loc[index, 'WEEKLY_PLAN']==0:
        original_df.loc[index, 'DISC_STATUS'] = 'NO_DISC'
        original_df.loc[index, 'DISC_STATUS_NO'] = 0
    elif original_df.loc[index, 'WEEKLY_MEALS'] < 3  and original_df.loc[index, 'WEEKLY_PLAN'] > 0:
        original_df.loc[index, 'DISC_STATUS'] = 'LOW_DISC'
        original_df.loc[index, 'DISC_STATUS_NO'] = 1
    else:
        original_df.loc[index, 'DISC_STATUS'] = 'HIGH_DISC'
        original_df.loc[index, 'DISC_STATUS_NO'] = 2    
        
# ONE HOT ENCODING to seperate different types of discount groups
stat = pd.get_dummies(original_df['DISC_STATUS'])
original_df = original_df.join([stat])

#Function to split texts to words

def text_split_feature(col, df, sep=' ', new_col_name='number_of_names'):

    
    df[new_col_name] = 0
    
    
    for index, val in df.iterrows():
        df.loc[index, new_col_name] = len(df.loc[index, col].split(sep = ' '))
        
#Function call to split the names and number of names
text_split_feature(col = 'NAME',
                   df  = original_df,
                   new_col_name='NO_OF_NAMES',
                  )
original_df['NAME_STATUS'] = 0

#Setting the the threshold flags to prepare for one hot encoding
for index, val in original_df.iterrows():
    if original_df.loc[index, 'NO_OF_NAMES']<=2:
        original_df.loc[index, 'NAME_STATUS'] = 'ONE_NAME'
    else:
        original_df.loc[index, 'NAME_STATUS'] = 'MORE_NAME'

# ONE HOT ENCODING
stat = pd.get_dummies(original_df['NAME_STATUS'])
original_df = original_df.join([stat])


#creating
candidate_dict = {
# only variables with 5 percentage or above correlations 
'logit_Above_5pct'    : [   'TH_FOLLOWED_RECOMMENDATIONS_PCT'    ,
                            'FOLLOWED_RECOMMENDATIONS_PCT'       ,   
                            'HIGH_REV_MED_FOL_PCT'               ,
                            'REV_MED_FOL_PCT'                    ,
                            'HIGH_FOLLOW_PCT'                    ,
                            'PROFESSIONAL_EMAIL'                 ,
                            'CANCELLATIONS_BEFORE_NOON'          ,
                            'NO_OF_NAMES'                        ,
                            'MEDIUM_REV_MED_FOL_PCT'             ,
                            'MOBILE_NUMBER'                      ,
                            'TASTES_AND_PREFERENCES'             ,
                            'REFRIGERATED_LOCKER'                ,
                            'MOBILE_LOGINS'                      ,
                            'CANCELLATIONS_AFTER_NOON'           ,
                            'LOW_REV_MED_FOL_PCT'                ,
                            'LOW_FOLLOW_PCT'                     ,
                        ]
     }
y_variables = ['CROSS_SELL_SUCCESS']

original_df_data   =  original_df.loc[:,candidate_dict['logit_Above_5pct']]
original_df_target =  original_df.loc[:, y_variables]


################################################################################
# Train/Test Split
################################################################################

# use this space to set up testing and validation sets using train/test split

# Note: Be sure to set test_size = 0.25


X_train, X_test, y_train, y_test = train_test_split(original_df_data, original_df_target,
                                                   test_size = 0.25, 
                                                   random_state = 222,
                                                   stratify = original_df_target)



################################################################################
# Final Model (instantiate, fit, and predict)
################################################################################

# use this space to instantiate, fit, and predict on your final model
# prediction model
logreg = LogisticRegression(solver       = 'lbfgs',
                            random_state = 222,
                            C            = 1,
                            warm_start   = True,
                            max_iter     = 5000
                     )

logreg.fit(X_train, y_train)

logreg_pred = logreg.predict(X_test)

print('Training Score   : ', logreg.score(X_train, y_train).round(3))
print('Testing Score    : ', logreg.score(X_test, y_test).round(3))
print('AUC Score        : ', roc_auc_score(y_true  = y_test, 
                                           y_score = logreg_pred).round(3))




################################################################################
# Final Model Score (score)
################################################################################

# use this space to score your final model on the testing set
# MAKE SURE TO SAVE YOUR TEST SCORE AS test_score
# Example: test_score = final_model.score(X_test, y_test)

test_score = roc_auc_score(y_true  = y_test, 
                           y_score = logreg_pred).round(3)


print('Training Score   : ', logreg.score(X_train, y_train).round(3))
print('Testing Score    : ', logreg.score(X_test, y_test).round(3))
print('AUC Score        : ', roc_auc_score(y_true  = y_test, 
                                           y_score = logreg_pred).round(3))

"""

 

# calculating execution time
elapsed_time = timeit.timeit(code_to_test, number=3)/3
print(elapsed_time)

