# Import the necessary dependencies for project
import os
import csv
import collections

# Read the resource file
# csv_file = os.path.join("/Users/msk/Desktop/Project/DataCourse/python-challenge/PyBank/Resources", "budget_data.csv")

# get the current working directory to find out where is the file
# https://docs.python.org/3/library/os.path.html#os.path.dirname:~:text=os.path.dirname(path)%C2%B6
find_folder = os.path.dirname(__file__)

csv_file = os.path.join(find_folder,"Resources", "election_data.csv")


# Declare variables
count_votes = 0
total_amount = 0
candidates = set()
candidate_vote_details = collections.Counter()


# open budget data csv file
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    # print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        
        # print(row)
        # count total number of months by adding +1 every time we read a new line
        count_votes = count_votes + 1

        # get candidate name 
        candidate_name = row[2]

        # add candidate in set https://docs.python.org/3/tutorial/datastructures.html#:~:text=and%20sequence%20unpacking.-,5.4.%20Sets%C2%B6,-Python%20also%20includes
        candidates.add(candidate_name)

        # use counter to count the votes. A counter tool is provided to support convenient and rapid tallies.
        # https://docs.python.org/3/library/collections.html#collections.Counter:~:text=A%20counter%20tool%20is%20provided%20to%20support%20convenient%20and%20rapid%20tallies.%20For%20example%3A
        # refer example to understand counters
        candidate_vote_details[candidate_name] += 1

        # find the election winnder
        election_winner = max(candidate_vote_details, key=candidate_vote_details.get)



# Create the path for the output filename
data_output = os.path.join(find_folder,"analysis", "election_data_analysis.txt")

#  Open the analysis file where you will store the results
with open(data_output, "w", newline='') as datafile:


    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: ' + str(count_votes) )
    print("-------------------------")
    # print(candidate_vote_details)

    # Write date to the file 
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write("Total Votes: "+str(count_votes)+"\n")
    datafile.write("-------------------------\n")

    for candidate, candidate_total_vote in candidate_vote_details.items():
        # print(candidate, candidate_total_vote)
        # Calculate the percentrage votes
        candidate_percent_vote = round((candidate_total_vote/count_votes) * 100, 3)

        #Print the candidate details - name, percent votes, total candidate votes
        print(candidate+": "+str(candidate_percent_vote)+"% ("+str(candidate_total_vote)+")")
        
        # write the same details to file as well 
        datafile.write(candidate+": "+str(candidate_percent_vote)+"% ("+str(candidate_total_vote)+")\n")
    
    print("-------------------------")
    #Print the Winner
    print("Winner: "+str(election_winner))
    print("-------------------------")

    # Write winner details to the analysis file
    datafile.write("-------------------------\n")
    datafile.write("Winner: "+str(election_winner)+"\n")
    datafile.write("-------------------------\n")




    

    
    

