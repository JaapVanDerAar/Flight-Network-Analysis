# MODULE FOR VISUALIZING FLIGHT NETWORK ON WORLD MAP


#%%import necessary packages and tools
import module_comparison as comp

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap 



#%% Basic functions 

# function to create graph object from dataframe using NetworkX
def create_graph_object(df, directionality = nx.Graph()):
    graph = nx.from_pandas_edgelist(df, source = 'source airport', \
                                 target = 'destination airport', create_using = directionality)
    return graph   


# function to create variable pos, that contains the position of each node
def create_pos_variable(df, m):
    
    # Assign the longitude to mx and the latitude to my
    # Because you assign it to the m, which is the basemap, the coordinates are 
    # recalculated to the size of m
    mx, my = m(df['longitude'].values, df['latitude'].values)
    pos = {}
    for count, elem in enumerate (df['source airport']):
         pos[elem] = (mx[count], my[count])
    # now the parameters G (the graph) and pos (the positions) are set  
    return pos


def draw_nodes_and_edges(graph, pos, node_size, ncolor='#F7A538', node_visibility = 0.8, ecolor='#5EC4B7', ewidth = 2, edge_visibility = 0.1):
    
    # draw the nodes of graph on the map and set other parameters for layout     
    nx.draw_networkx_nodes(graph, pos, node_size = node_size, node_color = ncolor, alpha = node_visibility)
                     
    # draw the edges of graph on the map and set other parameters for layout
    nx.draw_networkx_edges(graph, pos, edge_color = ecolor, width = ewidth, alpha = edge_visibility)
        
    

#%% Visualization options


# function to create a node size list dependent on degree 
def node_size_degree(graph):
    
    # calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # create a list with node sizes by multiplying the node degree with 1.5 for each node
    node_size_list = []
    for h in degree.values():
        node_size_list = node_size_list + [h * 1.5]
    
    return node_size_list



def draw_biggest_hubs(df, hub_nr, graph_df, pos, color, node_size):
    
    # create table with 
    hub_table = comp.find_hubs_in_df(df, hub_nr)
    hublist = hub_table["airport"].tolist()
    nx.draw_networkx_nodes(graph_df, pos, nodelist=hublist, node_color=color, node_size = node_size) 
    
    

# function to create a label dictionary for hubs and draw them on the worldmap
def hub_network_labels(hub_table, graph, pos):
    
    # create a list of hubs from the table
    hublist = hub_table["airport"].tolist()
    
    # create empty dictionary for labels
    labels = {}

    for hub in hublist:
        # write node (airport) name for every hub in dictionary
        labels[hub] = hub    
     
    # draw labels    
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=12, font_color='#000000')                                          
            
    #return labels   




#%% Function to draw network on the world map

def visualize_on_worldmap(dataframe, directionality, node_size, hub_nr):
     
    # create graph object from dataframe
    graph = create_graph_object(dataframe, directionality)
    
    # print graph info
    graph_info = nx.info(graph)
    print(graph_info)

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
    pos = create_pos_variable(dataframe, m)   
    
    # draw the nodes and edges on the map and set other parameters for layout
    draw_nodes_and_edges(graph, pos, node_size)
    
    # if hub_nr is more than 0, draw biggest hubs
    if hub_nr > 0:
        draw_biggest_hubs(dataframe, hub_nr, graph, pos, '#CC0000', node_size)
        
        # find biggest hubs and draw hub labels
        hub_table = comp.find_hubs_in_df(dataframe, hub_nr)
        hub_network_labels(hub_table, graph, pos)
    
    # show plot
    # plt.figure(figsize = (130,120))
    plt.show()

     



#%% Function to visualise multiple networks on the worldmap
    
def visualize_two_networks_on_worldmap(df1, df2):
        
    # create graph object from dataframe for both airlines
    graph_df1 = create_graph_object(df1, directionality = nx.Graph())

    graph_df2 = create_graph_object(df2, directionality = nx.Graph())

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

    
    # create variable pos for both airlines, that contains the position of each node
    pos1 = create_pos_variable(df1, m)
    pos2 = create_pos_variable(df2, m)

    # calculate node size of both airline networks
    node_size1 = node_size_degree(graph_df1)
    node_size2 = node_size_degree(graph_df2)
    
    # draw the nodes and edges of the airlines on the map and set other parameters for layout 
    draw_nodes_and_edges(graph = graph_df1, pos = pos1, node_size = node_size1, ncolor = "#FF6347", ecolor = '#FFBABA', edge_visibility = 0.5)
    draw_nodes_and_edges(graph = graph_df2, pos = pos2, node_size = node_size2, ncolor = '#20B2AA', ecolor = '#AFEEEE', edge_visibility = 0.5)                     
                 
    # draw biggest hubs of airlines
    draw_biggest_hubs(df1, 1, graph_df1, pos1, '#CC0000', node_size1)
    draw_biggest_hubs(df2, 1, graph_df2, pos2, '#CC0000', node_size2)
    

    # find biggest hub of airline and draw labels on the graph
    hub1 = comp.find_hubs_in_df(df1, 1)
    hub_network_labels(hub1, graph_df1, pos1)
       
    hub2 = comp.find_hubs_in_df(df2, 1)
    hub_network_labels(hub2, graph_df2, pos2)
        
    # show plot
    # plt.figure(figsize = (130,120))
    plt.show()    
   
    
    
    
    
    
#%% keep to be sure

def visualize_on_worldmap2(dataframe, directionality, node_size, node_visibility, edge_visibility):
     
    # create graph object from dataframe
    graph = create_graph_object(dataframe, directionality = directionality)
    
    # print graph info
    graph_info = nx.info(graph)
    print(graph_info)

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
    pos = create_pos_variable(dataframe, m)   
    
    # draw the nodes and edges on the map and set other parameters for layout
    draw_nodes_and_edges(graph, pos, node_size = node_size, node_visibility = node_visibility, edge_visibility = edge_visibility)
    
    # show plot
    # plt.tight_layout()
    # plt.figure(figsize = (130,120))
    plt.show()    
