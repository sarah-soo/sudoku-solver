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

    for i in range(9):
        for j in range(9):
            if container == "row" and puzzle[i,j] == 0:
                count += 1
            elif container == "column" and puzzle[j,i] == 0:
                count += 1
        if (count != 0) and (count < lowest):
            lowest = count
            n = i
        count = 0

    if not lowest == 10:
        print("Found " + container + " with " + str(lowest) + " missing number(s)." )

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

    return missing

def solve(n, missing, container):
    """
    Solves one number in speficied container with array index n.
    """
    # use recursion

    print("Solving " + container + " with " + str(len(missing)) + " missing numbers(s).")

    cc = find_corresponding_coord(n, container)
    
    for i in range(len(missing)):
        if not already_exists(cc, missing[i], container):
            if container == "row":
                puzzle[n,cc] = missing[i]
            elif container == "column":
                puzzle[cc,n] = missing[i]
            m = i

    if container == "row":
        print_solved(n, cc, m)
    elif container == "column":
        print_solved(cc, n, m)

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


def already_exists(cc, missing, container):
    """
    Checks to see if the missing number from the container (row/column) exists
    in the corresponding container (column/row).
    """
    i = 0
    
    if container == "row":
        for i in range(9):
            if puzzle[i,cc] == missing:
                return True
        return False
    elif container == "column":
        for i in range(9):
            if puzzle[cc,i] == missing:
                return True
        return False

def print_solved(row, col, m):
    """
    Prints a message to say what has been solved.
    """
    print("Solved: '" + str(missing[m]) + "' goes in row " + str(row + 1) + ", column " + str(col + 1) + ".")

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:/repos/sudoku-solver/test_missing_3r_3c.txt")

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
