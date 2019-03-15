#%% import necessary packages
import pandas as pd




#%% dataframes
# loading routes as dataframe
df_routes = pd.read_csv('routes.csv', sep=',')
print(df_routes)

# loading airports as dataframe
df_airports = pd.read_csv('airports-extended.csv', sep=',')
print(df_airports)



#%% Pandas options

print(df_airports.index)
print(df_airports.columns)
print(df_airports.dtypes)
print(df_routes.columns)
#%%check the data frame info

print(df_routes.info())
print(df_airports.info())

#%% Unique number of values in both files

print('Routes file parameters \n')
for column in df_routes.columns:
    print(f'{column} = {len(df_routes[column].unique())}')

print('\n\n')

print('Airports file parameters \n')
for column in df_airports.columns:
    print(f'{column} = {len(df_airports[column].unique())}')
# Airport ID is the same across files
    # column 2 [1] in routes and column 1 [0] in airports
# Airport parameters
    

#%%
len(df_routes['airline', 'airline ID'].uniques())
len(df_routes['airline ID'].unique())
len(df_routes['airline ID'].unique())
len(df_routes['airline ID'].unique())
len(df_routes['airline ID'].unique())
#%% indexing = .iloc
print(df.iloc[0])
print(df.iloc[0:5])
# rows and columns
print(df_routes.iloc[0:5,0:3])
# specific point
print(df.iloc[0,0])

print(type(df.iloc[0]))

#%% using labels = .loc
print(df.loc[0:5, 'airline'])
# multiple rows select
print(df[['airline', 'airline ID']])
# select specific conditions 
print(df[df['airline']=='ZL'])
print(df[df[' stops']>0])
print(df[(df['airline']=='5T') & (df[' stops']>0)])
print(df[' stops'])
#%% 
print(f'There are {(df[" stops"].sum())} stops in total')
hist = df[' stops'].hist(bins=df[' stops'].max())
print(hist) 
hist = df.hist()
#%% sort values - with index number/or not
sorted_df = df.sort_values('airline')
print(sorted_df)
sorted_reindexed_df = sorted_df.reset_index()
print(sorted_reindexed_df)

