
### MODULE COMPARE AIRLINES

# import necessary packages
import module_comparison as comp

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap 




#%% Network metrics 

def calculate_network_metrics_from_df(df):
    
    # create graph object of airline network
    graph_airline = comp.create_graph_object(df)
    
    # number of nodes and edges
    nnodes = graph_airline.number_of_nodes()
    nedges = graph_airline.number_of_edges()
    
     # calculate density of the network
    density_airline = nx.density(graph_airline)
    
    # calculate average shortest path
    short_path_av_airline = nx.average_shortest_path_length(graph_airline)
    global_efficiency_airline = 1/short_path_av_airline
    
    # biggest hub
    hub_table_airline = comp.find_hubs_in_df(df, 1)
    hub_airline = hub_table_airline.iloc[0,0]

    # create list of graph metrics
    graph_metrics = [nnodes, nedges, density_airline, global_efficiency_airline, hub_airline]

    return graph_metrics


def create_graph_metrics_table(df1, df2):
    
    # create graph metrics table
    list_graph_metrics_airline1 = calculate_network_metrics_from_df(df1)
    list_graph_metrics_airline2 = calculate_network_metrics_from_df(df2)

    # make dataframe of graph metrics
    graph_metrics = pd.DataFrame({"metrics":["nr of nodes", "nr of edges", "density", "global efficiency", "biggest hub"], "airline 1": list_graph_metrics_airline1, "airline 2":list_graph_metrics_airline2})
    print(graph_metrics)
    
    


    


