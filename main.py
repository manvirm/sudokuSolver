def is_valid_move(grid, row, col, number):
    for x in range(9):
        # Invalid move
        if grid[row][x] == number:
            return False

    for x in range(9):
        # Invalid move
        if grid[x][col] == number:
            return False

    # Get top left row and left most column
    corner_row = row - row % 3
    corner_col = col - col % 3

    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True

def solve(grid, row, col):
    # Check if we reached end (sudoku solved)
    if col = 9:
        if row == 8:
            return True
        row += 1
        col = 0

    # Solve grid recursively
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    # Check all possibilities
    for num in range(1, 10):

        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True