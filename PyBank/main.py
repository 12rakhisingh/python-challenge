# Import the necessary dependencies for project
import os
import csv

# Read the resource file
# csv_file = os.path.join("/Users/msk/Desktop/Project/DataCourse/python-challenge/PyBank/Resources", "budget_data.csv")

# get the current working directory to find out where is the file
# https://docs.python.org/3/library/os.path.html#os.path.dirname:~:text=os.path.dirname(path)%C2%B6
find_folder = os.path.dirname(__file__)

csv_file = os.path.join(find_folder,"Resources", "budget_data.csv")

# Declare variables
count_months = 0
total_amount = 0
previous_profit_loss_change = 0 
profit_loss_change = []
profit_loss_change_month = {}

# Write data to a .csv file
# with open(data_output, "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     # To save specific data input as a row in the csv
#     writer.writerow(["row1", "row2"])

# open budget data csv file
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:

        print(row)
        # count total number of months by adding +1 every time we read a new line
        count_months = count_months + 1
        # store the profilt/loss amount in a variable
        amount = int(row[1])
        # store the month details in a variable
        date_details = row[0]

        print(amount)
        
        # calculate total amount of profit/loss
        total_amount = total_amount + amount
        
        #calculate the change in profit or loss
        change_profit_loss =  amount - previous_profit_loss_change

        # Store month and change in profit/loss details in a dictionary 
        profit_loss_change_month[date_details] = change_profit_loss

        #set current amount as previous profit loss amount
        previous_profit_loss_change = amount

        # print(change_profit_loss)
        # profit_loss_change.append(change_profit_loss)

    
    print(count_months)
    print(total_amount)



    # Calculate the sum of the profit loss changes
    total_change=sum(profit_loss_change_month.values())

    average_change = total_change/count_months

    # print(total_change)

    # #Calculate the average using len
    # average_profit_loss_change = total_change / len(profit_loss_change)

    #Get the max valur from the dictionary
    max_profit_change = max(profit_loss_change_month.values())

    #get the key of the max value 
    max_profit_change_month = max(profit_loss_change_month, key=profit_loss_change_month.get)

    #Get the max valur from the dictionary
    max_loss_change = min(profit_loss_change_month.values())

    #get the key of the max value 
    max_loss_change_month = min(profit_loss_change_month, key=profit_loss_change_month.get)

    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: ' + str(count_months) )
    print("Total: $"+str(total_amount))
    print("Average Change: $"+str(average_change))
    print("Greatest Increase in Profits: "+str(max_profit_change_month)+" ($"+str(max_profit_change)+")")
    print("Greatest Decrease in Profits: "+str(max_loss_change_month)+" ($"+str(max_loss_change)+")")

    # print(average_profit_loss_change)
    # print(len(profit_loss_change))


# Create the path for the output filename
data_output = os.path.join(find_folder,"analysis", "budget_data_analysis.txt")

#  Open the analysis file where you will store the results
with open(data_output, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    # Write data in analysis file
    datafile.write("Financial Analysis\n")
    # writer.writerow(["Financial Analysis"])
    datafile.write("----------------------------\n")
    # writer.writerow(["----------------------------"])

    datafile.write("Total Months: "+str(count_months)+"\n")
    datafile.write("Total : "+str(total_amount)+"\n")
    datafile.write("Average Change: "+str(average_change)+"\n")

    datafile.write("Greatest Increase in Profits: "+str(max_profit_change_month)+" ($"+str(max_profit_change)+")"+"\n")
    datafile.write("Greatest Decrease in Profits: "+str(max_loss_change_month)+" ($"+str(max_loss_change)+")"+"\n")





