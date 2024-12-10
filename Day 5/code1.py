def parse_data(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    
    rules_section, updates_section = data.split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    
    return rules, updates

def is_update_correct(update, rules):
    # Create a set of rules applicable to the current update
    update_set = set(update)
    applicable_rules = [(x, y) for x, y in rules if x in update_set and y in update_set]
    
    # Create a dictionary for positions of pages in the update
    positions = {page: idx for idx, page in enumerate(update)}
    
    # Check if all applicable rules are satisfied
    for x, y in applicable_rules:
        if positions[x] >= positions[y]:
            return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def main():
    # Parse the input data
    rules, updates = parse_data('data.txt')
    
    # Initialize the sum of middle pages
    middle_sum = 0
    
    # Process each update
    for update in updates:
        if is_update_correct(update, rules):
            middle_sum += find_middle_page(update)
    
    print(f"The sum of middle pages of correctly ordered updates is: {middle_sum}")

if __name__ == "__main__":
    main()
