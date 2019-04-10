
### MODULE_VISUALIZATION_WORLDMAP.PY

### This is the visualization on worldmap module. In here you can find several functions:

### - Functions for creating variables necessary for visualization
### - Functions necessary for other visualization options
### - Functions to create the visualization on the worldmap
### - Functions that include a program for the demo and the visualisation on worldmap


#%% Necessary modules and packages for this module

import module_inspect_data as inspect
import module_settings_airlines_airports as setair

import networkx as nx
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np



#%% Basic functions for creating variables necessary for visualization

# function to create graph object from dataframe using NetworkX
def create_graph_object(df, directionality):
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

# function to draw the nodes and edges with specific parameters
def draw_nodes_and_edges(graph, pos, node_size, node_visibility, edge_visibility, ncolor='#F7A538', ecolor='#5EC4B7', ewidth = 2):
    
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


# function to draw the biggest hub(s) in the network
def draw_biggest_hubs(df, hub_nr, graph_df, pos, color):
    
    # create dataframe with hubs and their degree (number of edges)
    hub_table = setair.find_hubs_in_df(df, hub_nr)
    
    # from dataframe, create separate lists for airport and degree
    hublist = hub_table["airport"].tolist()
    node_size = hub_table["degree"].tolist()
    
    # draw hubs with lay-out parameters
    nx.draw_networkx_nodes(graph_df, pos, nodelist=hublist, node_color=color, node_size = node_size) 
    
    

# function to create a label dictionary for hubs and draw them on the worldmap
def hub_network_labels(hub_table, graph, pos):
    
    # create a list of hubs from the table
    hublist = hub_table["airport"].tolist()
    
    # create empty dictionary for labels
    labels = {}

    # write node (airport) name for every hub in dictionary
    for hub in hublist:
        labels[hub] = hub    
     
    # draw labels with lay-out parameters   
    nx.draw_networkx_labels(graph, pos, labels=labels, font_size=12, font_color='#000000')                                          
             




#%% Function to draw network on the world map

def visualize_on_worldmap(dataframe, directionality=nx.Graph(), node_size=20, hub_nr=0, node_visibility=0.8, edge_visibility=0.1):
     
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
                urcrnrlat=80)

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
    draw_nodes_and_edges(graph, pos, node_size, node_visibility, edge_visibility)
    
    # if hub_nr is more than 0, draw biggest hubs
    if hub_nr > 0:
        draw_biggest_hubs(dataframe, hub_nr, graph, pos, '#CC0000')
        
        # find biggest hubs and draw hub labels
        hub_table = setair.find_hubs_in_df(dataframe, hub_nr)
        hub_network_labels(hub_table, graph, pos)
    
    # show plot
    plt.show()



#%% Program for the demo
    
def demo_program(dataframe):
    
    demo_options = input("""What do you want to do?
    1\tShow both airports and flight routes             
    2\tShow only airports
    3\tShow only flight routes
    enter answer (1/2/3): """)
    if demo_options == '1':
        print('You chose to show both airports and flight routes')
        
        # visualize demo flight network 
        visualize_on_worldmap(dataframe)
    
    elif demo_options == '2':
        print('You chose to show only the airports')
        
        # visualize demo flight network with only nodes
        visualize_on_worldmap(dataframe, edge_visibility = 0)
        
    elif demo_options == '3':
        print('You chose to show only the flight routes')
        
        # visualize demo flight network with only edges
        visualize_on_worldmap(dataframe, node_visibility = 0)

    else:
        print('\nSorry, this is not an option, we will return to the main program')
        
    
#%% Program for the visualisation with self-chosen parameters

def visualisation_worldmap_program(dataframe):

    # default settings
    dataframe = dataframe
    directionality = nx.Graph()
    node_size = 20
    hub_nr = 0
    
    # 1st parameter: amount of airlines and airports
    map_amount = input("""What do you want to do?
    1\tSelect all airlines and airports              
    2\tSelect specific airlines
    3\tSelect specific airports
    enter answer (1/2/3): """)
    
    if map_amount == '1':
        print('You chose to plot all airlines and airports')
        # dataframe input parameter for metafunction is default
          
    elif map_amount == '2':
        print('You chose to plot specific airlines')
        choice_airlines = input("""What do you want to do?
        1\tSelect the biggest airlines             
        2\tSelect a specific airline
        enter answer (1/2): """)
        
        if choice_airlines == '1':
            print('You chose to plot the biggest airlines')
            map_number_airlines = int(input('How many of the biggest airlines do you want to plot? (1 to 15) '))
            
            if 1 <= map_number_airlines <= 15:
                print(f'You chose to plot the top {map_number_airlines} biggest airlines')
                
                # create a table with the top airlines with n. of flights (with IATA code)
                airline_table = setair.airline_table(dataframe)
                
                # create a table with the top airlines with n. of flights (full airline names)
                airline_table_name = setair.airline_table_name(dataframe)
                
                # create input parameter for metafunction: dataframe with only the flights of the desired n. of airlines 
                dataframe = setair.take_nairlines(dataframe, airline_table, map_number_airlines)
                
                # show barplot of number of flight routes per airline, by first taking top n rows of airline table
                top_table = airline_table_name[:map_number_airlines]
                inspect.barplot_from_df(top_table, x="name airline" , y="flight_routes_nr" , ylabel="flight routes")
                

            else:
                print('\nSorry, this is not an option, we will use the default setting: all airports and airlines') 

                
        elif choice_airlines == '2':   
            print('You chose to plot a specific airline based on name')
            
            # create input parameter for metafunction: dataframe with only the in- and outcoming flights of the selected airport through user
            dataframe = setair.define_airline_through_user_input(dataframe)
          
        else:
            print('\nSorry, this is not an option, we will use the default setting: all airports and airlines') 
        
        
    elif map_amount == '3':
        print('You chose to plot specific airports')
        choice_airports = input("""What do you want to do?
        1\tSelect the biggest airports             
        2\tSelect a specific airports
        enter answer (1/2): """)  
        
        if choice_airports == '1':
            print('You chose to plot the biggest airports')
            map_number_airports = int(input('How many of the biggest airports do you want to plot? (1 to 15) '))
            if 1 <= map_number_airports <= 15:
                
                hub_nr = map_number_airports
                print(f'You chose to plot the top {hub_nr} biggest airports')
            
                # determine what are the top 'n' most connected airports (hubs)
                hub_table = setair.find_hubs_in_df(dataframe, hub_nr)
            
                # create input parameter for metafunction: dataframe with only the in- and outcoming flights from hub airports
                dataframe = setair.hub_network_df(dataframe, hub_table)
            
                # show barplot of amount of flight routes (edges) per hub airport
                inspect.barplot_from_df(hub_table, x="airport" , y="degree", ylabel="flight routes")
            else:
                print('\nSorry, this is not an option, we will use the default setting: all airports and airlines') 
                
        elif choice_airports == '2':
            print('You chose to plot a specific airport based on name')
            
            # create input parameter for metafunction: number of hubs to visualise
            hub_nr = 1
            
            # create input parameter for metafunction: dataframe with only the in- and outcoming flights of the selected airport through user
            dataframe = setair.define_airport_through_user_input(dataframe)

    else:
        print('\nSorry, this is not an option, we will use the default setting: all airports and airlines') 



    # 2nd parameter: directed or undirected network
    map_edges = input("""What do you want to do?
    1\tMake an undirected network              
    2\tMake a directed network
    enter answer (1/2): """)
    
    if map_edges == '1':
        print(f'You chose to create an undirected network')
        # directionality input parameter for metafunction is default (undirected)
        
    elif map_edges == '2':
        print(f'You chose to create a directed network')
        
        # create input parameter for metafunction: directed graph
        directionality = nx.DiGraph()
        
    else:
        print('\nSorry, this is not an option, we will use the default setting: an undirected network')   
    

    # 3rd parameter: size of the airports
    size_airport = input("""What do you want to do?
    1\tDisplay all airports with the same size             
    2\tDisplay size of airport depending on how many flight routes it has (degree)
    enter answer (1/2): """)
    
    if size_airport == '1':
        print('You chose to display all airports with the same size')
        # node size parameter for metafunction is default (node_size = 20)
        
    elif size_airport == '2':
        print('You chose to display airport size dependent on degree')
        
        # create graph object from dataframe defined as first parameter
        graph = create_graph_object(dataframe, nx.Graph())

        # create input parameter for metafunction: use graph object to calculate degree per node and write to list
        node_size = node_size_degree(graph)
        
    else:
        print('\nSorry, this is not an option, we will use the default setting: all same size ')
    
    
    # CALLING METAFUNCTION: VISUALIZE FLIGHT NETWORK WITH USER OPTIONS
    visualize_on_worldmap(dataframe, directionality, node_size, hub_nr)


