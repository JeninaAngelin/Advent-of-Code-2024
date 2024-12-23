def is_safe(sequence):
    """Check if a sequence is either strictly increasing or strictly decreasing with valid step sizes."""
    if all(1 <= sequence[i + 1] - sequence[i] <= 3 for i in range(len(sequence) - 1)):
        return True  # Increasing
    if all(1 <= sequence[i] - sequence[i + 1] <= 3 for i in range(len(sequence) - 1)):
        return True  # Decreasing
    return False

def safe_with_dampener(report):
    """Check if a report is safe considering the Problem Dampener."""
    # If the report is already safe, return True
    if is_safe(report):
        return True

    # Try removing each level and check if the modified report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports_with_dampener(file_path):
    """Count the number of safe reports considering the Problem Dampener."""
    with open(file_path, 'r') as file:
        reports = [[int(x) for x in line.strip().split()] for line in file]

    safe_count = sum(1 for report in reports if safe_with_dampener(report))
    return safe_count

# Path to the input data file
file_path = 'data.txt'

# Calculate and print the number of safe reports
safe_count = count_safe_reports_with_dampener(file_path)
print(f"Number of safe reports with the Problem Dampener: {safe_count}")

