### MODULE_COMPARISON.PY

### This is the comparison module. In here you can find several functions:

### - A Functions to calculate the degree of the airports
### - Functions to select the right dataframes for input
### - Functions to define the user input

#%% Necessary packages for this module

import networkx as nx
import operator
import pandas as pd
import base_preprocessing as bpp
import matplotlib.pyplot as plt

#%%% Basic Functions

### ALSO IN VISUALISATION_WORLDMAP, DELETE IN ONE OF TWO
# function to create a graph object from dataframe 
def create_graph_object(df):
    graph = nx.from_pandas_edgelist(df, source = 'source airport', \
                                 target = 'destination airport')
    return graph


# function to determine the degree of each node in a graph object
def degree_of_nodes(graph):
    
    # calculate degree of each node and save as dictionary
    degree = dict(graph.degree())

    # sort nodes by degree
    # (since dictionaries can not be sorted on value we use the itemgetter function)
    degree_sorted = sorted(degree.items(), key = operator.itemgetter(1), reverse=True)

    # create dataframe with nodes (airports) and degree per node 
    degree_nodes = pd.DataFrame(degree_sorted, columns=["airport", "degree"])

    return degree_nodes



#%% Metafunctions

# function to find the airports with the most connections to other airports (hubs)
def find_hubs_in_df(df, hubs_nr):
    
    # make graph object from dataframe
    graph = create_graph_object(df)
    
    # caluculate degree of each nodes (degree is the amount of edges a node has)
    degree_nodes = degree_of_nodes(graph)
    
    # select the top degree nodes (hubs) based on the specified number of hubs
    hub_table = degree_nodes[:hubs_nr]
    
    return hub_table
    

# function to create a dataframe with only the in and outcoming flights from hub airports
def hub_network_df(df, hub_table):
 
    # create a list of hubs from the table
    hublist = hub_table["airport"].tolist()
    
    # select all flights from hub airports from the df
    hub_df_source = df[df["source airport"].isin(hublist)]
    
    # select all flights to hub airports from the df
    hub_df_dest = df[df["destination airport"].isin(hublist)]
    
    # concatenate these two selections to create a df with all in and outcoming flights from hub airports
    df_hubnetwork = pd.concat([hub_df_source, hub_df_dest], axis=0)
    
    # clean hub network dataframe
    df_hubnetwork_clean = bpp.clean_dataframe(df_hubnetwork)
    
    return df_hubnetwork_clean




# create a dataframe with only the in and outcoming flights from a specific airport
def specific_airport_df(df, airport):
    
    # select all flights from hub airports from the df
    hub_df_source = df[df["source airport"]==airport]
    
    # select all flights to hub airports from the df
    hub_df_dest = df[df["destination airport"]==airport]
    
    # concatenate these two selections to create a df with all in and outcoming flights from hub airports
    df_specific_airport = pd.concat([hub_df_source, hub_df_dest], axis=0)
    
    # clean hub network dataframe
    df_specific_airport_clean = bpp.clean_dataframe(df_specific_airport)
    
    return df_specific_airport_clean


#%% function to create bar plot from table
    
def barplot_from_df(table, x, y, ylabel = None):
    
    # create bar plot of table
    table.plot.bar(x, y, legend=False)
    plt.ylabel(ylabel)
    plt.show()
    

#%% Functions for airlines
#function to create a dataframe for the top airlines    
def airline_table(dataframe):
    #ordering the airlines by number of flights 
    df_top_airlines = dataframe['airline IATA code'].value_counts().reset_index()
    #renaming the second column name 
    df_top_airlines.rename(columns= {'airline IATA code':'flight_routes_nr'}, inplace=True)
    #renamming the first column name 
    df_top_airlines.rename(columns= {'index':'airline IATA code'}, inplace=True)
    
    return df_top_airlines

#function to create a dataframe in which airlines are ordered by flights number and their complete name is displayed 
def airline_table_name(dataframe):
    df_top_airlines = dataframe['name airline'].value_counts().reset_index()
    df_top_airlines.rename(columns= {'name airline':'flight_routes_nr'}, inplace=True)
    df_top_airlines.rename(columns= {'index':'name airline'}, inplace=True)
    
    return df_top_airlines

#function to create a dataframe with the selected airline only 
def take_airlines(dataframe, sel_airline):
    dataframe = dataframe[dataframe['airline IATA code'] == (sel_airline)]
    #airl_selected = only_airl["airline IATA code"].tolist()
    #dataframe = dataframe.loc[dataframe['airline IATA code'].isin(airl_selected)]
    dataframe_clean = bpp.clean_dataframe(dataframe)

    return dataframe_clean


#function to create a dataframe with the n. of seleced airlines only
def take_nairlines(dataframe, airline_table, number):
    #take only the first # airlines (amount selected by the user)
    df_airlines = airline_table[:number]
    #make the previous variable into a list
    airl_list = df_airlines['airline IATA code'].tolist()
    #create a dataframe of flight only by those airlines
    dataframe = dataframe.loc[dataframe['airline IATA code'].isin(airl_list)]
    #clean the just created dataframe 
    dataframe_clean = bpp.clean_dataframe(dataframe)
    
    return dataframe_clean 

# function to create bar plot of top airlines
def barplot_airlines(dataframe):
    dataframe.plot.bar(x = "name airline", y = "flight_routes_nr", legend=False)
    plt.ylabel("flight routes")
    plt.show()







#%%
    
def define_airline_through_user_input(df):
    
    # create a list of unique airlines
    unique_airlines_list = df["airline IATA code"].drop_duplicates().tolist()
    
    # initialise input to false
    input_airline = False
    
    # ask user for an airline to visualise on the map until a valid input is given
    while input_airline == False:
        
        airline = input("""
        Which airline do you want to visualise? Enter the 2-letter IATA code in 
        capital letters.
        
        For inspiration see the 10 airlines with the most flight routes: 
                        
        FR\tRyanair
        AA\tAmerican Airlines
        UA\tUnited Airlines
        DL\tDelta Air Lines
        US\tUS Airways
        CZ\tChina Southern Airlines
        MU\tChina Eastern Airlines
        CA\tAir China
        WN\tSouthwest Airlines
        U2\teasyJet
        
        Enter your answer here: """)
        
        # if input is in the list with unique airlines, proceed
        if airline in unique_airlines_list:   
            
            # create a dataframe with only the fligths of the specified airline
            df_airline = take_airlines(df, airline)
            
            input_airline == True
            
            return df_airline
        
        # if an invalid input is given, give message accordingly and let user try again    
        else: 
            print("This is not a valid input, try again")
    
    
    
    
    
def define_airport_through_user_input(df):
    
    # create a list of unique airlines
    unique_airport_list = df["source airport"].drop_duplicates().tolist()
    
    # initialise input to false
    input_airport = False
    
    # ask user for an airline to visualise on the map until a valid input is given
    while input_airport == False:
    
        airport = input("""
        Which airport do you want to visualise? Enter the 3-letter IATA code in 
        capital letters.
        
        For inspiration see the 10 airports with the most flight routes: 
                        
        AMS\tAmsterdam Airport Schiphol
        FRA\tFrankfurt am Main International Airport
        CDG\tCharles de Gaulle International Airport
        IST\tAtatürk International Airport
        ATL\tHartsfield Jackson Atlanta International Airport
        PEK\tBeijing Capital International Airport
        ORD\tChicago O'Hare International Airport
        MUC\tMunich International Airport
        DME\tDomodedovo International Airport
        DFW\tDallas Fort Worth International Airport
        
        Enter your answer here: """)
        
        # if input is in the list with unique airlines, proceed
        if airport in unique_airport_list:   
            
            # create a dataframe with only the fligths of the specified airline
            df_airport = specific_airport_df(df, airport)
            
            input_airport == True
            
            return df_airport
        
        # if an invalid input is given, give message accordingly and let user try again    
        else: 
            print("This is not a valid input, try again")
    
    
    

