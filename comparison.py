
#%% Find biggests hubs
# use .degree (in or out) - undirected to find top (10) (might be done with 1:11 sorted?)
# make it weighted or not

#%% visualisation

# make bar graph with degrees of the top hubs

# options:
# ten biggest hubs as 'weighted' hubs on the world hubs

# compare complete network with network of the top 10 hubs, so problably these ten will 
# already cover almost the whole world. 

#%% optional: What is the most important airport per airline e.g. is 
# Charles de Gaulle or Schiphol Airport the most connected hub of Air-France-KLM?


#%% Compare two/three/more biggest airlines:

# so count the number of 'airline' in routes file. But then correct for A to B == B to A
# this is the number of edges in the network of the airline
# So visualize top ... with bar graph/circle or whatever
# optional: visualize top ... in world map 

# Compare using all the graph theory measures such as nodes/degree/edges whatever ...
# efficiency!!!! (average shortest path length function - inverse is measure of global efficiency)


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

#%%
# other try of defining edges
# define edges as possible correspondence between source airport ID and destination ID
for node in nodes:
    edges = (airport_source_uniq, airport_dest_uniq) 

# add edges    
G.add_edges_from([(airport_source_uniq, airport_dest_uniq)])
# this doesn't work. should have list of tuples as input

#%% defining the biggest airlines 

df_top_airlines = df_merged.groupby(['airline', 'airline ID'])['airline'].agg({"code_count": len}).sort_values("code_count", ascending=False).head(100).reset_index()
print(df_top_airlines)
df_biggest_hubs = df_merged.groupby(['source airport'])['city'].agg({"code_count": len}).sort_values("code_count", ascending=False).head(100).reset_index()
print(df_biggest_hubs)
df_biggest_hubs_dest = df_merged.groupby(['destination airport'])['city'].agg({"code_count": len}).sort_values("code_count", ascending=False).head(100).reset_index()
print(df_biggest_hubs_dest)
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

