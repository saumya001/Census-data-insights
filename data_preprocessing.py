# Import required modules
import pandas as pd
import numpy as np

# Reading csv file into dataframe
file = pd.read_csv('./Input_Dataset.csv')

# Renaming some columns as per convenience
file.rename(columns = {'native-country':'country', 
                       'educational-num':'education_level',
                       'hours-per-week':'weekly_hours',
                       'marital-status':'marital_status'}, inplace = True)

# Creating a new column containing net capital values
file['net_capital'] = file['capital-gain'] - file['capital-loss']
file.insert(12, 'net_capital', file.pop('net_capital'))

# Removing capital-gain and capital-loss columns
file.drop(['capital-gain', 'capital-loss', 'education'], axis=1, inplace=True)

# Checking for missing values in below mentioned columns
# and removing corresponding rows
file1 = file.drop(file[(file.workclass == '?') | (file.occupation == '?') | (file.country == '?')].index)

# Another way of removing missing values, first replacing all '?' by Nan
file = file.replace('?', np.nan)

# Removing all the rows where there are Nan values
file.dropna()

# Converting processed and clean dataframe to input.csv file
file1.to_csv('input.csv', index_label='id')
