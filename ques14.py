print("Enter multiple lines of text (press Enter on an empty line to finish):")

# List to store the input lines
lines = []

while True:
    line = input()  # Read a line from the user
    if line == "":  # If the line is empty, break the loop
        break
    lines.append(line)  # Add the line to the list

# Print all the lines entered by the user
print("\nYou entered:")
for line in lines:
    print(line)


