# MAIN PROGRAM
# handling the interaction with the user

#%% import modules and packages

# self-defined modules
import base_preprocessing as bpp
import module_visualization_worldmap as worldmap
import module_comparison as comp

# other modules
import networkx as nx

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
    

#%% Inspect data -- MAKE THIS IN A NICER FORMAT

# ask user whether he/she wants to get some basic information on the datasets
while True:
    data_inspection = input("do you want to get some information on the datasets? (y/n) ")

    # if user says 'yes', print information on datasets
    if data_inspection == "y":
        
        # print headers of the columns
        print(df_routes.columns)
        print(df_airports.columns) 
        
        # print unique values of df_routes
        print('df_routes unique values per variable \n')
        for column in df_routes.columns:
            print(f'{column} = {len(df_routes[column].unique())}')
        
        print('\n\n')
        
        #print unique values of df_airports
        print('df_airports unique values per variable \n')
        for column in df_airports.columns:
            print(f'{column} = {len(df_airports[column].unique())}')
        
        break
        
    # if user says 'no', print message accordingly
    elif data_inspection == "n":
        print("Okay let's move on to the visualisation then!")
        break
    
    # if an invalid answer is given, print message accordingly
    else:
        print('Sorry, this is not an option, try again')



#%% Data preprocessing
    
# merging of the two df's    
df_merged = bpp.merge_dataframes(df_routes, df_airports)

# cleaning of the merged df
df_merged = bpp.clean_dataframe(df_merged)   



#%% run program in loop until user chooses to exit

while True:   
# print options to user:
    choice = input("""What do you want to do?
    0\tSee demo visualization of the flight network               
    1\tVisualise flight network with self-chosen parameters
    2\tAnalyze opportunities for new flight routes
    3\tExit program.
    enter answer (0/1/2/3): """)
    
    # set default variables for the visualisation
    dataframe = df_merged
    directionality = nx.Graph()
    node_size = 20
    node_visibility = 0.8
    edge_visibility = 0.1
    
    # evaluate user choice and proceed accordingly
    if choice == "0": # see demo
       
        demo_options = input("""What do you want to do?
        1\tShow both airports and flight routes             
        2\tShow only airports
        3\tShow only flight routes
        enter answer (1/2/3): """)
        if demo_options == '1':
            print('You chose to show both airports and flight routes')
        elif demo_options == '2':
            print('You chose to show only the airports')
            edge_visibility = 0
        elif demo_options == '3':
            print('You chose to show only the flight routes')
            node_visibility = 0
        else:
            print('Sorry, this is not an option, we will use the default setting')  
    
        worldmap.visualize_on_worldmap(dataframe, directionality, node_size, node_visibility, edge_visibility)
        
    if choice == "1": # Visualize flight network
        
        # 1st parameters: amount of airlines and airports
        map_amount = input("""What do you want to do?
        1\tSelect all airlines and airports              
        2\tSelect a specific amount of airlines
        3\tSelect a specific amount of airports
        enter answer (1/2/3): """)
        if map_amount == '1':
            print('You chose to plot all airlines and airports')
              
            
        elif map_amount == '2':
            print('You chose to plot a specific amount of airlines')
            map_number_airlines = int(input('How many of the biggest airlines do you want to plot? (1 to 50) '))
            if 1 <= map_number_airlines <= 50:
                print(f'You chose to plot the top {map_number_airlines} biggest airlines')
                ### CALL CREATE SPECIFIC AIRLINES FUNCTION HERE 
                ### AND RETURN THE DATAFRAME AS:  dataframe = 
                ### add cleaning function: dataframe = bpp.clean_dataframe(df_airports)
                
                ### MAYBE ALSO ADD OPTION TO DISPLAY SPECIFIC AIRLINE
            else:
                print('Sorry, this is not an option, we will use the default setting')   
            
        elif map_amount == '3':
            print('You chose to plot a specific amount of airports')
            map_number_airports = int(input('How many of the biggest airports do you want to plot? (1 to 50) '))
            
            ### MAYBE ALSO ADD OPTION TO DISPLAY SPECIFIC AIRPORT. i already made a function
            
            if 1 <= map_number_airports <= 50:
                hubs_nr = map_number_airports
                print(f'You chose to plot the top {hubs_nr} biggest airports')
                
                # determine what are the top 'n' most connected airports (hubs)
                hub_table = comp.find_hubs_in_df(df_merged, hubs_nr)
                
                # create a dataframe with only the in and outcoming flights from hub airports
                df_hubs = comp.hub_network_df(df_merged, hub_table)
                
                # clean dataframe from airports that do not have incoming flights
                dataframe = bpp.clean_dataframe(df_hubs)
                
                # show barplot of amount of flight routes (edges) per hub airport
                comp.barplot_hubs(hub_table)
                
            else:
                print('Sorry, this is not an option, we will use the default setting')   

        else:
            print('Sorry, this is not an option, we will use the default setting')                  
    
    
        # 2nd parameter: directed or undirected network
        map_edges = input("""What do you want to do?
        1\tMake an undirected network              
        2\tMake a directed network
        enter answer (1/2): """)
        
        if map_edges == '1':
            print(f'You chose to create an undirected network')
            
        elif map_edges == '2':
            print(f'You chose to create a directed network')
            directionality = nx.DiGraph()
            
        else:
            print('Sorry, this is not an option, we will use the default setting')   
        

        # 3rd parameter: size of the airports
        size_airport = input("""What do you want to do?
        1\tDisplay all airports with the same size             
        2\tDisplay size of airport depending on how many flight routes it has (degree)
        enter answer (1/2): """)
        
        if size_airport == '1':
            print('You chose to display all airports with the same size')
            
        elif size_airport == '2':
            print('You chose to display airport size dependent on degree')
            
            # create graph object from dataframe defined as 1st parameter
            graph = comp.create_graph_object(dataframe)
            
            # ADJUST! now degree of node changes dependent on subnetwork.
            # degree should be static, based on whole network!
            # use graph object to calculate degree per node and write to list
            node_size = comp.node_size_degree(graph)
            
        else:
            print('Sorry, this is not an option, we will use the default setting')
        
        
        # VISUALIZE FLIGHT NETWORK WITH USER OPTIONS
        worldmap.visualize_on_worldmap(dataframe, directionality, node_size, node_visibility, edge_visibility)
     
            
    elif choice == "2": # Analyze opportunities for new flight routes
        print("To do: return list of routes that are not/less used in the network of the 100 biggest hubs")
        print("To do: create visualisation of 'missing' routes")
        
    elif choice == "3": # Exit program
        print("Thank you for using this program.")
        break 
    
    else:
        print("Choice not recognized. Try again.")
        
        
      
    
