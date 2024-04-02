'''This program takes a grid with dash (mine-free) and hash (mine) and calculates
the number of adjacent mines (horizontally, vertically, diagonally) and replaces the dash
with the number of mines'''

#create a function that takes in grid, row, column as variables
def count_adjacent_mines(grid, row, col):
    #initiate the count at zero
    count = 0
    #iterate through the range of the rows, starting at the row above the given row, and ensure not going out of bounds using len[grid]
    for i in range(max(0, row - 1), min(row + 2, len(grid))):
    #iterate over columns adjacent to given column, starting at column to left of given column
    #and not going out of bounds
        for j in range(max(0, col - 1), min(col + 2, len(grid[0]))):
    #use if statement to check if cell contains a mine
            if grid[i][j] == '#':
    #increment count of mines by one
                count += 1
    return str(count)
    #create a function taking grid as input



def minesweeper(grid):
    #determine number of rows in grid
    rows = len(grid)
    #determine number of columns in grid (all rows have same number)
    cols = len(grid[0])
    #creating empty grid to store adjacent mines
    result = [['' for _ in range(cols)] for _ in range(rows)]
    #iterate over rows
    for i in range(rows):
        #iterate over columns
        for j in range(cols):
            #check if cell empty
            if grid[i][j] == '-':
                #if true, count adjacent mines
                result[i][j] = count_adjacent_mines(grid, i, j)
            else:
                #define current cell as #
                result[i][j] = '#'

    return result



grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]


#return modified grid
result = minesweeper(grid)
for row in result:
    print(row)
