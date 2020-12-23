import numpy as np

puzzle_file = open("C:/repos/sudoku-solver/medium_3.txt", "r")

puzzle = puzzle_file.read().split("\n")

p_array = np.empty([9, 9])
i = 0
while (i < len(puzzle)):
    temp_list = list(map(int, puzzle[i].split(' ')))
    p_array[i,:] = temp_list
    i += 1

count = 0
for i in range(9):
    for j in range(9):
        if p_array[i, j] == 0:
            count += 1

print(count)
