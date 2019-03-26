# MAIN PROGRAM
# handling the interaction with the user

#%% import self-defined modules

import base_preprocessing as bpp

#%% later/optional packages
#import networkx as nx 
#import matplotlib as mpl
# deepgraph?
# ggraph?

#%% load data sets

# define filenames
filename_routes = "routes.csv"
filename_airports = "airports-extended.csv"

# load routes and airports data in seperate dataframes
try:
    df_routes = bpp.load_data_routes_from_file(filename_routes)
except FileNotFoundError:
    print("file not found, please check filename_routes and current directory")
except Exception as err: 
    print("Something went wrong")
    print(err)
    
try:
    df_airports = bpp.load_data_airports_from_file(filename_airports)
except FileNotFoundError:
    print("file not found, please check filename_routes and current directory")
except Exception as err: 
    print("Something went wrong")
    print(err)   
    


#%% Inspect data

# print headers of the columns
print(df_routes.columns)
print(df_airports.columns)

# Unique number of values in both files
# print unique values of df_routes
print('df_routes unique values per variable \n')
for column in df_routes.columns:
    print(f'{column} = {len(df_routes[column].unique())}')

print('\n\n')

#print unique values of df_airports
print('df_airports unique values per variable \n')
for column in df_airports.columns:
    print(f'{column} = {len(df_airports[column].unique())}')


#%% Data preprocessing
    
# merging of rhe two df's    
try:
    df_merged = bpp.merge_dataframes(df_routes, df_airports)
except Exception as err: 
    print("Something went wrong")
    print(err)    


#%% Here can be the function of visualization on the worldmap

want_visualization = input('Would you like to visualize a network on a map? (y/n) ')
if want_visualization == 'y':
    visualization_on_map() # I'll create this one
    
    
#%% Creation of network graphs
print("To do: create total network graph.")
print("To do: create network graph per airline.")





#%% run program in loop until user chooses to exit
while True:   
# print options to user:
    choice = input("""What do you want to do?
    1\tVisualise flight network
    2\tAnalyze 'who are the biggest'?
    3\tAnalyze opportunities for new flight routes
    4\tExit program.
    enter answer (1/2/3/4): """)
    # evaluate user choice and proceed accordingly
    if choice == "1": # Visualise flight network
        # print options to user:
        choice = input("""Choose visualisation option:
        1\tUndirected and binary
        2\tUndirected and weighted
        3\tDirected and binary
        4\tDirected and weighted
        enter answer (1/2/3/4): """)
        if choice == "1":               
            print("To do: Create flight network on world map (undirected and binary).")
        elif choice == "2":
            print("To do: Create flight network on world map (undirected and weighted).")
        elif choice == "3":
            print("To do: Create flight network on world map (directed and binary).")
        elif choice == "4":
            print("To do: Create flight network on world map (directed and weighted).")
        else:
            print("Choice not recognized. Try again.")
            
    elif choice == "2": # Analyze 'who are the biggest'?
        # print options to user:
        choice = input("""What do you want to do?
        1\tAnalyze biggest hubs
        2\tAnalyze biggest airlines
        enter answer (1/2): """)
        if choice == "1":
            print("To do: return list of 10 biggest hubs.")
            print("To do: create network graph of 10 biggest hubs.")
        elif choice == "2":
            print("To do: return list/library of the biggest hub per airline.")
            print("To do: returns list of airlines sorted by 'connectedness' (number of edges).") # visualise with bar graph?
            print("To do: returns network metrics of 2 biggest airlines.")
            print("To do: create visualisation of 2 biggest airline networks.")
        else: 
            print("Choice not recognized. Try again.")
            
    elif choice == "3": # Analyze opportunities for new flight routes
        print("To do: return list of routes that are not/less used in the network of the 100 biggest hubs")
        print("To do: create visualisation of 'missing' routes")
        
    elif choice == "4": # Exit program
        print("Thank you for using this program.")
        break 
    
    else:
        print("Choice not recognized. Try again.")
        
        


# PLANNED ADDITIONAL MODULES
# create_network.py creates the network graphs (used as input in further analyses). 
# flight_network_world.py Creates flight network on world map.
# hubs_world.py is a module that has functions to defines the 10 biggest hubs \
# and returns a list and visualisation to the calling code. 
# airlines.py is a module that has functions that return a list/library of \
# biggest hub per airline, a list of airlines sorted by 'connectedness' etc.
# opportunities.py is a module that returns list and visualisation of routes 
# that are less used in the world's flight network .         
    

