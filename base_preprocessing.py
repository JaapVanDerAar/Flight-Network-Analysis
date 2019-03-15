# this file is for preprocessing the data before analysis and visualisation
#%% Load packages 

##ggraph?

import pandas as pd



#%% Load data
# dataframes
# loading routes as dataframe
df_routes = pd.read_csv('routes.csv', sep=',')
print(df_routes)

# loading airports as dataframe
df_airports = pd.read_csv('airports-extended.csv', sep=',')
print(df_airports)




#%% Merge data into one file
# based on the airport ID
# routes as main 

# could be something like this
# for every row in routes
# if source airport ID [:,2] routes == airport ID [:,0] in airports
# append routes with all airport data

#%% preprocess data into workable format ???????????????????????????
# make it in the right format so it can easily be processed by NetworkX ????
