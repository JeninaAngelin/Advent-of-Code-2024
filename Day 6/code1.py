def load_map(file_path):
    """Load the map from the file and find the guard's initial position and direction."""
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    
    # Find guard's initial position and direction
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    guard_pos = None
    guard_dir = None
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in directions:
                guard_pos = (x, y)
                guard_dir = directions[cell]
                grid[y][x] = '.'  # Replace guard's marker with an empty cell
                break
        if guard_pos:
            break
    
    return grid, guard_pos, guard_dir, directions

def simulate_patrol(grid, guard_pos, guard_dir, directions):
    """Simulate the guard's patrol path and count distinct positions visited."""
    visited = set()
    visited.add(guard_pos)  # Add initial position
    
    rows, cols = len(grid), len(grid[0])
    
    # Define turning right 90°
    turn_right = {
        (0, -1): (1, 0),  # ^ -> >
        (1, 0): (0, 1),   # > -> v
        (0, 1): (-1, 0),  # v -> <
        (-1, 0): (0, -1)  # < -> ^
    }
    
    while True:
        # Calculate the next position
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        
        # Check if next position is out of bounds
        if not (0 <= next_pos[0] < cols and 0 <= next_pos[1] < rows):
            break  # Guard has left the mapped area
        
        # Check if next position is an obstacle
        if grid[next_pos[1]][next_pos[0]] == '#':
            # Turn right 90°
            guard_dir = turn_right[guard_dir]
        else:
            # Move forward
            guard_pos = next_pos
            visited.add(guard_pos)
    
    return visited

def main():
    file_path = 'data.txt'
    grid, guard_pos, guard_dir, directions = load_map(file_path)
    visited_positions = simulate_patrol(grid, guard_pos, guard_dir, directions)
    print(f"Distinct positions visited: {len(visited_positions)}")

if __name__ == "__main__":
    main()
