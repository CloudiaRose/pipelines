# This program takes a grid with dash (mine-free) and hash (mine) and calculates
# the number of adjacent mines (horizontally, vertically, diagonally) and replaces the dash
# with the number of mines

def count_adjacent_mines(grid, row, col):
    """
    Count adjacent mines around a given cell.

    Args:
    - grid (list): The grid representing the minesweeper board.
    - row (int): The row index of the cell.
    - col (int): The column index of the cell.

    Returns:
    - str: The count of adjacent mines as a string.
    """
    count = 0  # Initiate the count at zero

    # Iterate through the neighboring cells
    for i in range(max(0, row - 1), min(row + 2, len(grid))):
        for j in range(max(0, col - 1), min(col + 2, len(grid[0]))):
            if grid[i][j] == '#':  # Check if cell contains a mine
                count += 1  # Increment count of mines by one

    return str(count)

def minesweeper(grid):
    """
    Perform the minesweeper algorithm on the given grid.

    Args:
    - grid (list): The grid representing the minesweeper board.

    Returns:
    - list: The modified grid after performing the minesweeper algorithm.
    """
    rows = len(grid)  # Determine number of rows in grid
    cols = len(grid[0])  # Determine number of columns in grid

    result = [['' for _ in range(cols)] for _ in range(rows)]  # Create empty grid to store adjacent mines

    # Iterate over rows and columns
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '-':  # Check if cell is empty
                try:
                    result[i][j] = count_adjacent_mines(grid, i, j)  # Count adjacent mines
                except IndexError:
                    result[i][j] = '!'  # Mark cells with invalid indices as '!' for error handling
            else:
                result[i][j] = '#'  # Define current cell as '#'

    return result

grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = minesweeper(grid)  # Perform minesweeper algorithm on the grid

for row in result:
    print(row)  # Print the modified grid
