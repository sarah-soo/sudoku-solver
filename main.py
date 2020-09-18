from puzzle import Puzzle
import numpy as np

def find_least_missing(container):
    """
    Finds the specified container with the least missing numbers,
    but is still incomplete.
    """
    n = 10
    lowest = 10
    count = 0
    i = 0
    j = 0

    while (i < 9):
        while (j < 9):
            if container == "row":
                if puzzle[i,j] == 0:
                    count += 1
            elif container == "column":
                if puzzle[j,i] == 0:
                    count += 1
            j += 1
        if (count != 0) and (count < lowest):
            lowest = count
            n = i
        i += 1
        j = 0
        count = 0

    if not lowest == 10:
        print("Found " + container + " with " + str(lowest) + " missing number(s)." )

    return n, lowest

def find_missing_values(n, container):
    """
    Finds the numbers missing from a specified container with array index n.
    """
    i = 0
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while (i < 9):
        j = 1
        while (j <= 9):
            if container == "row":
                if puzzle[n,i] == j:
                    missing.remove(j)
                    break
            elif container == "column":
                if puzzle[i,n] == j:
                    missing.remove(j)
                    break
            j += 1
        i += 1

    return missing

def solve(n, missing, container):
    """
    Solves one number in speficied container with array index n.
    """
    print("Solving " + container + " with " + str(len(missing)) + " missing numbers(s).")

    c_c = find_corresponding_coord(n, container)
    
    i = 0

    while i < len(missing):
        if not already_exists(c_c, missing[i], container):
            if container == "row":
                puzzle[n,c_c] = missing[i]
            elif container == "column":
                puzzle[c_c,n] = missing[i]
            m = i
        i += 1

    if container == "row":
        print_solved(n, c_c, m)
    elif container == "column":
        print_solved(c_c, n, m)

def find_corresponding_coord(n, container):
    """
    Finds the corresponding container that also references missing number.
    """
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


def already_exists(c_c, missing, container):
    """
    Checks to see if the missing number from the container (row/column) exists
    in the corresponding container (column/row).
    """
    i = 0
    
    if container == "row":
        while (i < 9):
            if puzzle[i,c_c] == missing:
                return True
            i += 1
        return False
    elif container == "column":
        while (i < 9):
            if puzzle[c_c,i] == missing:
                return True
            i += 1
        return False

def print_solved(row, col, m):
    """
    Prints a message to say what has been solved.
    """
    print("Solved: '" + str(missing[m]) + "' goes in row " + str(row + 1) + ", column " + str(col + 1) + ".")

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:/repos/sudoku-solver/real_1.txt")

print(puzzle)

row_n, r_lowest = find_least_missing("row")
column_n, c_lowest = find_least_missing("column")

while row_n != 10 or column_n != 10:
    while r_lowest <= c_lowest and row_n != 10:
        missing = find_missing_values(row_n, "row")
        solve(row_n, missing, "row")
        row_n, r_lowest = find_least_missing("row")
        column_n, c_lowest = find_least_missing("column")

    while r_lowest > c_lowest and column_n != 10:
        missing = find_missing_values(column_n, "column")
        solve(column_n, missing, "column")
        row_n, r_lowest = find_least_missing("row")
        column_n, c_lowest = find_least_missing("column")
   

print(puzzle)

# The current code is not certain where the number goes; it will blindly insert
# the missing number if it doesn't already exist in the corresponding container.

# Need to start eliminating possibility for missing number to go elsewhere.

# Maybe have a "potential coords" variable for each missing number.
