import csv
from pprint import pprint

# Open the CSV file for reading
with open('Program-Outcomes.csv', 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    # Skip the first row (headers)
    headers = next(csvreader)

    # Create an empty list to store the data
    data = []

    # Loop through each row in the CSV file
    for row in csvreader:
        # Add the row to the list
        data.append(row)

# Print the data
pprint(data)






