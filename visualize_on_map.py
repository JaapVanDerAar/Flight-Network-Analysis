# This function is to visualize the network on a map. 
# It contains multiple options as input.


def visualize_on_map(map_hubs, map_edges, map_number_airlines, 
                     map_number_airports, map_area):
    
    # First the user is asked if it want the hubs to be weighted or not
    
    map_hubs = str(input('Do you want the hubs to be weighted or unweighted? '))
    if map_hubs == 'weighted':
        print('hi')
    elif map_hubs == 'unweighted': 
        print('hi')
    else: 
        print('wrong input')

    
################ ETC