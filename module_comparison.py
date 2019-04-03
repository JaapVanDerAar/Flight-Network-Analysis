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

#%%% Functions

# function to create a graph object from dataframe
def create_graph_object(df, source_column_name, dest_column_name):
    graph = nx.from_pandas_edgelist(df, source = source_column_name, \
                                 target = dest_column_name)
    return graph


# function to determine the degree of each node in a graph object
def degree_of_nodes(graph):
    
    # calculate degree of each node and save as dictionary
    degree_nodes = dict(graph.degree())

    # sort nodes by degree
    # (since dictionaries can not be sorted on value we use the itemgetter function)
    degree_nodes_sorted = sorted(degree_nodes.items(), key = operator.itemgetter(1), reverse=True)

    # create dataframe with nodes (airports) and degree per node 
    df_degree = pd.DataFrame(degree_nodes_sorted, columns=["airport", "degree"])

    return df_degree


# function to create bar plot of top hubs
def barplot_hubs(df_degree, hubs_nr):
    
    # select hubs from df_degree based on the number of hubs
    df_hubs = df_degree[:hubs_nr]
    hub_list = df_hubs["airport"].tolist()

    # create bar plot of hubs
    df_hubs.plot.bar(x = "airport", y = "degree", legend=False)
    plt.ylabel("flight routes")
    plt.show()
    
    
    
#%% Metafunction

def create_bargraph_hubs(df, source_column_name, dest_column_name, hubs_nr):
    
    graph = create_graph_object(df, source_column_name, dest_column_name)    
    
    df_degree = degree_of_nodes(graph)  

    barplot_hubs(df_degree, hubs_nr)


  