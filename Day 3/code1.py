import re

def parse_and_sum(file_path):
    # Read the data from the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Define a regex pattern to find valid mul(X,Y) instructions
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

    # Find all matches in the data
    matches = re.findall(pattern, data)

    # Compute the sum of the results of the multiplications
    total_sum = 0
    for match in matches:
        x, y = map(int, match)  # Convert the matched numbers to integers
        total_sum += x * y

    return total_sum

# Path to the file
file_path = "data.txt"

# Compute and print the result
result = parse_and_sum(file_path)
print("The sum of all valid multiplications is:", result)
