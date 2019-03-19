
# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable

#%%import necessary packages
import networkx as nx

#%% Create binary graph


# selection of dataframe with unique combinations of [source airport ID - destination airport ID] 
selection = df_merged.drop_duplicates(subset=["source airport ID", "destination airport ID"])
selection2 = selection.iloc[:,2:21] # ignore airline info
# but now include something that corrects for A to B == B to A
# should sum up the amount of duplicates...

# leave for now...

# simple try:
# unique source and destination airports
airport_source_uniq = df_merged["source airport ID"].unique() #3321 unique source airports
airport_dest_uniq = df_merged["destination airport ID"].unique() #3327 unique dest airports

# define nodes (now: source airports)
nodes = airport_source_uniq.tolist()

# create empty graph structure
G = nx.Graph()

# add nodes to graph
G.add_nodes_from(nodes)

# Use keywords to update specific node attributes for every node, like size and weight

# add edges, for example:
G.add_edge(3329,6341)
G.add_edge(3329,5811)
G.add_edge(3329,5811)

connections = ()
edges = [] 

# define edges as possible correspondence between source airport ID and destination ID
for node in nodes:
    edges = (aiport_source_uniq, airport_dest_uniq) 
    
G.add_edges_from([(airport_source_uniq, airport_dest_uniq)])
# later:
#define edges as a list of tuples (examples)
#G.add_edges_from([(2965,2990),(2952,6156).(2990,6156)])

# visualize graph (takes a while)
nx.draw(G,with_labels=True)
# cannot see the edges yet... 
# maybe create better visualisation with deepgraph?

#%% How to:
# create list of unique combinations
# every unique combination of [soure airport id - destination airport id]
# loading these data into nx
# output: huge ass big crazy graph 




#%% (create weighted)

# create list of unique combinations
# every unique combination of [soure airport id - destination airport id]. But then correct for A to B == B to A

# this is in matlab: [outputname, IA, IC] = unique(var)
# probably .unique also holds something like this in python


#%% Visualisation on a word map (use binary!)

# take coordinates as location for the hubs of the binary graph

