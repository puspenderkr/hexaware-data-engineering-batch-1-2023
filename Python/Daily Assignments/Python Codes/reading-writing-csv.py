import csv

# Open a CSV file for reading
with open('data.csv', 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)
    
    # Convert each row to a list and store in a master list
    data_list = [row for row in csv_reader]

