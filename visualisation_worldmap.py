#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:13:44 2019

@author: Kirsten
"""

# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable

#%%import necessary packages and tools
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap 


#%% Draw network on the world map

# create graph using NetworkX. Give the df, and the source and destination as input.
# choose either diGraph or undirected
# for now: undirected, since directed takes really long to visualise.
# for directed add as parameter: create_using = nx.DiGraph()
graph = nx.from_pandas_edgelist(df_merged, source = 'source airport', 
                                target = 'destination airport')

# print graph info
graph_info = nx.info(graph)
print(graph_info)

#plt.figure(figsize = (10,9))
#nx.draw_networkx(graph)
 # plt.savefig("./images/map_0.png", format = "png", dpi = 300)
#plt.savefig("./map_0.png", format = "png", dpi = 300)
#plt.show()

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

# To let the basemap know where the nodes are, assign values to them.
# Assign the longitude to mx and the lattitude to my
# Because you assign it to the m, which is the basemap, the coordinates are 
# recalculated to the size of m
mx, my = m(df_merged['longitude'].values, df_merged['lattitude'].values)
pos = {}
for count, elem in enumerate (df_merged['source airport']):
     pos[elem] = (mx[count], my[count])    
# now the parameters G (the graph) and pos (the positions) are set  
# i changed IATA to source airport, because i deleted IATA column in the new version of df_merged 
     
# draw the nodes on the map and set other parameters for layout     
nx.draw_networkx_nodes(G = graph, pos = pos, node_list = graph.nodes(), node_size = 50, node_color = 'r', alpha = 0.8)
# draw the edges on the map and set other parameters for layout
nx.draw_networkx_edges(G = graph, pos = pos, edge_color='b', width = 2, alpha=0.2)
# plt.tight_layout()
plt.figure(figsize = (130,120))
plt.show()

# save file
plt.savefig("./map_0.png", format = "png", dpi = 300) 
     


#%%

#### ALL NEXT CODE WE DONT NEED FOR NOT BUT I'LL JUST SAVE IT HERE FOR NOW



#%% Load smaller csv file for testing
# CAUTION: this is just a small selection. This code now only works because 
# every airport has flights to it and back, but i think this is not the case in our dataset
df_merged_small = pd.read_csv('df_merged_small.csv', sep=',')
df_merged_small = df_merged.iloc[[0,1,3,5,9,10,12,13,14,15]]

#%% Visualisation binary graph - use DiGraph() for directed
# Set variable 'graph', use nx.from_pandas_edgelist
# https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.convert_matrix.from_pandas_dataframe.html
# this link contains several options such as making it a create_using = nx.DiGraph()
# and it can be made weighted by using edge_attr
graph = nx.from_pandas_edgelist(df_merged_small, source = 'source airport', 
                                 target = 'destination airport')

# set size of the figue using matplotlib as plt
plt.figure(figsize = (20,20))
# Draw graph
nx.draw_networkx(graph)

# add options to figure
plt.show()

#%% Draw network on the world map

# create graph using NetworkX. Give the df, and the source and destination as input.
# choose either diGraph or undirected
graph = nx.from_pandas_edgelist(df_merged_small, source = 'source airport', 
                                target = 'destination airport', create_using = nx.DiGraph())

# plot this graph to see it, this is optional 
plt.figure(figsize = (10,9))
nx.draw_networkx(graph)


plt.figure(figsize = (10,9))
# use the mercator projection as background, and set the size 
m = Basemap(projection='merc',
            llcrnrlat=-80,
            urcrnrlat=80,
            llcrnrlon=-180,
            urcrnrlon=180,
            lat_ts=20)
# include coastlines, countries and boundaries
m.drawcoastlines()
m.drawmapboundary()
m.drawcountries()
# include longitude and lattitude lines if you want
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))

# To let the basemap know where the nodes are, assign values to them.
# Assign the longitude to mx and the lattitude to my
# Because you assign it to the m, which is the basemap, the coordinates are 
# recalculated to the size of m
mx, my = m(df_merged_small['longitude'].values, df_merged_small['lattitude'].values)


# before plotting is possible, it needs to be in the right structure.
# create variable pos, and for every longitude+lattitude, link them to the IATA code
pos = {}
for count, elem in enumerate (df_merged_small['IATA']):
     pos[elem] = (mx[count], my[count])
     
# now the parameters G (the graph) and pos (the positions) are set
     
# draw the nodes on the map and set other parameters for layout
nx.draw_networkx_nodes(G = graph, pos = pos, node_list = graph.nodes(), node_size = 50, node_color = 'r', alpha = 0.8)
# draw the edges on the map and set other parameters for layout
nx.draw_networkx_edges(G = graph, pos = pos, edge_color='b', width = 2, alpha=0.2)

# save file
plt.savefig("./map_0.png", format = "png", dpi = 300)
plt.show()

#%% Worldmap 1
# import necessary packages
import geopandas as gpd
from shapely.geometry import Point

# to use the Point function of shapely.geometry, it is necessary to have to coordinates
# in one variable. So add a tuple of coordinates in de df_merged file
df_merged_small['Coordinate Points'] = list(zip(df_merged_small['longitude'],
               df_merged_small['lattitude']))

# make Point of them using .apply(Point)
df_merged_small['Coordinate Points'] = df_merged_small['Coordinate Points'].apply(Point)

# create geopandas dataframe to plot
gdf = gpd.GeoDataFrame(df_merged_small, geometry='Coordinate Points')

# get a simple world map that has the outlines of the countries. Set as black and white
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
colors_map = world.plot(color='white', edgecolor='black', figsize = (20,20))

# This does not work yet. 
# Plot with Points on world map
gdf.plot(ax=colors_map, color='red',)
plt.show()

#%% Worldmap 1 - full

# to use the Point function of shapely.geometry, it is necessary to have to coordinates
# in one variable. So add a tuple of coordinates in de df_merged file
df_merged['Coordinate Points'] = list(zip(df_merged['longitude'],
               df_merged['lattitude']))

# make Point of them using .apply(Point)
df_merged['Coordinate Points'] = df_merged['Coordinate Points'].apply(Point)

# create geopandas dataframe to plot
gdf = gpd.GeoDataFrame(df_merged, geometry='Coordinate Points')

# get a simple world map that has the outlines of the countries. Set as black and white
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
colors_map = world.plot(color='white', edgecolor='black', figsize = (20,20))

# This does not work yet. 
# Plot with Points on world map
gdf.plot(ax=colors_map, color='red',)
plt.show()

#%% Worldmap 2 

graph = nx.from_pandas_edgelist(df_merged_small, source = 'source airport', 
                                target = 'destination airport')
plt.figure(figsize = (10,9))
nx.draw_networkx(graph)
#plt.savefig("./images/networkx_basemap/map_0.png", format = "png", dpi = 300)
plt.show()
