import csv

# Specify the filename
filename = 'data.csv'

# Open the file and read its contents
with open(filename, mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read and print each row
    for row in csv_reader:
        print(row)
