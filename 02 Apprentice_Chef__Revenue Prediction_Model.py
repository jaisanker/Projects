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
import pandas as pd                                            # data science essentials
import numpy as np                                             # fundamental package in python
from sklearn.model_selection import train_test_split           # train/test split
from sklearn.linear_model import LinearRegression              # linear regression (scikit-learn)


################################################################################
# Load Data
################################################################################

# use this space to load the original dataset
# MAKE SURE TO SAVE THE ORIGINAL FILE AS original_df
# Example: original_df = pd.read_excel('Apprentice_Chef_Dataset.xlsx')

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

#dropping the column used to create flags for missing family name
original_df = original_df.drop(labels = 'MISSING_FAMILY_NAME', axis = 1)

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

AVG_PREP_VID_TIME_LO = 0 #60
AVG_PREP_VID_TIME_HI = 300

LARGEST_ORDER_SIZE_LO = 2
LARGEST_ORDER_SIZE_HI = 8 #6

MASTER_CLASSES_ATTENDED_LO = 0
MASTER_CLASSES_ATTENDED_HI = 6 #2

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

TOTAL_MEALS_ORDERED_CHG_LO = 50
TOTAL_MEALS_ORDERED_CHG_HI = 350

UNIQUE_MEALS_PURCH_CHG_LO = 1
UNIQUE_MEALS_PURCH_CHG_HI = 10

CONTACTS_W_CUSTOMER_SERVICE_CHG_LO = 0
CONTACTS_W_CUSTOMER_SERVICE_CHG_HI = 10

PRODUCT_CATEGORIES_VIEWED_CHG_LO = 0
PRODUCT_CATEGORIES_VIEWED_CHG_HI = 10

AVG_TIME_PER_SITE_VISIT_CHG_LO = 0
AVG_TIME_PER_SITE_VISIT_CHG_HI = 300 

MOBILE_NUMBER_CHG_LO = 0
MOBILE_NUMBER_CHG_HI = 1

CANCELLATIONS_BEFORE_NOON_CHG_LO = 2
CANCELLATIONS_BEFORE_NOON_CHG_HI = 8

CANCELLATIONS_AFTER_NOON_CHG_LO = original_df['CANCELLATIONS_AFTER_NOON'].quantile(0.2)
CANCELLATIONS_AFTER_NOON_CHG_HI = original_df['CANCELLATIONS_AFTER_NOON'].quantile(0.8)

TASTES_AND_PREFERENCES_CHG_LO = original_df['TASTES_AND_PREFERENCES'].quantile(0.2)
TASTES_AND_PREFERENCES_CHG_HI = original_df['TASTES_AND_PREFERENCES'].quantile(0.8)

PC_LOGINS_CHG_LO = original_df['PC_LOGINS'].quantile(0.2)
PC_LOGINS_CHG_HI = original_df['PC_LOGINS'].quantile(0.8)

MOBILE_LOGINS_CHG_LO = original_df['MOBILE_LOGINS'].quantile(0.25)
MOBILE_LOGINS_CHG_HI = original_df['MOBILE_LOGINS'].quantile(0.75)

WEEKLY_PLAN_CHG_LO = 0
WEEKLY_PLAN_CHG_HI = 50 #40

EARLY_DELIVERIES_CHG_LO = 0
EARLY_DELIVERIES_CHG_HI = 6

LATE_DELIVERIES_CHG_LO = 0
LATE_DELIVERIES_CHG_HI = 7.5

PACKAGE_LOCKER_CHG_LO = 0
PACKAGE_LOCKER_CHG_HI = 1

REFRIGERATED_LOCKER_CHG_LO = original_df['REFRIGERATED_LOCKER'].quantile(0.25)
REFRIGERATED_LOCKER_CHG_HI = original_df['REFRIGERATED_LOCKER'].quantile(0.75)

FOLLOWED_RECOMMENDATIONS_PCT_CHG_LO = 0
FOLLOWED_RECOMMENDATIONS_PCT_CHG_HI = 60 #40 55 - 70

AVG_PREP_VID_TIME_CHG_LO = 50 #0
AVG_PREP_VID_TIME_CHG_HI = 200

LARGEST_ORDER_SIZE_CHG_LO = 0
LARGEST_ORDER_SIZE_CHG_HI = 10

MASTER_CLASSES_ATTENDED_CHG_LO = original_df['MASTER_CLASSES_ATTENDED'].quantile(0.25)
MASTER_CLASSES_ATTENDED_CHG_HI = original_df['MASTER_CLASSES_ATTENDED'].quantile(0.75)

MEDIAN_MEAL_RATING_CHG_LO = 0
MEDIAN_MEAL_RATING_CHG_HI = 4

AVG_CLICKS_PER_VISIT_CHG_LO = 6 #6
AVG_CLICKS_PER_VISIT_CHG_HI = 18

TOTAL_PHOTOS_VIEWED_CHG_LO = 0
TOTAL_PHOTOS_VIEWED_CHG_HI = 1000 #200

original_df['CHG_TOTAL_MEALS_ORDERED'] = 0
ch_hi = original_df.loc[0:,'CHG_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] > TOTAL_MEALS_ORDERED_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_TOTAL_MEALS_ORDERED'][original_df['TOTAL_MEALS_ORDERED'] < TOTAL_MEALS_ORDERED_CHG_LO]
original_df['CHG_TOTAL_MEALS_ORDERED'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_TOTAL_MEALS_ORDERED'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_UNIQUE_MEALS_PURCH'] = 0
ch_hi = original_df.loc[0:,'CHG_UNIQUE_MEALS_PURCH'][original_df['UNIQUE_MEALS_PURCH'] > UNIQUE_MEALS_PURCH_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_UNIQUE_MEALS_PURCH'][original_df['UNIQUE_MEALS_PURCH'] < UNIQUE_MEALS_PURCH_CHG_LO]
original_df['CHG_UNIQUE_MEALS_PURCH'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_UNIQUE_MEALS_PURCH'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_CONTACTS_W_CUSTOMER_SERVICE'] = 0
ch_hi = original_df.loc[0:,'CHG_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] > CONTACTS_W_CUSTOMER_SERVICE_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_CONTACTS_W_CUSTOMER_SERVICE'][original_df['CONTACTS_W_CUSTOMER_SERVICE'] < CONTACTS_W_CUSTOMER_SERVICE_CHG_LO]
original_df['CHG_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_CONTACTS_W_CUSTOMER_SERVICE'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_PRODUCT_CATEGORIES_VIEWED'] = 0
ch_hi = original_df.loc[0:,'CHG_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] > PRODUCT_CATEGORIES_VIEWED_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_PRODUCT_CATEGORIES_VIEWED'][original_df['PRODUCT_CATEGORIES_VIEWED'] < PRODUCT_CATEGORIES_VIEWED_CHG_LO]
original_df['CHG_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_PRODUCT_CATEGORIES_VIEWED'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_AVG_TIME_PER_SITE_VISIT'] = 0
ch_hi = original_df.loc[0:,'CHG_AVG_TIME_PER_SITE_VISIT'][original_df['AVG_TIME_PER_SITE_VISIT'] > AVG_TIME_PER_SITE_VISIT_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_AVG_TIME_PER_SITE_VISIT'][original_df['AVG_TIME_PER_SITE_VISIT'] < AVG_TIME_PER_SITE_VISIT_CHG_LO]
original_df['CHG_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_AVG_TIME_PER_SITE_VISIT'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_MOBILE_NUMBER'] = 0
ch_hi = original_df.loc[0:,'CHG_MOBILE_NUMBER'][original_df['MOBILE_NUMBER'] > MOBILE_NUMBER_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_MOBILE_NUMBER'][original_df['MOBILE_NUMBER'] < MOBILE_NUMBER_CHG_LO]
original_df['CHG_MOBILE_NUMBER'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_MOBILE_NUMBER'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_CANCELLATIONS_BEFORE_NOON'] = 0
ch_hi = original_df.loc[0:,'CHG_CANCELLATIONS_BEFORE_NOON'][original_df['CANCELLATIONS_BEFORE_NOON'] > CANCELLATIONS_BEFORE_NOON_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_CANCELLATIONS_BEFORE_NOON'][original_df['CANCELLATIONS_BEFORE_NOON'] < CANCELLATIONS_BEFORE_NOON_CHG_LO]
original_df['CHG_CANCELLATIONS_BEFORE_NOON'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_CANCELLATIONS_BEFORE_NOON'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_CANCELLATIONS_AFTER_NOON'] = 0
ch_hi = original_df.loc[0:,'CHG_CANCELLATIONS_AFTER_NOON'][original_df['CANCELLATIONS_AFTER_NOON'] > CANCELLATIONS_AFTER_NOON_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_CANCELLATIONS_AFTER_NOON'][original_df['CANCELLATIONS_AFTER_NOON'] < CANCELLATIONS_AFTER_NOON_CHG_LO]
original_df['CHG_CANCELLATIONS_AFTER_NOON'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_CANCELLATIONS_AFTER_NOON'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_TASTES_AND_PREFERENCES'] = 0
ch_hi = original_df.loc[0:,'CHG_TASTES_AND_PREFERENCES'][original_df['TASTES_AND_PREFERENCES'] > TASTES_AND_PREFERENCES_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_TASTES_AND_PREFERENCES'][original_df['TASTES_AND_PREFERENCES'] < TASTES_AND_PREFERENCES_CHG_LO]
original_df['CHG_TASTES_AND_PREFERENCES'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_TASTES_AND_PREFERENCES'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_PC_LOGINS'] = 0
ch_hi = original_df.loc[0:,'CHG_PC_LOGINS'][original_df['PC_LOGINS'] > PC_LOGINS_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_PC_LOGINS'][original_df['PC_LOGINS'] < PC_LOGINS_CHG_LO]
original_df['CHG_PC_LOGINS'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_PC_LOGINS'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_MOBILE_LOGINS'] = 0
ch_hi = original_df.loc[0:,'CHG_MOBILE_LOGINS'][original_df['MOBILE_LOGINS'] > MOBILE_LOGINS_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_MOBILE_LOGINS'][original_df['MOBILE_LOGINS'] < MOBILE_LOGINS_CHG_LO]
original_df['CHG_MOBILE_LOGINS'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_MOBILE_LOGINS'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_WEEKLY_PLAN'] = 0
ch_hi = original_df.loc[0:,'CHG_WEEKLY_PLAN'][original_df['WEEKLY_PLAN'] > WEEKLY_PLAN_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_WEEKLY_PLAN'][original_df['WEEKLY_PLAN'] < WEEKLY_PLAN_CHG_LO]
original_df['CHG_WEEKLY_PLAN'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_WEEKLY_PLAN'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_EARLY_DELIVERIES'] = 0
ch_hi = original_df.loc[0:,'CHG_EARLY_DELIVERIES'][original_df['EARLY_DELIVERIES'] > EARLY_DELIVERIES_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_EARLY_DELIVERIES'][original_df['EARLY_DELIVERIES'] < EARLY_DELIVERIES_CHG_LO]
original_df['CHG_EARLY_DELIVERIES'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_EARLY_DELIVERIES'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_LATE_DELIVERIES'] = 0
ch_hi = original_df.loc[0:,'CHG_LATE_DELIVERIES'][original_df['LATE_DELIVERIES'] > LATE_DELIVERIES_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_LATE_DELIVERIES'][original_df['LATE_DELIVERIES'] < LATE_DELIVERIES_CHG_LO]
original_df['CHG_LATE_DELIVERIES'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_LATE_DELIVERIES'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_PACKAGE_LOCKER'] = 0
ch_hi = original_df.loc[0:,'CHG_PACKAGE_LOCKER'][original_df['PACKAGE_LOCKER'] > PACKAGE_LOCKER_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_PACKAGE_LOCKER'][original_df['PACKAGE_LOCKER'] < PACKAGE_LOCKER_CHG_LO]
original_df['CHG_PACKAGE_LOCKER'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_PACKAGE_LOCKER'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_REFRIGERATED_LOCKER'] = 0
ch_hi = original_df.loc[0:,'CHG_REFRIGERATED_LOCKER'][original_df['REFRIGERATED_LOCKER'] > REFRIGERATED_LOCKER_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_REFRIGERATED_LOCKER'][original_df['REFRIGERATED_LOCKER'] < REFRIGERATED_LOCKER_CHG_LO]
original_df['CHG_REFRIGERATED_LOCKER'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_REFRIGERATED_LOCKER'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_FOLLOWED_RECOMMENDATIONS_PCT'] = 0
ch_hi = original_df.loc[0:,'CHG_FOLLOWED_RECOMMENDATIONS_PCT'][original_df['FOLLOWED_RECOMMENDATIONS_PCT'] > FOLLOWED_RECOMMENDATIONS_PCT_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_FOLLOWED_RECOMMENDATIONS_PCT'][original_df['FOLLOWED_RECOMMENDATIONS_PCT'] < FOLLOWED_RECOMMENDATIONS_PCT_CHG_LO]
original_df['CHG_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_FOLLOWED_RECOMMENDATIONS_PCT'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_AVG_PREP_VID_TIME'] = 0
ch_hi = original_df.loc[0:,'CHG_AVG_PREP_VID_TIME'][original_df['AVG_PREP_VID_TIME'] > AVG_PREP_VID_TIME_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_AVG_PREP_VID_TIME'][original_df['AVG_PREP_VID_TIME'] < AVG_PREP_VID_TIME_CHG_LO]
original_df['CHG_AVG_PREP_VID_TIME'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_AVG_PREP_VID_TIME'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_LARGEST_ORDER_SIZE'] = 0
ch_hi = original_df.loc[0:,'CHG_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] > LARGEST_ORDER_SIZE_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_LARGEST_ORDER_SIZE'][original_df['LARGEST_ORDER_SIZE'] < LARGEST_ORDER_SIZE_CHG_LO]
original_df['CHG_LARGEST_ORDER_SIZE'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_LARGEST_ORDER_SIZE'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_MASTER_CLASSES_ATTENDED'] = 0
ch_hi = original_df.loc[0:,'CHG_MASTER_CLASSES_ATTENDED'][original_df['MASTER_CLASSES_ATTENDED'] > MASTER_CLASSES_ATTENDED_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_MASTER_CLASSES_ATTENDED'][original_df['MASTER_CLASSES_ATTENDED'] < MASTER_CLASSES_ATTENDED_CHG_LO]
original_df['CHG_MASTER_CLASSES_ATTENDED'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_MASTER_CLASSES_ATTENDED'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_MEDIAN_MEAL_RATING'] = 0
ch_hi = original_df.loc[0:,'CHG_MEDIAN_MEAL_RATING'][original_df['MEDIAN_MEAL_RATING'] > MEDIAN_MEAL_RATING_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_MEDIAN_MEAL_RATING'][original_df['MEDIAN_MEAL_RATING'] < MEDIAN_MEAL_RATING_CHG_LO]
original_df['CHG_MEDIAN_MEAL_RATING'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_MEDIAN_MEAL_RATING'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_AVG_CLICKS_PER_VISIT'] = 0
ch_hi = original_df.loc[0:,'CHG_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] > AVG_CLICKS_PER_VISIT_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_AVG_CLICKS_PER_VISIT'][original_df['AVG_CLICKS_PER_VISIT'] < AVG_CLICKS_PER_VISIT_CHG_LO]
original_df['CHG_AVG_CLICKS_PER_VISIT'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_AVG_CLICKS_PER_VISIT'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['CHG_TOTAL_PHOTOS_VIEWED'] = 0
ch_hi = original_df.loc[0:,'CHG_TOTAL_PHOTOS_VIEWED'][original_df['TOTAL_PHOTOS_VIEWED'] > TOTAL_PHOTOS_VIEWED_CHG_HI]
ch_lo = original_df.loc[0:,'CHG_TOTAL_PHOTOS_VIEWED'][original_df['TOTAL_PHOTOS_VIEWED'] < TOTAL_PHOTOS_VIEWED_CHG_LO]
original_df['CHG_TOTAL_PHOTOS_VIEWED'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)
original_df['CHG_TOTAL_PHOTOS_VIEWED'].replace(to_replace = ch_lo,
                                    value      = 1,
                                    inplace    = True)

original_df['APVT_MMR'] = original_df['AVG_PREP_VID_TIME']*original_df['MEDIAN_MEAL_RATING']
original_df['TTM_APVT'] = original_df['TOTAL_MEALS_ORDERED']*original_df['AVG_PREP_VID_TIME']
original_df['APVT_ACPR'] = original_df['AVG_PREP_VID_TIME']*original_df['AVG_CLICKS_PER_VISIT']
original_df['MMR_TTM'] = original_df['MEDIAN_MEAL_RATING']*original_df['TOTAL_MEALS_ORDERED']
original_df['APVT_MMR_TTM'] = original_df['APVT_MMR']*original_df['TTM_APVT']
original_df['APVT_TPV'] = original_df['AVG_PREP_VID_TIME']*original_df['TOTAL_PHOTOS_VIEWED']
original_df['TPV_ACPR'] = original_df['TOTAL_PHOTOS_VIEWED']*original_df['AVG_CLICKS_PER_VISIT']

original_df['D_APVT_MMR'] = original_df['AVG_PREP_VID_TIME']/original_df['MEDIAN_MEAL_RATING']
original_df['D_MMR_TTM'] = original_df['MEDIAN_MEAL_RATING']/original_df['TOTAL_MEALS_ORDERED']
original_df['TMO_UMP'] = original_df['TOTAL_MEALS_ORDERED']/original_df['UNIQUE_MEALS_PURCH']
original_df['D_TTM_APVT'] = original_df['TOTAL_MEALS_ORDERED']/original_df['AVG_PREP_VID_TIME']
original_df['OOV'] = original_df['UNIQUE_MEALS_PURCH'] / original_df['PRODUCT_CATEGORIES_VIEWED']

# checks if the average order for an individual is more than 23 and flags it as 1 if true and 0 otherwise
original_df['REVENUE_PER_MEAL'] = original_df['REVENUE'] / original_df['TOTAL_MEALS_ORDERED']

original_df['HIGH_BUY'] = 0
ch_hi = original_df.loc[0:,'HIGH_BUY'][original_df['REVENUE_PER_MEAL'] >= 23]

original_df['HIGH_BUY'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)

# checks if the average ratio of customer spending to rating for an individual is more than 34 and flags it as 1 if true and 0 otherwise
original_df['RATING_CUSTOMER'] = original_df['REVENUE'] / original_df['MEDIAN_MEAL_RATING']
original_df['HIGH_RATING'] = 0
ch_hi = original_df.loc[0:,'HIGH_RATING'][original_df['RATING_CUSTOMER'] >= 34]

original_df['HIGH_RATING'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)

original_df['CLICKTOREV'] = original_df['REVENUE'] / original_df['AVG_CLICKS_PER_VISIT']
original_df['HIGHCLICKTOREV'] = 0
ch_hi = original_df.loc[0:,'HIGHCLICKTOREV'][original_df['CLICKTOREV'] >= 90]

original_df['HIGHCLICKTOREV'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)

original_df['REV_AVG_VID'] = original_df['REVENUE'] / original_df['AVG_PREP_VID_TIME']
original_df['RATIO_REV_VID_TIME'] = 0
ch_hi = original_df.loc[0:,'RATIO_REV_VID_TIME'][original_df['REV_AVG_VID'] >= 23]

original_df['RATIO_REV_VID_TIME'].replace(to_replace = ch_hi,
                                    value      = 1,
                                    inplace    = True)

X_variables_1 = ['APVT_MMR','TTM_APVT','APVT_ACPR','MMR_TTM','APVT_MMR_TTM', 'APVT_TPV', 'TPV_ACPR',
                 'D_APVT_MMR','D_MMR_TTM','TMO_UMP','D_TTM_APVT','OOV',
                  'HIGH_BUY','HIGH_RATING','HIGHCLICKTOREV','RATIO_REV_VID_TIME',
                 'TOTAL_MEALS_ORDERED', 'UNIQUE_MEALS_PURCH', 'CONTACTS_W_CUSTOMER_SERVICE', 
                 'PRODUCT_CATEGORIES_VIEWED', 'AVG_TIME_PER_SITE_VISIT', 'MOBILE_NUMBER', 
                 'CANCELLATIONS_BEFORE_NOON', 'CANCELLATIONS_AFTER_NOON', 'TASTES_AND_PREFERENCES', 
                 'PC_LOGINS', 'MOBILE_LOGINS', 'WEEKLY_PLAN', 'EARLY_DELIVERIES', 'LATE_DELIVERIES', 
                 'PACKAGE_LOCKER', 'REFRIGERATED_LOCKER', 'FOLLOWED_RECOMMENDATIONS_PCT', 'AVG_PREP_VID_TIME', 
                 'LARGEST_ORDER_SIZE', 'MASTER_CLASSES_ATTENDED', 'MEDIAN_MEAL_RATING', 'AVG_CLICKS_PER_VISIT',
                 'TOTAL_PHOTOS_VIEWED', 'TH_TOTAL_MEALS_ORDERED', 'TH_UNIQUE_MEALS_PURCH', 
                 'TH_CONTACTS_W_CUSTOMER_SERVICE', 'TH_PRODUCT_CATEGORIES_VIEWED', 
                 'TH_AVG_TIME_PER_SITE_VISIT', 'TH_MOBILE_NUMBER', 'TH_CANCELLATIONS_BEFORE_NOON', 
                 'TH_CANCELLATIONS_AFTER_NOON', 'TH_TASTES_AND_PREFERENCES', 'TH_PC_LOGINS', 
                 'TH_MOBILE_LOGINS', 'TH_WEEKLY_PLAN', 'TH_EARLY_DELIVERIES', 'TH_LATE_DELIVERIES', 
                 'TH_PACKAGE_LOCKER','TH_REFRIGERATED_LOCKER', 'TH_FOLLOWED_RECOMMENDATIONS_PCT', 
                 'TH_AVG_PREP_VID_TIME', 'TH_LARGEST_ORDER_SIZE', 'TH_MASTER_CLASSES_ATTENDED', 
                 'TH_MEDIAN_MEAL_RATING', 'TH_AVG_CLICKS_PER_VISIT', 'TH_TOTAL_PHOTOS_VIEWED', 
                 'CHG_TOTAL_MEALS_ORDERED', 'CHG_UNIQUE_MEALS_PURCH', 'CHG_CONTACTS_W_CUSTOMER_SERVICE', 
                 'CHG_PRODUCT_CATEGORIES_VIEWED', 'CHG_AVG_TIME_PER_SITE_VISIT', 'CHG_MOBILE_NUMBER', 
                 'CHG_CANCELLATIONS_BEFORE_NOON', 'CHG_CANCELLATIONS_AFTER_NOON', 'CHG_TASTES_AND_PREFERENCES', 
                 'CHG_PC_LOGINS', 'CHG_MOBILE_LOGINS', 'CHG_WEEKLY_PLAN', 'CHG_EARLY_DELIVERIES', 
                 'CHG_LATE_DELIVERIES', 'CHG_PACKAGE_LOCKER', 'CHG_REFRIGERATED_LOCKER', 
                 'CHG_FOLLOWED_RECOMMENDATIONS_PCT', 'CHG_AVG_PREP_VID_TIME', 'CHG_LARGEST_ORDER_SIZE', 
                 'CHG_MASTER_CLASSES_ATTENDED', 'CHG_MEDIAN_MEAL_RATING', 'CHG_AVG_CLICKS_PER_VISIT', 
                 'CHG_TOTAL_PHOTOS_VIEWED']


y_variables_1 = ['REVENUE']

original_df_data   = original_df.loc[ : , X_variables_1]

original_df_target = original_df.loc[ : , y_variables_1]




################################################################################
# Train/Test Split
################################################################################

# use this space to set up testing and validation sets using train/test split

# Note: Be sure to set test_size = 0.25

# train-test split
X_train, X_test, y_train, y_test = train_test_split(original_df_data,original_df_target ,
                                                   test_size = 0.25, 
                                                   random_state = 222 )




################################################################################
# Final Model (instantiate, fit, and predict)
################################################################################

# use this space to instantiate, fit, and predict on your final model

lr = LinearRegression()

lr_fit = lr.fit(X_train, y_train)
lr_pred = lr_fit.predict(X_test)



################################################################################
# Final Model Score (score)
################################################################################

# use this space to score your final model on the testing set
# MAKE SURE TO SAVE YOUR TEST SCORE AS test_score
# Example: test_score = final_model.score(X_test, y_test)

test_score = lr.score(X_test, y_test).round(3)

print('Training Score:', lr.score(X_train, y_train).round(3))
print('Testing Score :',  lr.score(X_test, y_test).round(3))

"""

 

# calculating execution time
elapsed_time = timeit.timeit(code_to_test, number=3)/3
print(elapsed_time)
