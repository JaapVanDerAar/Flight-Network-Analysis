# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable

#%%import necessary packages
import networkx as nx
import matplotlib as mpl


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

# add edges to graph
G.add_edges_from(edges)

# visualize graph (takes a while)
nx.draw(G,with_labels=True)
nx.draw(G,with_labels=False)
# x.draw(G,pos=nx.spring_layout(G)) diferent lay-out
# does not yet show edges of graph..

# try to visualise edges individually
edge_graph = nx.draw_networkx_edges(G, pos=nx.spring_layout(G))

#%%
# other try of defining edges
# define edges as possible correspondence between source airport ID and destination ID
for node in nodes:
    edges = (airport_source_uniq, airport_dest_uniq) 

# add edges    
G.add_edges_from([(airport_source_uniq, airport_dest_uniq)])
# this doesn't work. should have list of tuples as input


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



# change node size depending on degree node
d = nx.degree(G)
print(d)

nx.draw(G, nodelist=d.keys(), node_size=[v * 100 for v in d.values()])
plt.show()



# visualise with matplotlib - does not work...
import matplotlib.pyplot as plt
#mpl.pyplot.show()
plt.savefig("graph.png")
plt.show()



#%% create weighted graph

# create list of unique combinations
# every unique combination of [soure airport id - destination airport id]. But then correct for A to B == B to A

# this is in matlab: [outputname, IA, IC] = unique(var)
# probably .unique also holds something like this in python
