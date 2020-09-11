from puzzle import Puzzle
import numpy as np

def find_least_missing(container):
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

    if lowest == 10:
        lowest = 0
    else:
        print("Found " + container + " with " + str(lowest) + " missing number(s)." )

    return n, lowest

def find_missing_values(n, container):
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

def already_exists(n, m, missing, container):
    i = 0
    
    if container == "row":
        while (i < 9):
            if puzzle[i,m] == missing:
                return True
            i += 1
        return False
    elif container == "column":
        while (i < 9):
            if puzzle[m,i] == missing:
                return True
            i += 1
        return False


def solve(n, missing, container):
    print("Solving " + container + " with " + str(len(missing)) + " missing cell(s).")

    m = 0       # corresponding row/column that references missing number
    i = 0

    if len(missing) == 1:
        while (i < 9):
            if container == "row":
                if puzzle[n,i] == 0:
                    m = i
                    break
                i += 1
            elif container == "column":
                if puzzle[i,n] == 0:
                    m = i
                    break
                i += 1
        
        if container == "row":
            puzzle[n,m] = missing[0]
        elif container == "column":
            puzzle[m,n] = missing[0]
    elif len(missing) == 2:
        while (i < 9):
            if container == "row":
                if puzzle[n,i] == 0:
                    m = i
                    break
                i += 1
            elif container == "column":
                if puzzle[i,n] == 0:
                    m = i
                    break
                i += 1
                
        if container == "row":
            if not already_exists(n, m, missing[0], container):
                puzzle[n,m] = missing[0]
            else:
                puzzle[n,m] = missing[1]
        elif container == "column":
            if not already_exists(n, m, missing[0], container):
                puzzle[m,n] = missing[0]
            else:
                puzzle[m,n] = missing[1]

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:/repos/sudoku-solver/test_full_4.txt")

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