## Minesweeper

This program implements the Minesweeper game algorithm. Given a grid with dashes representing mine-free cells and hashes representing cells with mines, it calculates the number of adjacent mines (horizontally, vertically, and diagonally) for each mine-free cell and replaces the dash with the count of adjacent mines.

### Functions:

#### `count_adjacent_mines(grid, row, col)`
Counts the number of adjacent mines around a given cell.

- **Arguments**:
  - `grid` (list): The grid representing the Minesweeper board.
  - `row` (int): The row index of the cell.
  - `col` (int): The column index of the cell.

- **Returns**:
  - `str`: The count of adjacent mines as a string.

#### `minesweeper(grid)`
Performs the Minesweeper algorithm on the given grid.

- **Arguments**:
  - `grid` (list): The grid representing the Minesweeper board.

- **Returns**:
  - `list`: The modified grid after performing the Minesweeper algorithm.

### Usage:

1. Ensure you have Python installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

2. Save the code into a file named `minesweeper.py`.

3. Open a terminal or command prompt.

4. Navigate to the directory where `minesweeper.py` is saved.

5. Run the following command:

>>python minesweeper.py

6. The program will execute and print the modified grid after performing the Minesweeper algorithm.

### Notes:
- Dash (-) represents mine-free cells.
- Hash (#) represents cells with mines.
- The program calculates adjacent mines for each mine-free cell and replaces dashes with the count of adjacent mines.
- Cells with invalid indices (due to being on the edge of the grid) are marked with an exclamation mark (!) for error handling.
