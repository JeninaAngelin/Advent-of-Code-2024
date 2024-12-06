def count_x_mas_in_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line.strip()) for line in file]
    
    rows, cols = len(grid), len(grid[0])
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
    
    def check_mas(r, c, dr, dc, reverse=False):
        mas_chars = 'MAS' if not reverse else 'SAM'
        for i, char in enumerate(mas_chars):
            nr, nc = r + i*dr, c + i*dc
            if (nr < 0 or nr >= rows or 
                nc < 0 or nc >= cols or 
                grid[nr][nc] != char):
                return False
        return True
    
    x_mas_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'X':
                for dr, dc in directions:
                    # Check MAS on both sides of X
                    if (check_mas(r-dr, c-dc, dr, dc) or 
                        check_mas(r-dr, c-dc, dr, dc, reverse=True) or
                        check_mas(r+dr, c+dc, -dr, -dc) or 
                        check_mas(r+dr, c+dc, -dr, -dc, reverse=True)):
                        x_mas_count += 1
    
    return x_mas_count

# Run the function
file_path = "data.txt"
result = count_x_mas_in_grid(file_path)
print(result)

