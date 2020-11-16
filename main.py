from puzzle import Puzzle
from grid_dict import grids
import numpy as np

def grid_if_equal(i, j, n):
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

def find_value_in_grid(coord, missing):    
    counter = 0
    for grid in grids:
        if coord[0] in grid['x'] and coord[1] in grid['y']:
            break
        counter += 1

    # print("Searching for " + str(missing) + " in grid " + str(counter))

    for i in grids[counter]['x']:
        for j in grids[counter]['y']:
            if puzzle[i, j] == missing:
                return True

    return False

def get_list(unsolved_row, unsolved_col, unsolved_grid):
    row_n, r_lowest = find_least_missing("row", unsolved_row)
    column_n, c_lowest = find_least_missing("column", unsolved_col)
    grid_n, g_lowest = find_least_missing("grid", unsolved_grid)
    
    return row_n, column_n, grid_n, [r_lowest, c_lowest, g_lowest]

def find_least_missing(container, unsolved):
    """
    Finds the specified container with the least missing numbers,
    but is still incomplete.
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
    Finds the numbers missing from a specified container with array index n.
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

def solve(n, missing, container):
    """
    Solves one number in speficied container with array index n.
    """
    print("Solving " + container + " " + str(n + 1) + " with " + str(len(missing)) + " missing number(s).")

    coord = find_coord(n, container)

    unique = False
    m = -1
    for i in range(len(missing)):
        # print("Searching for " + str(missing[i]) + "...")
        if not already_exists(n, coord, missing[i], container):
            if m == -1:
                unique = True
                m = i
            else:
                unique = False

    if unique == True:
        if container == "row":
            puzzle[n,coord] = missing[m]
            print_solved(n, coord, m)
            return True
        elif container == "column":
            puzzle[coord,n] = missing[m]
            print_solved(coord, n, m)
            return True
        elif container == "grid":
            puzzle[coord[0],coord[1]] = missing[m]
            print_solved(coord[0], coord[1], m)
            return True

    return False

def find_coord(n, container):
    """
    Finds the corresponding container that also references missing number.
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
                if puzzle[i,j] == 0:
                    return i, j
    else:
        i = 0
        while (i < 9):
            if container == "row":
                if puzzle[n,i] == 0:
                    break
                i += 1
            elif container == "column":
                if puzzle[i,n] == 0:
                    break
                i += 1
        return i

def already_exists(n, coord, missing, container):
    """
    Checks to see if the missing number from the container (row/column) exists
    in the corresponding container (column/row).
    """
    i = 0
    if container == "row":
        for i in range(9):
            if puzzle[i,coord] == missing:
                # print("Found " + str(missing) + " in (" + str(i) + ", " + str(coord) + ")")
                return True
    
        if find_value_in_grid([n, coord], missing):
            return True

    elif container == "column":
        for i in range(9):
            if puzzle[coord,i] == missing:
                # print("Found " + str(missing) + " in (" + str(coord) + ", " + str(i) + ")")
                return True

        if find_value_in_grid([coord, n], missing):
            return True
    
    elif container == "grid":
        for i in range(9):
            if puzzle[coord[0],i] == missing:
                return True
            if puzzle[i,coord[1]] == missing:
                return True
    
    return False

def print_solved(row, col, m):
    """
    Prints a message to say what has been solved.
    """
    print("Solved: '" + str(missing[m]) + "' goes in row " + str(row + 1) + ", column " + str(col + 1) + ".")

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:/repos/sudoku-solver/real_1.txt")

unsolved_row, unsolved_col, unsolved_grid = [], [], []

row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

# where grid is indexed as follows:
# |0|1|2|
# |3|4|5|
# |6|7|8|

while row_n != 10 or column_n != 10 or grid_n != 10:
    while n_missing.index(min(n_missing)) == 0 and row_n != 10:
        missing = find_missing_values(row_n, "row")
        if solve(row_n, missing, "row"):
            if row_n in unsolved_row:
                unsolved_row.remove(row_n)
        else:
            unsolved_row.append(row_n)

        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

    while n_missing.index(min(n_missing)) == 1 and column_n != 10:
        missing = find_missing_values(column_n, "column")
        if solve(column_n, missing, "column"):
            if column_n in unsolved_col:
                unsolved_col.remove(column_n)
        else:
            unsolved_col.append(column_n)

        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

    while n_missing.index(min(n_missing)) == 2 and grid_n != 10:
        missing = find_missing_values(grid_n, "grid")
        if solve(grid_n, missing, "grid"):
            if grid_n in unsolved_grid:
                unsolved_grid.remove(grid_n)
        else:
            unsolved_grid.append(grid_n)
    
        row_n, column_n, grid_n, n_missing = get_list(unsolved_row, unsolved_col, unsolved_grid)

print(puzzle)
