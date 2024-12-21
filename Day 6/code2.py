def load_map(file_path):
    """
    Load the grid map and the guard's initial position from the input file.
    """
    grid = []
    guard_pos = None

    with open(file_path, 'r') as file:
        for y, line in enumerate(file.readlines()):
            row = list(line.strip())
            for x, cell in enumerate(row):
                if cell == '^':  # Guard's initial position
                    guard_pos = (x, y)
                    row[x] = '.'  # Replace guard's position with open space
            grid.append(row)

    return grid, guard_pos


def is_valid_position(grid, x, y):
    """
    Check if the position is within the bounds of the grid and is an open space.
    """
    return 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] == '.'


def simulate_guard(grid, guard_pos, obstruction):
    """
    Simulate the guard's movement after adding an obstruction.
    """
    x, y = guard_pos
    direction = (0, -1)  # Initial direction (up)
    visited = set()

    # Place the obstruction
    grid[obstruction[1]][obstruction[0]] = '#'

    while (x, y) not in visited:
        visited.add((x, y))

        # Determine the next position
        for turn in [(direction[1], -direction[0]), direction, (-direction[1], direction[0])]:
            nx, ny = x + turn[0], y + turn[1]
            if is_valid_position(grid, nx, ny):
                direction = turn
                x, y = nx, ny
                break
        else:
            # If no valid moves are possible, the guard is stuck
            grid[obstruction[1]][obstruction[0]] = '.'  # Remove the obstruction
            return True

    grid[obstruction[1]][obstruction[0]] = '.'  # Remove the obstruction
    return False


def find_obstruction_positions(grid, guard_pos):
    """
    Find all valid positions for placing an obstruction that traps the guard in a loop.
    """
    valid_positions = []

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '.' and (x, y) != guard_pos:
                if simulate_guard(grid, guard_pos, (x, y)):
                    valid_positions.append((x, y))

    return valid_positions


def main():
    file_path = "data.txt"  # Replace with your input file path
    grid, guard_pos = load_map(file_path)
    valid_positions = find_obstruction_positions(grid, guard_pos)
    print(f"Number of valid obstruction positions: {len(valid_positions)}")
    print("Valid positions:", valid_positions)


if __name__ == "__main__":
    main()


