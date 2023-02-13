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