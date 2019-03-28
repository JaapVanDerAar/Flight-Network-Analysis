
# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable


#%% Import neccessary packages

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import operator


#%% Function to create a network graph object (still adjust)

df_small = df_merged.iloc[0:20]

df_to_visualize = df_merged

graph = nx.from_pandas_edgelist(df_to_visualize, source = 'source airport', \
                                 target = 'destination airport')

# print graph info
graph_info = nx.info(graph)
print(graph_info)

#%% Draw graph (Make into function!)

nx.draw_networkx(graph)

# set size of the figue using matplotlib as plt
plt.figure(figsize = (10,10))

# add options to figure
plt.axis('off')

# show plot
plt.show()


#%% Global metrics

# calculate density of the network
density = nx.density(graph)

# calculate average shortest path
#short_path_av = nx.average_shortest_path_length(graph)
# error: graph is not fully connected...

# calculate average shortest path per subgraph (takes a while)
#for C in nx.connected_component_subgraphs(graph):
#    print(nx.average_shortest_path_length(C))
# apparently there are 8 subgraphs in the flight network    


#%% Nodal metrics


# calculate degree of each node and save as dictionary
degree_nodes = dict(graph.degree())

# add degree as node attribute
nx.set_node_attributes(graph, degree_nodes, 'degree')

# sort nodes by degree
# (since dictionaries can not be sorted on value we use the itemgetter function)
degree_nodes_sorted = sorted(degree_nodes.items(), key = operator.itemgetter(1), reverse=True)

# create dataframe with nodes (airports) and degree per node 
df_degree = pd.DataFrame(degree_nodes_sorted, columns=["airport", "degree"])

# maybe merge this df with big df_merged to get other info?

# define top hubs
hubs_nr = 10
df_hubs = df_degree[:hubs_nr]



# use list comprehension to access first value in list of tuples
#nodes_to_list = [x[0] for x in degree_nodes_sorted]

# define amount of hubs
#hubs_nr = 20

# create list of top hubs
#hubs = nodes_to_list[:hubs_nr]




# still add: in / out degree


#%% Visualise hubs

# bar plot of top hubs

df_hubs.plot.bar(x = "airport", y = "degree", legend=False)
plt.ylabel("flights")
plt.show()




# options:
# ten biggest hubs as 'weighted' hubs on the world hubs

# compare complete network with network of the top 10 hubs, so problably these ten will 
# already cover almost the whole world. 

#%% optional: What is the most important airport per airline e.g. is 
# Charles de Gaulle or Schiphol Airport the most connected hub of Air-France-KLM?



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





#%% Visualize binary graph of hubs

# Set variable 'graph', use nx.from_pandas_edgelist
# https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.convert_matrix.from_pandas_dataframe.html
# this link contains several options such as making it a DiGraph()
# and it can be made weighted by using edge_attr

df_to_visualize = df_hubs

graph = nx.from_pandas_edgelist(df_to_visualize, source = 'source airport', 
                                 target = 'destination airport')

# set size of the figue using matplotlib as plt
plt.figure(figsize = (20,20))

# Draw graph
nx.draw_networkx(graph)

# add options to figure
plt.axis('off')
plt.show()



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

