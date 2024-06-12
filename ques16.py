# Get input from the user
input_string = input("Enter a string: ")

# Create an empty dictionary to store character frequencies
frequency_dict = {}

# Iterate over each character in the string
for char in input_string:
    # If the character is already in the dictionary, increment its count
    if char in frequency_dict:
        frequency_dict[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        frequency_dict[char] = 1

# Print the frequency of each character
print("Character frequencies:")
for char, frequency in frequency_dict.items():
    print(f"'{char}': {frequency}")