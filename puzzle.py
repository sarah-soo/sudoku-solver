from row import Row

class Puzzle:
    def __init__(self):
        self.row = []

    def load_puzzle(self, filepath):
        print("Loading puzzle...")
        puzzle_file = open(filepath, "r")

        puzzle = puzzle_file.read().split('\n')

        print("Initialising rows...")
        i = 0
        while (i < 9):
            self.row.append(Row())
            i += 1

        print("Populating rows...")
        self.row[0].populate(list(map(int, puzzle[0].split(' '))))
        self.row[1].populate(list(map(int, puzzle[1].split(' '))))
        self.row[2].populate(list(map(int, puzzle[2].split(' '))))

        return self.row