from subgrid import Subgrid
from puzzle import Puzzle
from row import Row
import numpy as np

def find_least_missing_row(puzzle):
    row_n = 0
    lowest = 9
    count = 0
    i = 0
    j = 0

    while (i < 3):
        while (j < 9):
            if puzzle[i,j] == 0:
                count += 1
            j += 1
        if (count != 0) and (count < lowest):
            lowest = count
            row_n = i
        i += 1
        j = 0
        count = 0

    return row_n


def find_missing_values_from_row(puzzle, row_n):
    i = 0
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while (i < 9):
        j = 1
        while (j <= 9):
            if puzzle[row_n,i] == j:
                missing.remove(j)
                break
            j += 1
        i += 1
    return missing


def solve_row(row_n, missing):
    col0 = 0
    i = 0
    while (i < 9):
        if puzzle[row_n,i] == 0:
            col0 = i
            break
        i += 1
    
    puzzle[row_n,col0] = missing[0]

print("Loading puzzle...")
p = Puzzle()
puzzle = p.load_puzzle("C:\\repos\\sudoku-solver\\test_puzzle_1.txt")

row_n = find_least_missing_row(puzzle)

missing = find_missing_values_from_row(puzzle, row_n)

solve_row(row_n, missing)

print(puzzle)