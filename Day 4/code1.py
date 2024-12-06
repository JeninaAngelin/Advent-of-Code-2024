def count_xmas_in_grid(file_path):
    # Read the grid from the file
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    
    rows, cols = len(grid), len(grid[0])
    word = "XMAS"
    word_len = len(word)
    
    # Define all 8 directions (dx, dy)
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (1, 1),   # Down-Right
        (1, -1),  # Down-Left
        (0, -1),  # Left
        (-1, 0),  # Up
        (-1, -1), # Up-Left
        (-1, 1)   # Up-Right
    ]
    
    def is_valid(x, y, dx, dy):
        """Check if a word fits starting at (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True
    
    # Count occurrences of "XMAS"
    count = 0
    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if is_valid(r, c, dx, dy):
                    count += 1
    
    return count

# Run the function and print the result
file_path = "data.txt"
result = count_xmas_in_grid(file_path)
print("Total occurrences of XMAS:", result)
