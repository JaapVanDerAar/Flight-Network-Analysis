# This function is to visualize the network on a map. 
# It contains multiple options as input.


def visualize_on_map():

    map_hubs = str(input('Do you want the hubs to be weighted or not? (weighted/unweigthed) '))

    if map_hubs == 'weighted':
        print(f'You chose to create a {map_hubs} network')
    elif map_hubs == 'unweighted':
        print(f'You chose to create a {map_hubs} network')
    else:
        print('Sorry, this is not an option, we will not proceed any further')
    
    map_edges = str(input('Do you want the edges to be directed or not? (directed/undirected) '))
  
    if map_edges == 'directed':
        print(f'You chose to create a {map_edges} network')
    elif map_edges == 'undirected':
        print(f'You chose to create a {map_edges} network')
    else:
        print('Sorry, this is not an option, we will not proceed any further')
    
    map_number_airlines = str(input('Do you want to plot all airlines or a certain amount of biggest airlines? (all/top) '))
    
    if map_number_airlines == 'all':
        print(f'You chose to plot {map_number_airlines} airlines')
    elif map_number_airlines == 'top':
        map_number_airlines = int(input('How many of the biggest airlines do you want to plot? (1 to 50) '))
        print(f'You chose to plot the top {map_number_airlines} biggest airlines')
    else:
        print('Sorry, this is not an option, we will not proceed any further')

    map_number_airports = str(input('Do you want to plot all airports or a certain amount of biggest airports? (all/top) '))

    if map_number_airports == 'all':
        print(f'You chose to plot {map_number_airports} airports')
    elif map_number_airports == 'top':
        map_number_airports = int(input('How many of the biggest airports do you want to plot? (1 to 50) '))
        print(f'You chose to plot the top {map_number_airports} biggest airports')
    else:
        print('Sorry, this is not an option, we will not proceed any further')

##### WE CAN ALSO ADD SPECIFIC CONTINENTS IF THAT WORKS
        
##### THIS IS THE BASE FOR THIS FUNCTION, WE CAN ASSIGN THE RIGHT VARIABLES TO THIS

##### HERE IS THE FUNCTION OF CREATING THE GRAPH. THE FIRST INPUT IS THE SPECIFIC
##### graph = nx.from_pandas_edgelist(df_merged, source = 'source airport', target = 'destination airport')
##### DF WE WANT TO USE. USING MAP_NUMBER_AIRLINES AND MAP_NUMBER AIRPORTS 
##### WE CAN CREATE THE RIGHT DF AND ADD IT TO THE FUNCTION
##### ALSO, WE CAN ASSIGN DIRECTIONALITY WITH IT USING create_using = nx.DiGraph()
