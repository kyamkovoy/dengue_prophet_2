# set up the data for prospective cv using the MONTHLY data for years 2006-2016

import pandas as pd
import numpy as np
import pickle
from datetime import datetime
import warnings
warnings.simplefilter(action='ignore')

data = pd.read_csv('../../data/province-month.csv')
province_codes = [10, 41, 50, 70, 90]
years = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]

# use just data for the five provinces
# make a list of dataframes with missing years
smaller_data = data.loc[data['province'].isin(province_codes) & data['date_sick_year'].isin(years)]

# convert the year and month into a datetime (called date_sick)
smaller_data['date_sick_year'].apply(str)
smaller_data['month'].apply(str)

smaller_data['date_sick'] = smaller_data['date_sick_year'].map(str) + '-' + smaller_data['month'].map(str) + '-' + str(1)

# make dfs of data, prospectively, train on a few years, predict the next, etc
cv_df_list = []
for year in years:
    df = smaller_data.loc[smaller_data['date_sick_year'] < year]
    cv_df_list.append(df)

cv_df_list = cv_df_list[1:]

with open('../../output/cv_df_list_prospective_monthly.pkl', 'wb') as file:
    pickle.dump(cv_df_list, file)
