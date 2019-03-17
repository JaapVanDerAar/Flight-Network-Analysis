
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

# loading airports as dataframe
df_airports = pd.read_csv('airports-extended.csv', sep=',', header=None)
print(df_airports)

# assign column names
header = ["source airport ID", "name", "city", "country", "IATA", "ICAO", "lattitude", "longitude", "altitude", "timezone", "DST", "Tz Olson format", "type", "source"]
df_airports.columns = header


#%% Merge data into one file
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
#%%
# in theory:
    # for every row in the file
    # look at every row in the other file
    # to find the matching source airport ID
    # find the matching airport source airport ID in df_airports
    # add all rows of the df_airports to the file
    
print(df_routes)    
print(df_airports)


# for every row in the file
for index, row in df_routes.iterrows():
    src_airport_id = int(row[3])
    df_airports.loc[df_airports['source airport ID'] == src_airport_id]


#%% Notes and tries under here
#%%
# for every row in the file
for index, row in df_routes.iterrows():
    src_airport_id = int(row[3])
    df_airports.loc[df_airports['source airport ID'] == src_airport_id]

        #%%
        if df_airports.loc[df_airports['source airport ID']] == src_airport_id: 
            print('hello')
    #%%
    src_airport_id = row[3]
    # find the row in ...
    df_airports.loc[df_airports['source airport ID'] == src_airport_id

df_airports.loc[df_airports['source airport ID'] == src_airport_id]
df_airports.loc[df_airports['source airport ID'].isin(src_airport_id)]
# different way: use merge function of pandas    
# we need a left outer join of our dataframes (routes = left, and we want to all routes columns)
#%%
df_merged = df_routes.merge(df_airports, on="source airport ID", how= "left") 
   
# error: You are trying to merge on object and int64 columns. If you wish to proceed you should use pd.concat
    


#%%
# could be something like this
# for every row in routes
# if source airport ID [:,2] routes == airport ID [:,0] in airports
# append routes with all airport data

#%% preprocess data into workable format ???????????????????????????
# make it in the right format so it can easily be processed by NetworkX ????