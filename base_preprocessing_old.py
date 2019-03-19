
# this file is for preprocessing the data before analysis and visualisation
#%% Load packages 

import pandas as pd

# later/optional:
#import networkx as nx 
#import matplotlib as mpl
# deepgraph?
# ggraph?

#%% Load data

# loading routes as dataframe
df_routes = pd.read_csv('routes.csv', sep=',')
print(df_routes)

# loading airports as dataframe
df_airports = pd.read_csv('airports-extended.csv', sep=',', header=None)
print(df_airports)

#%% Add/change headers of the CSV files to have a clear and consistent format

# adjust column names (remove white spaces)
df_routes.rename(columns= {" source airport":"source airport"}, inplace=True)
df_routes.rename(columns= {" source airport id":"source airport ID"}, inplace=True)
df_routes.rename(columns= {" destination apirport":"destination airport"}, inplace=True) # fixed, 'apirport' was in the original
df_routes.rename(columns= {" destination airport id":"destination airport ID"}, inplace=True)
df_routes.rename(columns= {" codeshare":"codshare"}, inplace=True)
df_routes.rename(columns= {" stops":"stops"}, inplace=True)
df_routes.rename(columns= {" equipment":"equipment"}, inplace=True)
print(df_routes.columns)
# maybe someone knows a prettier/faster way?;)
# We can make a loop of it, but lets do that later on. 

# assign column names
header = ["source airport ID", "name", "city", "country", "IATA", "ICAO", "lattitude", "longitude", "altitude", "timezone", "DST", "Tz Olson format", "type", "source"]
df_airports.columns = header

#%% Get better idea of the data in the files

# print headers of the columns
print(df_routes.columns)
print(df_airports.columns)

# Unique number of values in both files
# print unique values of df_routes
print('df_routes unique values per variable \n')
for column in df_routes.columns:
    print(f'{column} = {len(df_routes[column].unique())}')

print('\n\n')

#print unique values of df_airports
print('df_airports unique values per variable \n')
for column in df_airports.columns:
    print(f'{column} = {len(df_airports[column].unique())}')
    


#%% Add the airports file to the routes file based on airport source ID 
### This part can take 10 minutes, because it iterates over al rows, only do once,
### Not necessary to do more often if routes_and_corresponding_airports.csv is created

# import regular expression package
import re

# create empty new dataframe, but with the columns of the original df_airports
df_new = pd.DataFrame(columns=["source airport ID", "name", "city", "country", "IATA", "ICAO", "lattitude", "longitude", "altitude", "timezone", "DST", "Tz Olson format", "type", "source"])
# iterate over all rows of df_routes
for index, row in df_routes.iterrows():
    # check if source airport ID in df_routes is known, if so it is a number
    if bool(re.search('[0-9]+', row[3])) == True:
        # change from string to integer and give variable name
        src_airport_id = int(row[3])
        # look for the corresponding source airport ID in df_airports and get this row
        a = df_airports.loc[df_airports['source airport ID'] == src_airport_id]
        # append df_new with the data of that row of df_airports
        df_new = df_new.append({
                "source airport ID": a.iloc[0,0], 
                "name": a.iloc[0,1],
                "city": a.iloc[0,2],
                "country": a.iloc[0,3],
                "IATA": a.iloc[0,4],
                "ICAO": a.iloc[0,5], 
                "lattitude": a.iloc[0,6], 
                "longitude": a.iloc[0,7],
                "altitude": a.iloc[0,8],
                "timezone": a.iloc[0,9],
                "DST": a.iloc[0,10],
                "Tz Olson format": a.iloc[0,11],
                "type": a.iloc[0,12],
                "source": a.iloc[0,13]
                }, ignore_index=True)
    # but if the source airport ID is unknown, fill the row with NaN
    else: 
        df_new = df_new.append({
                "source airport ID": "NaN", 
                "name": "NaN",
                "city": "NaN",
                "country": "NaN",
                "IATA": "NaN",
                "ICAO": "NaN", 
                "lattitude": "NaN", 
                "longitude": "NaN",
                "altitude": "NaN",
                "timezone": "NaN",
                "DST": "NaN",
                "Tz Olson format": "NaN",
                "type": "NaN",
                "source": "NaN"
                }, ignore_index=True)

# create new dataframe, where the df_new is added as columns to the df_routes     
df_routes_and_airports = pd.concat([df_routes, df_new], axis=1)

# save combined dataframe as csv file
df_routes_and_airports.to_csv('routes_and_corresponding_airports.csv')

#%% Add the airports file to the routes file based on airport source ID - Try 1 - save for now

# based on the airport ID
# routes as main 

# first try with match and write:

# make deep copy of df_routes
df_merged = df_routes.copy()

# add value to a new cell in dataframe
df_merged.loc[0,"new column"] = "bla"

# add value from airports dataframe to merged df
df_merged.loc[1,"new column"] = df_airports.iloc[0,0]

# add values to new column in loop
i = 0 # initialize row index to 0
for row in df_merged:
    df_merged.loc[i,"new column"] = df_airports.iloc[i,0]
    i += 1    
    # but iterates over columns... so only first 10 values. Info says that 
    #you should not change the item you are iterating over....
    
# next step: find the row index where df_airports == df_routes.iloc[i,3]
# and integrate in for loop
#%% Other try: just left it here for now
# different way: use merge function of pandas    
# we need a left outer join of our dataframes (routes = left, and we want to all routes columns)

df_merged = df_routes.merge(df_airports, on="source airport ID", how= "left") 
   
# error: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
    


#%%
# could be something like this
# for every row in routes
# if source airport ID [:,2] routes == airport ID [:,0] in airports
# append routes with all airport data

#%% preprocess data into workable format ???????????????????????????
# make it in the right format so it can easily be processed by NetworkX ????
