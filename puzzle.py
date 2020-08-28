import numpy as np

class Puzzle:
    def load_puzzle(self, filepath):
        puzzle_file = open(filepath, "r")

        puzzle = puzzle_file.read().split("\n")

        p_array = np.empty([3, 9])
        i = 0
        while (i < len(puzzle)):
            temp_list = list(map(int, puzzle[i].split(' ')))
            p_array[i,:] = temp_list
            i += 1

        return p_array