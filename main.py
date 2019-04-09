

# MAIN PROGRAM
# handling the interaction with the user
# 
#


# - Check consistency, does it print 'you chose ..' everywhere, and is there a default variable when the right option is not chosen?
# - Put demo + programm option 2 into module
# - Adding comments
# - Write some code shorter


#%% Import modules and packages

# self-defined modules
import base_preprocessing as bpp
import module_visualization_worldmap as worldmap
import module_comparison as comp
import module_inspect_data as inspect
import module_comparison_airlines as comp_air

# other modules
import networkx as nx

# list of other packages to install:
# matplotlib
# pandas
# numpy
# networkx
# basemap
# operator


#%% Load data

# define filenames which you want to load
# in this case a csv with all flight routes and a csv with geographical locations of airports
filename_routes = "routes.csv"
filename_airports = "airports-extended.csv"
filename_airlines = "airlines.txt"

# load flight routes data into dataframe
try:
    df_routes = bpp.load_data_routes_from_file(filename_routes)
except FileNotFoundError:
    print("file not found, please check filename_routes and current directory")
except Exception as err: 
    print("Something went wrong")
    print(err)

# load airports data into dataframe    
try:
    df_airports = bpp.load_data_airports_from_file(filename_airports)
except FileNotFoundError:
    print("file not found, please check filename_routes and current directory")
except Exception as err: 
    print("Something went wrong")
    print(err)   
    
# load airlines data into dataframe    
try:    
    df_airlines = bpp.load_data_airlines_from_file(filename_airlines)
except FileNotFoundError:
    print("file not found, please check filename_routes and current directory")
except Exception as err: 
    print("Something went wrong")
    print(err) 
    
    
#%% Preprocessing: merging and cleaning of dataframes
    
### MAYBE PUT ALL IN PREPROCESSING WITH METAFUNCTION

# left outer join of routes and airlines dataframes
df_merge_airlines_info = bpp.left_merge_dataframes(df_routes, df_airlines, "airline ID")

# left outer join of routes and airports dataframes
df_merged = bpp.left_merge_dataframes(df_merge_airlines_info, df_airports, "source airport ID")

# reindex columns of dataframe
df_merged = df_merged.reindex(columns=["airline IATA code", "airline ID", "name airline", "country airline", "source airport", "source airport ID", "destination airport", "destination airport ID", "airport name", "airport city", "airport country", "latitude", "longitude"])

# cleaning of the merged dataframe
df_merged = bpp.clean_dataframe(df_merged)   


#%% Run program in loop until user chooses to exit

while True:   
# print options to user:
    choice = input("""What do you want to do?
    0\tSee demo visualization of the flight network.
    1\tInspect the dataframes               
    2\tVisualise flight network with self-chosen parameters.
    3\tCompare airlines.
    4\tExit program.
    enter answer (0/1/2/3/4): """)
    
    # set default variables for the visualisation
    dataframe = df_merged
    directionality = nx.Graph()
    node_size = 20
    hub_nr = 0
    node_visibility = 0.8
    edge_visibility = 0.1
    
    # evaluate user choice and proceed accordingly
    if choice == "0": # see demo
        
        # start this program in the worldmap module with default settings
        worldmap.demo_program(dataframe, directionality, node_size, hub_nr, node_visibility, edge_visibility)

    

    elif choice == "1": # Inspect data

        # start this program in the inspect module with the dataframes to inspect
        inspect.inspect_data(df_routes, df_airports, df_merged)
    
    elif choice == "2": # Visualize flight network
        
        # start this program in the worldmap module with default settings
        worldmap.visualisation_worldmap_program(dataframe, directionality, node_size, hub_nr, node_visibility, edge_visibility)

     
            
    elif choice == "3": # Compare airlines
        
        comp_air.compare_airlines(df_merged)

                
        
    elif choice == "4": # Exit program 
        print("Thank you for using this program.")
        break 
    
    else:
        print("Choice not recognized. Try again.")
        
        
        
      
    

        
      
    
