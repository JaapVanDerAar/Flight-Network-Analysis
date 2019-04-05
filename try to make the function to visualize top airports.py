#function to select a desired airline or airport and visualize its output, 
#either on a graph or on  a new dataframe  with these data: 
#    1) ask number of airports. 
#    2) find list of these biggest airports. 
#    3) get whole df of these airports. 
#    FUNCTION to select airlines and to select data frame with that number of airlines. 

#%%   should work
while True: 
    try: 
        hubs_user = int(input("How many top airports would you like to be shown? "))
        break 
    except ValueError: 
        print("That was not an integer.")
        
def take_nairports(number):
    df_hubs = df_degree[:number]
    hub_list = df_hubs["airport"].tolist()
    dataframe = df_merged.loc[df_merged['source airport'].isin(hub_list) | df_merged['destination airport'].isin(hub_list)]
    
    return dataframe

   
df_nhubs = take_nairports(hubs_user)

#AIRPORTS, HUBS for visualization better to return a dataframe with IATA, AIRPORT, TOTAL FLIGHTS,LATTITUDE, LONGITUDE
#AIRLINES: do we have the nation where it is located? dont think so. so airline, number of flights, mode of the destinations?

#def desirednairline(amountofairlines):
    #take the input (amount of airlines)

    #return a dataframe with the top n airlines 

def take_airports(aairport):
    only_hubs = df_degree[df_degree['airport'] == (aairport)]
    hub_selected = only_hubs["airport"].tolist()
    dataframe1 = df_merged.loc[df_merged['source airport'].isin(hub_selected) | df_merged['destination airport'].isin(hub_selected)]

    return dataframe1

selectairport = input("Which hub do you want to visualize? (3 letters code, CAPITAL LETTERS) ")

dataframe = take_airports(selectairport)

def usefullines_dataframes(df_merged):
    
    while True:
        
        # create empty list for airports to be removed
        airports_to_remove = []
    
        # create a list of source airports to compare the destination airports with
        source_airport_ID_list = df_merged["source airport ID"].tolist()
        
        # for each destination airport, check if it is also a source airport. If not, add to to_remove list
        for ID in df_merged["destination airport ID"]:
            if ID not in source_airport_ID_list:
                airports_to_remove += [ID]
                
        if airports_to_remove == []:
            break
        else:
        # select the rows of df with destination airports that are not in airports_to_remove list
            df_merged = df_merged[~df_merged["destination airport ID"].isin(airports_to_remove)]
          
    # return merged dataframe to calling code
    return df_merged

cleandf_nameairport = usefullines_dataframes(dataframe)
cleandf_nairport = usefullines_dataframes(df_nhubs)


def take_airlines(airline):
    only_airl = df_merged[df_merged['airline'] == (airline)]
    airl_selected = only_airl["airline"].tolist()
    dataframe2 = df_merged.loc[df_merged['source airport'].isin(hub_selected) | df_merged['destination airport'].isin(hub_selected)]

    return dataframe2

selectairl = input("Which airline do you want to visualize? (3 letters code, CAPITAL LETTERS) ")

dataframe = take_airlines(selectairl)

#def desiredairport (name of the desired airport):
    #select the desired airport 
    
    #return a dataframe with only that airport
    