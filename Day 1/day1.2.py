from collections import Counter

def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_count = Counter(right_list)

    similarity_score = 0

    # For each number in the left list, calculate its contribution to the similarity score
    for left in left_list:
        similarity_score += left * right_count[left]

    return similarity_score

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

# Calculate the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)

# Output the result
print(f"Similarity score: {similarity_score}")
