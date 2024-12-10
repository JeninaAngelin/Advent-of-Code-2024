from collections import defaultdict, deque

def parse_data(filename):
    with open(filename, 'r') as file:
        data = file.read().strip()
    
    rules_section, updates_section = data.split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates_section.splitlines()]
    
    return rules, updates

def is_update_correct(update, rules):
    update_set = set(update)
    applicable_rules = [(x, y) for x, y in rules if x in update_set and y in update_set]
    positions = {page: idx for idx, page in enumerate(update)}
    for x, y in applicable_rules:
        if positions[x] >= positions[y]:
            return False
    return True

def correct_update(update, rules):
    # Create a graph for topological sorting
    update_set = set(update)
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Add edges based on applicable rules
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] = in_degree.get(x, 0)  # Ensure all nodes have an entry in in_degree
    
    # Perform topological sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def find_middle_page(update):
    return update[len(update) // 2]

def main():
    rules, updates = parse_data('data.txt')
    middle_sum = 0
    
    for update in updates:
        if not is_update_correct(update, rules):
            corrected_update = correct_update(update, rules)
            middle_sum += find_middle_page(corrected_update)
    
    print(f"The sum of middle pages of corrected updates is: {middle_sum}")

if __name__ == "__main__":
    main()
