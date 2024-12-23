def is_safe(report):
    """
    Check if the report is safe according to the given rules.
    """
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all differences are within the range [1, 3] or [-3, -1]
    if not all(1 <= abs(diff) <= 3 for diff in differences):
        return False

    # Check if all differences are positive or all are negative
    if all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences):
        return True

    return False


def count_safe_reports(file_path):
    """
    Count the number of safe reports in the input file.
    """
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count += 1
    return safe_count


# File path to the input data
file_path = "data.txt"

# Calculate the number of safe reports
safe_reports = count_safe_reports(file_path)
print(f"Number of safe reports: {safe_reports}")
