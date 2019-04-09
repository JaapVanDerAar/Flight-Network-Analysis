### MODULE_COMPARISON_AIRLINES.PY

### This is the compare airlines module. In here you can find several functions:

### - Functions to calculate graph metrics and turn them into a table
### - A function containing a program for user input and plotting the airlines 


#%% Necessary packages for this module

import module_comparison as comp
import networkx as nx
import pandas as pd
import module_visualization_worldmap as worldmap


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
    
    


#%% Metafunction

def compare_airlines(df):
    
    print("\nYou chose to compare airlines.")
    
    # let user specify airlines to visualize and create dataframes for both 
    df_airline1 = comp.define_airline_through_user_input(df)
    
    print("\n\tYou choose your first airline. Now select another one to compare!")
    
    df_airline2 = comp.define_airline_through_user_input(df)
    
    # visualize airline networks on worldmap
    worldmap.visualize_two_networks_on_worldmap(df_airline1, df_airline2)  
    
    # print network metrics table
    create_graph_metrics_table(df_airline1, df_airline2)
