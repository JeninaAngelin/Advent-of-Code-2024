import re

def parse_and_sum_with_conditions(file_path):
    # Read the data from the file
    with open(file_path, 'r') as file:
        data = file.read()

    # Define regex patterns
    mul_pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"  # Matches mul(X,Y)
    do_pattern = r"do\(\)"                           # Matches do()
    dont_pattern = r"don't\(\)"                     # Matches don't()

    # Find all instructions in the order they appear
    instructions = re.finditer(rf"{do_pattern}|{dont_pattern}|{mul_pattern}", data)

    # Initialize variables
    total_sum = 0
    mul_enabled = True  # At the beginning, mul instructions are enabled

    # Process each instruction
    for match in instructions:
        # Check for do() and don't()
        if match.group() == "do()":
            mul_enabled = True
        elif match.group() == "don't()":
            mul_enabled = False
        else:
            # Handle mul(X,Y) if it's enabled
            if mul_enabled:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum

# Path to the file
file_path = "data.txt"

# Compute and print the result
result = parse_and_sum_with_conditions(file_path)
print("The sum of all enabled multiplications is:", result)
