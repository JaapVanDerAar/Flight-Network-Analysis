#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:04:25 2019

@author: Kirsten
"""

# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable


#%% Import neccessary packages

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import operator


#%% Function to create a network graph object

def create_graph_object(df, source_column_name, dest_column_name):
    graph = nx.from_pandas_edgelist(df, source = source_column_name, \
                                 target = dest_column_name)
    return graph


#%% Function to draw graph object

def draw_graph(graph, ns=150, fs=10):
    
    # add options to figure using plt function
    
    # set size
    plt.figure(figsize = (10,10))
    
    # turn axes off
    plt.axis('off')
    
    # draw network
    nx.draw_networkx(graph, node_size = ns, font_size = fs)
    
    # show plot
    plt.show()



#%% NETWORK ANALYSIS OF FLIGHT NETWORK

# create graph object of the flight data in df
graph_flight_network = create_graph_object(df_merged, 'source airport', 'destination airport')

# print graph info
graph_info = nx.info(graph_flight_network)
print(graph_info)



#%% Visualize the network graph

# take smaller subset of df_merged to save time
df_merged_small = df_merged[:100]

# create graph object for subset
graph_flight_network_small = create_graph_object(df_merged_small, 'source airport', 'destination airport')

# draw graph
draw_graph(graph_flight_network_small)



#%% Global metrics

# calculate density of the network
density = nx.density(graph_flight_network)

# calculate average shortest path
#short_path_av = nx.average_shortest_path_length(graph_flight_network)
# error: graph is not fully connected... something we should look at!

# calculate average shortest path per subgraph (takes a while)
#for C in nx.connected_component_subgraphs(graph):
#    print(nx.average_shortest_path_length(C))
# apparently there are 8 subgraphs in the flight network    


#%% Nodal metrics: calculate degree of each node and identify hubs

# calculate degree of each node and save as dictionary
degree_nodes = dict(graph_flight_network.degree())

# add degree as node attribute ???
nx.set_node_attributes(graph_flight_network, degree_nodes, "degree")


# sort nodes by degree
# (since dictionaries can not be sorted on value we use the itemgetter function)
degree_nodes_sorted = sorted(degree_nodes.items(), key = operator.itemgetter(1), reverse=True)

# create dataframe with nodes (airports) and degree per node 
df_degree = pd.DataFrame(degree_nodes_sorted, columns=["airport", "degree"])

# maybe merge this df with big df_merged to get other info?

# define top hubs
hubs_nr = 20
df_hubs = df_degree[:hubs_nr]
hub_list = df_hubs["airport"].tolist()


# still add: in / out degree



#%% THE HUBNETWORK

# create a df with only the flights from hub airports
df_hubs_extended_from = df_merged[df_merged["source airport"].isin(hub_list)]

# create a df with only the flights to hub airports
df_hubs_extended_to = df_merged[df_merged["destination airport"].isin(hub_list)]

# for simplicity we will use the df with flights from hub airports, since this df contains more flights

# create graph object of the hub flight data in df
graph_hub_network = create_graph_object(df_hubs_extended_from, 'source airport', 'destination airport')

# print graph info
graph_info_hubs = nx.info(graph_hub_network)
print(graph_info_hubs)



#%% Visualization 1: bar plot of top hubs

df_hubs.plot.bar(x = "airport", y = "degree", legend=False)
plt.ylabel("flight routes")
plt.show()


#%% Visualization 2: network graph of hub airports and their in and outcoming flight routes

# make list of node size for each hub
degree_hubs = dict(graph_hub_network.degree())

node_size_list_hubs = []
for h in degree_hubs.values():
    node_size_list_hubs = node_size_list_hubs + [h * 1.5]


# draw graph with node size dependent on degree
plt.figure(figsize = (20,20))
plt.axis('off') 

# determine lay-out
pos = nx.fruchterman_reingold_layout(graph_hub_network)

# draw whole network
nx.draw_networkx(graph_hub_network, pos, node_size = node_size_list_hubs, \
                 with_labels=False, width=0.5, edge_color='#778899')


# highlight hubs 

# first create labels only for hubs
labels = {}
labels2 = {}
labels3 = {}
idx = 0

for node in hub_list:
    # write node (airport) name for every hub in dictionary
    labels[node] = node
    
    # write node (airport) city for every hub in dictionary
    bla = df_merged[df_merged["source airport"]== hub_list[idx]].reset_index()
    labels2[node] = bla.loc[0,"city"]
    
    # write both airport name and city in dictionary
    labels3[node] = node, bla.loc[0,"city"]
    idx += 1


# draw hubs
#nx.draw_networkx_nodes(graph_hub_network, pos, nodelist=hub_list, node_color='red', node_size=node_size_list_hubs)


# draw hub labels
nx.draw_networkx_labels(graph_hub_network, pos, labels=labels2, font_size=12, font_color='#000000')
         

# show graph
plt.show()                        

    

            




#%% Visualization 3: network graph of all airports with hubs highlighted

# make list of node size for each node/airport

node_size_list = []
for h in degree_nodes.values():
    node_size_list = node_size_list + [h * 1.5]


# draw graph with node size dependent on degree
plt.figure(figsize = (20,20))
plt.axis('off') 

# determine lay-out
pos = nx.fruchterman_reingold_layout(graph_flight_network)

# draw whole network
nx.draw_networkx(graph_flight_network, pos, node_size = node_size_list, \
                 node_color = "#2F4F4F", with_labels=False, width=0.5, edge_color='#778899')

# draw hubs
nx.draw_networkx_nodes(graph_flight_network, pos, nodelist=hub_list, node_color='red', node_size=node_size_list_hubs)

# show graph
plt.show()  



#%% optional: What is the most important airport per airline e.g. is 
# Charles de Gaulle or Schiphol Airport the most connected hub of Air-France-KLM?



#%% Compare two/three/more biggest airlines:

# so count the number of 'airline' in routes file. But then correct for A to B == B to A
# this is the number of edges in the network of the airline
# So visualize top ... with bar graph/circle or whatever
# optional: visualize top ... in world map 

# Compare using all the graph theory measures such as nodes/degree/edges whatever ...
# efficiency!!!! (average shortest path length function - inverse is measure of global efficiency)



#%% Define biggest airlines

df_top_airlines = df_merged.groupby(['airline', 'airline ID'])['airline'].agg({"code_count": len}).sort_values("code_count", ascending=False).head(100).reset_index()
print(df_top_airlines)














#%% How to:
# create list of unique combinations
# every unique combination of [soure airport id - destination airport id]
# loading these data into nx
# output: huge ass big crazy graph 


# selection of dataframe with unique combinations of [source airport ID - destination airport ID] 
selection = df_merged.drop_duplicates(subset=["source airport ID", "destination airport ID"])
selection2 = selection.iloc[:,2:21] # ignore airline info
# but now include something that corrects for A to B == B to A
# should sum up the amount of duplicates...

#%% Create binary graph

# simple try:

# create empty graph structure
G = nx.Graph()

# unique source and destination airports
airport_source_uniq = df_merged["source airport ID"].unique() #3321 unique source airports
airport_dest_uniq = df_merged["destination airport ID"].unique() #3327 unique dest airports

# define nodes (now: source airports)
nodes = airport_source_uniq.tolist()

# add nodes to graph
G.add_nodes_from(nodes)
# (Use keywords to update specific node attributes for every node, like size and weight)

# selection of dataframe with unique combinations of [source airport ID - destination airport ID] 
selection_uniq_routes = df_merged.drop_duplicates(subset=["source airport ID", "destination airport ID"])

# create lists of source en dest airport IDs
list_sourceAP_ID = selection_uniq_routes["source airport ID"].tolist()
list_destAP_ID = selection_uniq_routes["destination airport ID"].tolist()

# define edges as list of tuples from these lists
edges = list(zip(list_sourceAP_ID, list_destAP_ID))

