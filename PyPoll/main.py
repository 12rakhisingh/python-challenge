# Import the necessary dependencies for project
import os
import csv

# Read the resource file
# csv_file = os.path.join("/Users/msk/Desktop/Project/DataCourse/python-challenge/PyBank/Resources", "budget_data.csv")

# get the current working directory to find out where is the file
# https://docs.python.org/3/library/os.path.html#os.path.dirname:~:text=os.path.dirname(path)%C2%B6
find_folder = os.path.dirname(__file__)

csv_file = os.path.join(find_folder,"Resources", "election_data.csv")


# Declare variables
count_votes = 0
total_amount = 0
previous_profit_loss_change = 0 
profit_loss_change = []
profit_loss_change_month = {}


# open budget data csv file
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        
        # print(row)
        # count total number of months by adding +1 every time we read a new line
        count_votes = count_votes + 1

        # get candidate name 
        candidate_name = row[2]


    



    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: ' + str(count_votes) )
    print("-------------------------")




# Create the path for the output filename
data_output = os.path.join(find_folder,"analysis", "election_data_analysis.txt")

#  Open the analysis file where you will store the results
with open(data_output, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    datafile.write("Election Results\n")
    # writer.writerow(["Election Results"])
    datafile.write("-------------------------\n")
    # writer.writerow(["-------------------------"])

    datafile.write("Total Votes: "+str(count_votes)+"\n")
    # writer.writerow(["Total Votes: ",str(count_votes)])
    datafile.write("-------------------------\n")
    # writer.writerow(["-------------------------"])

