#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:51:37 2019

@author: Kirsten
"""

#%% Import neccessary packages

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import operator

#%%% Basic Functions

# function to create a graph object from dataframe
def create_graph_object(df):
    graph = nx.from_pandas_edgelist(df, source = 'source airport', \
                                 target = 'destination airport')
    return graph


# function to determine the degree of each node in a graph object
def degree_of_nodes(graph):
    
    # calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # sort nodes by degree
    # (since dictionaries can not be sorted on value we use the itemgetter function)
    degree_sorted = sorted(degree.items(), key = operator.itemgetter(1), reverse=True)

    # create dataframe with nodes (airports) and degree per node 
    degree_nodes = pd.DataFrame(degree_sorted, columns=["airport", "degree"])

    return degree_nodes



#%% Metafunctions

# function to find the airports with the most connections to other airports (hubs)
def find_hubs_in_df(df, hubs_nr):
    
    # make graph object from dataframe
    graph = create_graph_object(df)
    
    # caluculate degree of each nodes (degree is the amount of edges a node has)
    degree_nodes = degree_of_nodes(graph)
    
    # select the top degree nodes (hubs) based on the specified number of hubs
    hub_table = degree_nodes[:hubs_nr]
    
    return hub_table
    

# function to create a dataframe with only the in and outcoming flights from hub airports
def hub_network_df(df, hub_table):
 
    # create a list of hubs from the table
    hublist = hub_table["airport"].tolist()
    
    # select all flights from hub airports from the df
    hub_df_source = df[df["source airport"].isin(hublist)]
    
    # select all flights to hub airports from the df
    hub_df_dest = df[df["destination airport"].isin(hublist)]
    
    # concatenate these two selections to create a df with all in and outcoming flights from hub airports
    df_hubnetwork = pd.concat([hub_df_source, hub_df_dest], axis=0)
    
    return df_hubnetwork



# function to create bar plot of top hubs
def barplot_hubs(hub_table):

    # create bar plot of hubs
    hub_table.plot.bar(x = "airport", y = "degree", legend=False)
    plt.ylabel("flight routes")
    plt.show()



# create a dataframe with only the in and outcoming flights from a specific airport
def specific_airport_df(df, airport):
    
    # select all flights from hub airports from the df
    hub_df_source = df[df["source airport"]==airport]
    
    # select all flights to hub airports from the df
    hub_df_dest = df[df["destination airport"]==airport]
    
    # concatenate these two selections to create a df with all in and outcoming flights from hub airports
    df_specific_airport = pd.concat([hub_df_source, hub_df_dest], axis=0)
    
    return df_specific_airport



    
#%% functions for visualization options
    
# function to create a node size list dependent on degree 
def node_size_degree(graph):
    
    # calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # create a list with node sizes by multiplying the node degree with 1.5 for each node
    node_size_list = []
    for h in degree.values():
        node_size_list = node_size_list + [h * 1.5]
    
    return node_size_list


# function to create a label dictionary for hubs
def hub_network_labels(hub_table):
    
    # create a list of hubs from the table
    hublist = hub_table["airport"].tolist()
    
    # create empty dictionary for labels
    labels = {}

    for hub in hublist:
        # write node (airport) name for every hub in dictionary
        labels[hub] = hub    
        
    return labels    


  
