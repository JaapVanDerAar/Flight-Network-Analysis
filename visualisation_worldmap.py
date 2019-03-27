# !!! for this script, first run the load data and preprocessing cells of main.py
# for this you should also have the preprocessing module in the same directory
# result: you should have the merged dataframe as variable

#%%import necessary packages
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap as Basemap
import matplotlib.lines as mlines

# Load smaller csv file for testing
df_merged_small = pd.read_csv('df_merged_small.csv', sep=',')

#%% Visualisation binary graph - use DiGraph() for directed
# Set variable 'graph', use nx.from_pandas_edgelist
# https://networkx.github.io/documentation/networkx-1.10/reference/generated/networkx.convert_matrix.from_pandas_dataframe.html
# this link contains several options such as making it a DiGraph()
# and it can be made weighted by using edge_attr
graph = nx.from_pandas_edgelist(df_merged_small, source = 'source airport', 
                                 target = 'destination airport')

# set size of the figue using matplotlib as plt
plt.figure(figsize = (20,20))
# Draw graph
nx.draw_networkx(graph)

# add options to figure
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
#%%
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


m = Basemap(projection='merc',
            llcrnrlat=-80,
            urcrnrlat=80,
            llcrnrlon=-180,
            urcrnrlon=180,
            lat_ts=20)
m.drawcoastlines()
m.drawparallels(np.arange(-90.,91.,30.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary()
m.drawcountries()


plt.show()



