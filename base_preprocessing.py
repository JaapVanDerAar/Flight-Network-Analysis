#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:09:24 2019

@author: Kirsten
"""

# module for preprocessing the data before analysis and visualisation
import pandas as pd

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

    # delete unnecessary columns
    df_routes = df_routes.loc[:, ["airline", "airline ID", "source airport", "source airport ID", "destination airport", "destination airport ID"]]
    
    # delete rows with unknown source or destination airports ID's
    df_routes = df_routes[(df_routes["source airport ID"]!="\\N") & (df_routes["destination airport ID"]!="\\N")]
    
    # change source airport ID column to type integer
    df_routes["source airport ID"] = df_routes["source airport ID"].astype(int)
    
    # change source airport ID column to type integer
    df_routes["destination airport ID"] = df_routes["destination airport ID"].astype(int)
    
    # return dataframe to calling code
    return df_routes


def load_data_airports_from_file(file):

    # read content into dataframe
    df_airports = pd.read_csv(file, sep=',', header=None)
    
    # assign column names
    header = ["airport ID", "name", "city", "country", "IATA", "ICAO", "latitude", "longitude", "altitude", "timezone", "DST", "Tz Olson format", "type", "source"]
    df_airports.columns = header
    
    # delete unnecessary columns
    df_airports = df_airports.loc[:, ["airport ID", "name", "city", "country", "latitude", "longitude"]]
    
    # return dataframe to calling code
    return df_airports  




#%% Merge dataframes
    
# function to merge dataframes of routes and airports
# merge will be a left outer join (routes = left)    
def merge_dataframes(df_routes, df_airports):
    
    # merge dataframes based on the column source airport ID in df_routes and airport ID in df_airports
    df_merged = pd.merge(df_routes, df_airports, left_on="source airport ID", right_on="airport ID", how= "left") 
      
    # return merged dataframe to calling code
    return df_merged




#%% Clean dataframe from destination airports that do not receive incoming flights
# since we do not have lattitude/longitude data for these airports
    
# it is possible that after deleting these dest airports from the df, and with that there source airport, 
# that new dest airports do not have incoming flights. Therefore we check for this in a loop until 
#there are only dest airports left that receive incoming flights
 
def clean_dataframe(df):
    
    while True:
        
        # create empty list for airports to be removed
        airports_to_remove = []
    
        # create a list of source airports to compare the destination airports
        source_airport_ID_list = df["source airport ID"].tolist()
        
        # for each destination airport, check if it is also a source airport. 
        # If not, add to the 'to remove' list
        for ID in df["destination airport ID"]:
            if ID not in source_airport_ID_list:
                airports_to_remove += [ID]
                
        # if there are no destination airports left that should be removed, 
        # return the cleaned df and break the loop        
        if airports_to_remove == []:

            return df
            break
        
        # if there are airports to remove, select the rows of df with destination airports 
        # that are not in airports_to_remove list
        else:

            df = df[~df["destination airport ID"].isin(airports_to_remove)]
            
