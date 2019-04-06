### MODULE COMPARISON

#%% Import neccessary packages

import base_preprocessing as bpp

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
    
    # clean hub network dataframe
    df_hubnetwork_clean = bpp.clean_dataframe(df_hubnetwork)
    
    return df_hubnetwork_clean




# create a dataframe with only the in and outcoming flights from a specific airport
def specific_airport_df(df, airport):
    
    # select all flights from hub airports from the df
    hub_df_source = df[df["source airport"]==airport]
    
    # select all flights to hub airports from the df
    hub_df_dest = df[df["destination airport"]==airport]
    
    # concatenate these two selections to create a df with all in and outcoming flights from hub airports
    df_specific_airport = pd.concat([hub_df_source, hub_df_dest], axis=0)
    
    # clean hub network dataframe
    df_specific_airport_clean = bpp.clean_dataframe(df_specific_airport)
    
    return df_specific_airport_clean



    
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



# function to create bar plot from table
def barplot_from_df(table, x = None, y = None, ylabel = None):
    
    # create bar plot of table
    table.plot.bar(x, y, legend=False)
    plt.ylabel(ylabel)
    plt.show()
    

#%% Functions for airlines
    
def airline_table(dataframe):
    df_top_airlines = dataframe['airline IATA code'].value_counts().reset_index()
    df_top_airlines.rename(columns= {"airline IATA code":"flight_routes_nr"}, inplace=True)
    df_top_airlines.rename(columns= {"index":"airline IATA code"}, inplace=True)
    
    return df_top_airlines

# letting the user decide which airline to visualize, put an error detector on the input!
def take_airlines(dataframe, sel_airline):
    only_airl = dataframe[dataframe['airline IATA code'] == (sel_airline)]
    airl_selected = only_airl["airline IATA code"].tolist()
    dataframe = dataframe.loc[dataframe['airline IATA code'].isin(airl_selected)]
    dataframe_clean = bpp.clean_dataframe(dataframe)

    return dataframe_clean

# letting the user decide how many airlines to visualize
def take_nairlines(dataframe, airline_table, number):
    df_airlines = airline_table[:number]
    airl_list = df_airlines["index"].tolist()
    dataframe = dataframe.loc[dataframe['airline IATA code'].isin(airl_list)]
    dataframe_clean = bpp.clean_dataframe(dataframe)
    
    return dataframe_clean

