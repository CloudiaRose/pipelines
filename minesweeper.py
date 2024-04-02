def count_adjacent_mines(grid, row, col):
    """
    Count the number of adjacent mines to a given cell in the grid.

    Args:
        grid (list of list): The grid representing the minesweeper board.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        str: The count of adjacent mines as a string.
    """
    count = 0
    for i in range(max(0, row - 1), min(row + 2, len(grid))):
        for j in range(max(0, col - 1), min(col + 2, len(grid[0]))):
            if grid[i][j] == '#':
                count += 1
    return str(count)


def minesweeper(grid):
    """
    Generate a new grid representing the minesweeper board with counts of adjacent mines.

    Args:
        grid (list of list): The grid representing the minesweeper board.

    Returns:
        list of list: The new grid with counts of adjacent mines.
    """
    rows = len(grid)
    cols = len(grid[0])
    result = [['' for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '-':
                result[i][j] = count_adjacent_mines(grid, i, j)
            else:
                result[i][j] = '#'
    return result


grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Return modified grid
result = minesweeper(grid)
for row in result:
    print(row)
