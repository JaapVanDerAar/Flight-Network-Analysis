# module for preprocessing the data before analysis and visualisation

#%% Load data

# function to load routes data as dataframe
def load_data_routes_from_file(file):
    
    # read content into dataframe
    df_routes = pd.read_csv(file, sep=',')
    
    # adjust column names (remove white spaces)
    df_routes.rename(columns= {" source airport":"source airport"}, inplace=True)
    df_routes.rename(columns= {" source airport id":"source airport ID"}, inplace=True)
    df_routes.rename(columns= {" destination apirport":"destination airport"}, inplace=True) # fixed, 'apirport' was in the original
    df_routes.rename(columns= {" destination airport id":"destination airport ID"}, inplace=True)
    df_routes.rename(columns= {" codeshare":"codshare"}, inplace=True)
    df_routes.rename(columns= {" stops":"stops"}, inplace=True)
    df_routes.rename(columns= {" equipment":"equipment"}, inplace=True)

    # return dataframe to calling code
    return df_routes


def load_data_airports_from_file(file):

    # read content into dataframe
    df_airports = pd.read_csv(file, sep=',', header=None)
    
    # assign column names
    header = ["source airport ID", "name", "city", "country", "IATA", "ICAO", "lattitude", "longitude", "altitude", "timezone", "DST", "Tz Olson format", "type", "source"]
    df_airports.columns = header
    
    # return dataframe to calling code
    return df_airports  


#%% Merge dataframes
    
# function to merge dataframes of routes and airports
# merge will be a left outer join (routes = left)    
def merge_dataframes(df_routes, df_airports):
    
    # make the common column of the df's of similar datatype for the merge
    # change source airport ID in df airports of type string
    df_airports["source airport ID"] = df_airports["source airport ID"].astype(str)
    # would maybe be better though to change source airport ID in df_routes into int, but didn't work yet
    #df_routes["source airport ID"] = df_routes["source airport ID"].astype(int)
    #df_routes["source airport ID"] = pd.to_numeric(df_routes["source airport ID"])
    
    # merge dataframes
    df_merged = pd.merge(df_routes, df_airports, on="source airport ID", how= "left") 
    
    # return merged dataframe to calling code
    return df_merged
