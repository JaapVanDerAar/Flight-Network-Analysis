
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
    
    

#%% function to visualize two airline networks on worldmap


# basic functions 
def create_graph_object(df):
    graph = nx.from_pandas_edgelist(df, source = 'source airport', \
                                 target = 'destination airport', create_using = nx.Graph())
    return graph   


def draw_biggest_hub(df, graph_df, pos, color):
    
    metrics = calculate_network_metrics_from_df(df)
    hub = [metrics[4]]
    nx.draw_networkx_nodes(graph_df, pos, nodelist=hub, node_color=color, node_size = 100) 
    

def draw_nodes_and_edges(graph, pos, ncolor, ecolor):
    
    # draw the nodes of airline1 on the map and set other parameters for layout     
    nx.draw_networkx_nodes(G = graph, pos = pos, node_size = 20, node_color = ncolor, alpha = 0.8)
                     
    # draw the edges of airline1 on the map and set other parameters for layout
    nx.draw_networkx_edges(G = graph, pos = pos, edge_color = ecolor, width = 2, alpha = 0.5)
        


# metafunction to create a graph object from dataframe
def visualize_two_networks_on_worldmap(df1, df2):
        
    # create graph object from dataframe for both airlines
    graph_df1 = create_graph_object(df1)

    graph_df2 = create_graph_object(df2)

    # draw mercator projection as background and set size
    plt.figure(figsize = (15,20))
    m = Basemap(projection='merc',
                llcrnrlon=-180,
                llcrnrlat=-80,
                urcrnrlon=180,
                urcrnrlat=80,
                # lat_ts=20,
                # resolution='l',
                # suppress_ticks=True
               )
    
    # include coastlines, countries and boundaries
    m.drawcoastlines()
    m.drawmapboundary()
    m.drawcountries()

    # include longitude and latitude lines if you want
    m.drawparallels(np.arange(-90,90,30))
    m.drawmeridians(np.arange(-180,180,60))

    # create variable pos, that contains the position of each node
    mx, my = m(df1['longitude'].values, df1['latitude'].values)
    pos1 = {}
    for count, elem in enumerate (df1['source airport']):
         pos1[elem] = (mx[count], my[count])    
    
    # create variable pos, that contains the position of each node
    mx, my = m(df2['longitude'].values, df2['latitude'].values)
    pos2 = {}
    for count, elem in enumerate (df2['source airport']):
         pos2[elem] = (mx[count], my[count])     
    
    
    # draw the nodes and edges of the airlines on the map and set other parameters for layout 
    draw_nodes_and_edges(graph_df1, pos1, "#FF6347", '#FFBABA')
    draw_nodes_and_edges(graph_df2, pos2, '#20B2AA', '#AFEEEE')                     

                 
    # draw biggest hubs of airlines
    draw_biggest_hub(df1, graph_df1, pos1, 'r')
    draw_biggest_hub(df2, graph_df2, pos2, 'b')
    
    # draw labels of biggest hub airlines
    #label_hub1 = {hub1:hub1}
    #nx.draw_networkx_labels(graph_df1, pos1, labels=label_hub1, font_size=12, font_color='#000000')                                          
                           
    # show plot
    # plt.tight_layout()
    # plt.figure(figsize = (130,120))
    plt.show()
    


