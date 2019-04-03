# MAIN PROGRAM
# handling the interaction with the user

#%% import self-defined modules

import base_preprocessing as bpp
import module_visualization_worldmap as worldmap
import module_comparison as comp

# list of other packages to install:
# matplotlib
# pandas
# numpy
# networkx
# basemap
# operator


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
    

#%% Inspect data --> make optional in function!!

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
    
# merging of the two df's    
try:
    df_merged = bpp.merge_dataframes(df_routes, df_airports)
except Exception as err: 
    print("Something went wrong")
    print(err)    


#%% run program in loop until user chooses to exit

while True:   
# print options to user:
    choice = input("""What do you want to do?
    0\tSee demo visualization of the flight network               
    1\tVisualise flight network with self-chosen parameters
    2\tAnalyze 'who are the biggest'?
    3\tAnalyze opportunities for new flight routes
    4\tExit program.
    enter answer (0/1/2/3/4): """)
    
    # evaluate user choice and proceed accordingly
    if choice == "0": # see demo
       worldmap.visualize_on_worldmap(df_merged,'source airport','destination airport')
 
    
    
    if choice == "1": # Visualize flight network
        
        # 1st parameter: weighted or binary network
        map_weight = input('Do you want the network to be weighted or not? (weighted/unweigthed) ')
        if map_weight == 'weighted':
            print(f'You chose to create a {map_weight} network')
        elif map_weight == 'unweighted':
            print(f'You chose to create a {map_weight} network')
        else:
            print('Sorry, this is not an option, we will not proceed any further')
    
        # 2nd parameter: directed or undirected network
        map_edges = input('Do you want the edges to be directed or not? (directed/undirected) ')
        if map_edges == 'directed':
            print(f'You chose to create a {map_edges} network')
        elif map_edges == 'undirected':
            print(f'You chose to create a {map_edges} network')
        else:
            print('Sorry, this is not an option, we will not proceed any further')
        
        # 3rd parameter: airlines
        map_number_airlines = input('Do you want to plot all airlines or a certain amount of biggest airlines? (all/top) ')
        if map_number_airlines == 'all':
            print(f'You chose to plot {map_number_airlines} airlines')
        elif map_number_airlines == 'top':
            map_number_airlines = int(input('How many of the biggest airlines do you want to plot? (1 to 50) '))
            print(f'You chose to plot the top {map_number_airlines} biggest airlines')
        else:
            print('Sorry, this is not an option, we will not proceed any further')
        
        # 4th parameter: airports
        map_number_airports = input('Do you want to plot all airports or a certain amount of biggest airports? (all/top) ')
        if map_number_airports == 'all':
            print(f'You chose to plot {map_number_airports} airports')
        elif map_number_airports == 'top':
            map_number_airports = int(input('How many of the biggest airports do you want to plot? (1 to 50) '))
            print(f'You chose to plot the top {map_number_airports} biggest airports')
        else:
            print('Sorry, this is not an option, we will not proceed any further')
        
        # create flight network visualization based on user input
        print("to do: plot flight network with the input variables as parameters")
        
     
    elif choice == "2": # Analyze 'who are the biggest'?
        
        # print options to user:
        choice = input("""What do you want to do?
        1\tAnalyze biggest airports (hubs)
        2\tAnalyze biggest airlines
        enter answer (1/2): """)
        if choice == "1":
            hubs_nr = int(input('How many of the biggest airports do you want to analyze? (1 to 50) '))
            comp.create_bargraph_hubs(df_merged, 'source airport', 'destination airport', hubs_nr)

        elif choice == "2":
            print("To do: returns bar graph of top airlines based on 'connectedness' (number of flight routes/edges).")
            #print("To do: returns network metrics of 2 biggest airlines.")
            
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
        
        
      
    

