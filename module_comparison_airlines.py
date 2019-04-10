
### MODULE_COMPARISON_AIRLINES.PY

### This is the compare airlines module. In here you can find several functions:

### - Functions to calculate graph metrics and turn them into a table
### - Function to create the visualization of airlines on the worldmap
### - A function containing a program for user input and plotting the airlines 


#%% Necessary modules and packages for this module

import module_settings_airlines_airports as setair
import module_visualization_worldmap as worldmap

import networkx as nx
import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


#%% Functions for calculating network metrics 

def calculate_network_metrics_from_df(df):
    
    # create graph object of airline network
    graph_airline = setair.create_graph_object(df)
    
    # number of nodes and edges
    nnodes = graph_airline.number_of_nodes()
    nedges = graph_airline.number_of_edges()
    
    # calculate density of the network
    density_airline = nx.density(graph_airline)
    
    # calculate average shortest path
    short_path_av_airline = nx.average_shortest_path_length(graph_airline)
    global_efficiency_airline = 1/short_path_av_airline
    
    # define biggest hub
    hub_table_airline = setair.find_hubs_in_df(df, 1)
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
    
   
    
    
#%% Function to visualise multiple networks on the worldmap
    
def visualize_two_networks_on_worldmap(df1, df2):
        
    # create graph object from dataframe for both airlines
    graph_df1 = worldmap.create_graph_object(df1, nx.Graph())

    graph_df2 = worldmap.create_graph_object(df2, nx.Graph())

    # draw mercator projection as background and set size
    plt.figure(figsize = (15,20))
    m = Basemap(projection='merc',
                llcrnrlon=-180,
                llcrnrlat=-80,
                urcrnrlon=180,
                urcrnrlat=80)
    
    # include coastlines, countries and boundaries
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()

    # include longitude and latitude lines if you want
    m.drawparallels(np.arange(-90,90,30))
    m.drawmeridians(np.arange(-180,180,60))

    
    # create variable pos for both airlines, that contains the position of each node
    pos1 = worldmap.create_pos_variable(df1, m)
    pos2 = worldmap.create_pos_variable(df2, m)

    # calculate node size of both airline networks
    node_size1 = worldmap.node_size_degree(graph_df1)
    node_size2 = worldmap.node_size_degree(graph_df2)
    
    # draw the nodes and edges of the airlines on the map and set other parameters for layout 
    worldmap.draw_nodes_and_edges(graph_df1, pos1, node_size1, node_visibility = 0.8, edge_visibility = 0.5, ncolor = "#FF6347", ecolor = '#FFBABA')
    worldmap.draw_nodes_and_edges(graph_df2, pos2, node_size2, node_visibility = 0.8, edge_visibility = 0.5, ncolor = '#20B2AA', ecolor = '#AFEEEE')                     
                 
    # draw biggest hubs of airlines
    worldmap.draw_biggest_hubs(df1, 1, graph_df1, pos1, '#CC0000')
    worldmap.draw_biggest_hubs(df2, 1, graph_df2, pos2, '#0000CC')
    
    # find biggest hub of airline and draw labels on the graph
    hub1 = setair.find_hubs_in_df(df1, 1)
    worldmap.hub_network_labels(hub1, graph_df1, pos1)
       
    hub2 = setair.find_hubs_in_df(df2, 1)
    worldmap.hub_network_labels(hub2, graph_df2, pos2)
        
    # show plot
    plt.show()    
       


#%% Program for comparing airlines

def compare_airlines_program(df):
    
    print("\nYou chose to compare airlines.")
    
    # let user specify airlines to visualize and create dataframes for both 
    df_airline1 = setair.define_airline_through_user_input(df)
    
    print("\n\tYou choose your first airline. Now select another one to compare!")
    
    df_airline2 = setair.define_airline_through_user_input(df)
    
    # visualize airline networks on worldmap
    visualize_two_networks_on_worldmap(df_airline1, df_airline2)  
    
    # print network metrics table
    create_graph_metrics_table(df_airline1, df_airline2)
