#Assing a variable for teh file to load and the path
file_to_load = 'Resources3/election_results.csv'
with open(file_to_load) as election_data: 
    print(election_data)
#open the election results and read the file. 
#to do: perform analysis
#Close the file
election_data.close()