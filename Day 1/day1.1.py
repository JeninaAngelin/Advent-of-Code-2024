def calculate_total_distance(left_list, right_list):
    # Sort both lists in ascending order
    left_list.sort()
    right_list.sort()

    total_distance = 0

    # Calculate the sum of distances between corresponding elements in both lists
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)

    return total_distance

def process_data(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line by 3 whitespaces
            left, right = line.split('   ')
            # Append the numbers to the respective lists
            left_list.append(int(left))
            right_list.append(int(right.strip()))  # Remove the newline at the end

    return left_list, right_list

# Example usage:
file_path = 'data.txt'  # Specify the file path with your data

# Process the file to get the left and right lists
left_list, right_list = process_data(file_path)

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)

# Output the result
print(f"Total distance: {total_distance}")
