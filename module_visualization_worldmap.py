# MODULE FOR VISUALIZING FLIGHT NETWORK ON WORLD MAP


#%%import necessary packages and tools
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap 


#%% Function to draw network on the world map

def visualize_on_worldmap(dataframe, directionality):
        
    # create graph object from dataframe using NetworkX
    graph = nx.from_pandas_edgelist(dataframe, source = 'source airport', 
                                target = 'destination airport', create_using = directionality)

    # print graph info
    graph_info = nx.info(graph)
    print(graph_info)

    # draw mercator projection as background and set size
    plt.figure(figsize = (10,9))
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

    # include longitude and lattitude lines if you want
    m.drawparallels(np.arange(-90,90,30))
    m.drawmeridians(np.arange(-180,180,60))

    # create variable pos, that contains the position of each node
    # Assign the longitude to mx and the lattitude to my
    # Because you assign it to the m, which is the basemap, the coordinates are 
    # recalculated to the size of m
    mx, my = m(dataframe['longitude'].values, dataframe['lattitude'].values)
    pos = {}
    for count, elem in enumerate (dataframe['source airport']):
         pos[elem] = (mx[count], my[count])    
    # now the parameters G (the graph) and pos (the positions) are set  
    
    # draw the nodes on the map and set other parameters for layout     
    nx.draw_networkx_nodes(G = graph, pos = pos, node_list = graph.nodes(), node_size = 50, node_color = 'r', alpha = 0.8)
    
    # draw the edges on the map and set other parameters for layout
    nx.draw_networkx_edges(G = graph, pos = pos, edge_color='b', width = 2, alpha=0.2)
    
    # show plot
    # plt.tight_layout()
    # plt.figure(figsize = (130,120))
    plt.show()


     
    
    