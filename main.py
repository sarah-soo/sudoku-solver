from puzzle import Puzzle
from grid_dict import grids
import numpy as numpy

def find_value_in_grid(coord, missing):
    """
    Tries to find the missing value in the grid containing coord.
    """
    grid_n = which_grid(coord)
    
    for i in grids[grid_n]['x']:
        for j in grids[grid_n]['y']:
            if puzzle[i, j] == missing:
                return True

    return False

def which_grid(coord):
    """
    Returns the grid index that contains the coord.
    """
    counter = 0
    for grid in grids:
        if coord[0] in grid['x'] and coord[1] in grid['y']:
            return counter
        counter += 1

def get_list(unsolved_row, unsolved_col, unsolved_grid):
    """
    Returns a list of row, column and grid index with the corresponding lowest
    number of missing values.

    unsolved_<container>: indexes that have had an unsuccessful solve attempt
                            since the last successful solve
    """
    row_n, r_lowest = find_least_missing("row", unsolved_row)
    column_n, c_lowest = find_least_missing("column", unsolved_col)
    grid_n, g_lowest = find_least_missing("grid", unsolved_grid)
    
    return row_n, column_n, grid_n, [r_lowest, c_lowest, g_lowest]

def find_least_missing(container, unsolved):
    """
    Finds the specified container with the least missing numbers, but is still
    incomplete.

    container: the container type
    unsolved: indexes that have had an unsuccessful solve attempt since the
                last successful solve
    """
    n = 10
    lowest = 10
    count = 0

    for i in range(9):
        for j in range(9):
            if container == "row" and puzzle[i,j] == 0:
                count += 1
            elif container == "column" and puzzle[j,i] == 0:
                count += 1
            elif container == "grid" and grid_if_equal(i, j, 0):
                count += 1

        if (count != 0) and (count < lowest) and (i not in unsolved):
            lowest = count
            n = i
        
        count = 0
        
    return n, lowest

def find_missing_values(n, container):
    """
    Returns the numbers missing from a specified container with index n.
    """
    missing = [x for x in range(1,10)]

    for i in range(9):
        for j in range(1,10):
            if container == "row" and puzzle[n,i] == j:
                missing.remove(j)
                break
            elif container == "column" and puzzle[i,n] == j:
                missing.remove(j)
                break
            elif container == "grid"and grid_if_equal(n, i, j):
                missing.remove(j)
                break

    return missing


def grid_if_equal(i, j, n):
    """
    Allows the grid container to be iterated through with a nested loop with
    two counters.
    """
    if i in range(3):
        x_modifier = 0
    elif i in range(3,6):
        x_modifier = 3
    elif i in range(6,9):
        x_modifier = 6

    if j in range(3):
        r = 0
    elif j in range(3,6):
        r = 1
    elif j in range(6,9):
        r = 2

    if puzzle[r + x_modifier, (j%3)+((i%3)*3)] == n:
        return True
    else:
        return False

def solve(n, container, missing):
    """
    Attempts to place one of the missing values in the specified row/column/grid n.

    n: the container index
    missing: array of values missing from specified container
    container: the container type
    """
    print(str(step) + ". Solving " + container + " " + str(n + 1) + " with " + str(len(missing)) + " missing number(s).")

    coords = []
    for _ in range(len(missing)):
        coords.append(find_empty_coord(n, container, coords))

    for value in missing:
        valid_coords = get_valid_coords(coords, value)

        if len(valid_coords) == 1:
            coord = valid_coords[0]

            puzzle[coord[0], coord[1]] = value
            print_solved(coord, value)

            grid_n = which_grid(coord)
            for mark in pencil:
                if mark[0] == grid_n and mark[1] == "row" and mark[2] == coord[0] and mark[3] == value:
                    pencil.remove(mark)
                    break
                elif mark[0] == grid_n and mark[1] == "col" and mark[2] == coord[1] and mark[3] == value:
                    pencil.remove(mark)
                    break

            return True

        else:
            grid_n = which_grid(valid_coords[0])

            if common_row_or_col(valid_coords) == "row":
                if not [grid_n, "row", valid_coords[0][0], value] in pencil:
                    pencil.append([grid_n, "row", valid_coords[0][0], value])
                    # print("Added pencil mark:", pencil[-1])
                    return True
            elif common_row_or_col(valid_coords) == "col":
                if not [grid_n, "col", valid_coords[0][1], value] in pencil:
                    pencil.append([grid_n, "col", valid_coords[0][1], value])
                    # print("Added pencil mark:", pencil[-1])
                    return True

    return False

def find_empty_coord(n, container, checked_coords):
    """
    Finds the corresponding coordinate element (with n) with a missing number.

    n: part of the coordinate
    container: defines which part of the coordinate n describes
    checked_coords: array of coordinates already found
    """
    if container == "grid":
        if n in range(3):
            i_mod = 0
        elif n in range(3,6):
            i_mod = 3
        elif n in range(6,9):
            i_mod = 6

        j_mod = (n%3)*3

        for i in range(0 + i_mod, 3 + i_mod):
            for j in range(0 + j_mod, 3 + j_mod):
                if puzzle[i, j] == 0 and [i, j] not in checked_coords:
                    return [i, j]
    else:
        for i in range(9):
            if container == "row":
                if puzzle[n, i] == 0 and [n, i] not in checked_coords:
                    return [n, i]
            elif container == "column":
                if puzzle[i, n] == 0 and [i, n] not in checked_coords:
                    return [i, n]

def get_valid_coords(coords, missing_val):
    """
    Returns a list of valid coordinates for the missing value.

    coords: list of coordinates with no value
    missing_val: missing value
    """
    valid_coords = []

    for coord in coords:
        if not already_exists(coord, missing_val):
            valid_coords.append(coord)

    return valid_coords

def already_exists(coord, missing_val):
    """
    Checks if the missing value is already in the row, column or grid of the
    coordinate, and is therefore blocking that coordinate.
    """
    for i in range(9):
        if puzzle[i, coord[1]] == missing_val:
            return True
        if puzzle[coord[0], i] == missing_val:
            return True

    if find_value_in_grid(coord, missing_val):
        return True

    grid_n = which_grid(coord)

    for mark in pencil:
        if mark[0] != grid_n and mark[1] == "row" and mark[2] == coord[0] and mark[3] == missing_val:
            return True
        elif mark[0] != grid_n and mark[1] == "col" and mark[2] == coord[1] and mark[3] == missing_val:
            return True

    return False

def common_row_or_col(coords):
    """
    Checks if the valid coordinates for a missing value has a common row or
    column in the same grid, which then determines whether to add a pencil mark or not.
    """
    common_grid = True
    common_row = True
    common_col = True
    
    row = coords[0][0]
    col = coords[0][1]
    
    for i in range(len(coords)):
        if which_grid(coords[0]) != which_grid(coords[i]):
            common_grid = False

    if common_grid:
        for i in range(len(coords)):
            if not coords[i][0] == row:
                common_row = False
            
            if not coords[i][1] == col:
                common_col = False

        if common_row:
            return "row"
        elif common_col:
            return "col"
    
    return None

def print_solved(coord, missing_val):
    """
    Prints a message to say what has been solved.
    """
    print("*** Solved: '" + str(missing_val) + "' goes in row " + str(coord[0] + 1) + ", column " + str(coord[1] + 1) + ". ***")

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:/repos/sudoku-solver/real_4.txt")

step = 1
unsolved_row, unsolved_col, unsolved_grid = [], [], []
pencil = []

row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

# where grid is indexed as follows:
# |0|1|2|
# |3|4|5|
# |6|7|8|

while row_n != 10 or column_n != 10 or grid_n != 10:
    while n_missing.index(min(n_missing)) == 0 and row_n != 10:
        missing = find_missing_values(row_n, "row")
        if solve(row_n, "row", missing):
            unsolved_row, unsolved_col, unsolved_grid = [], [], []
        else:
            unsolved_row.append(row_n)

        step += 1
        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

    while n_missing.index(min(n_missing)) == 1 and column_n != 10:
        missing = find_missing_values(column_n, "column")
        if solve(column_n, "column", missing):
            unsolved_row, unsolved_col, unsolved_grid = [], [], []
        else:
            unsolved_col.append(column_n)

        step += 1
        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

    while n_missing.index(min(n_missing)) == 2 and grid_n != 10:
        missing = find_missing_values(grid_n, "grid")
        if solve(grid_n, "grid", missing):
            unsolved_row, unsolved_col, unsolved_grid = [], [], []
        else:
            unsolved_grid.append(grid_n)
    
        step += 1
        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

if 0 not in puzzle:
    print(puzzle)
    print("Solved in " + str(step - 1) + " steps.")
else:
    print("Could not solve.\nCurrent state:")
    print(puzzle)
    print("Pencil marks:", pencil)
