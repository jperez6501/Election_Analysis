#Read the file object with the reader function. 
file_reader = csv.reader(election_data)
# Print each row in the csv file. 
for row in file_reader:
    print(row)
#create a filename variable to a direct or indirect path to the file. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# using the open() function with a w mode we will write data to teh open(file_to_save, "w")
Traceback(most recent call last):
File "PyPoll.py", line 24, in <module>
open(file_to_save, "w")
IOError: [Errno 2] No such file or directory: 'analysis/election_analysis.txt'
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Counties in the Election\n \nArapahoe\nDenver\nJefferson")

# Close the file
outfile.close()