temperature = int(input("What is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC.")
else: 
    print("Open the windows.") 


counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])
if counties[3] != 'Jefferson':
    print(counties[2])


    # Assign a variable for the file to load and the path.
## file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
## with open(file_to_load) as election_data:

    # Print the file object.
    ## print(election_data)

# Create a filename variable to a direct or indirect path to the file. 
## file_to_save = os.path.join("analysis", "election_anaylsis.txt")
# Using the open() function with the "w" mode we will write data to the file. 
##open(file_to_save, 'w')

# Create a filename variable to a direct or indirect path to the file. 
## file_to_save = os.path.join("analysis", "election_anaylsis.txt")

# Use the open statement to open the file as a text file. 
## outfile = open(file_to_save, "w")
# Write some data to the file. 
## outfile.write("Hello World")

# Close the file. 
## outfile.close()

# Import the datetime class from the datetime module. 
## import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
## now = dt.datetime.now()
# Print the presenet time. 
## print("The time right now is ", now)

# Assign a variable for the file to load and the path. 
## file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
## with open(file_to_load) as election_data:
    
    # To do: perform analysis.
    ## print(election_data)

    # Assign a variable to load a file from a path. 
## file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path. 
## file_to_save = os.path.join("analysis", "election_anaylsis.txt")

# Open the election results and read the file. 
## with open(file_to_save, "w") as txt_file:

# Write three counties to the file. 
    ## txt_file.write("Counties in the Election\n")
    ## txt_file.write("--------------------------\n")
    ## txt_file.write("Arapahoe\nDenver\nJefferson")

 # Print each row in the CSV file.
    ## headers = next(file_reader)
    ## print(headers)