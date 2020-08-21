from subgrid import Subgrid
from puzzle import Puzzle

p = Puzzle()

p.load_puzzle("C:\\repos\\sudoku-solver\\test_puzzle_1.txt")

tl = Subgrid()
tm = Subgrid()
tr = Subgrid()

# make this shorter
tl.populate(p.row[0].content, p.row[1].content, p.row[2].content, "tl")
tm.populate(p.row[0].content, p.row[1].content, p.row[2].content, "tm")
tr.populate(p.row[0].content, p.row[1].content, p.row[2].content, "tr")

tl.check_if_complete()
tm.check_if_complete()
tr.check_if_complete()

print(tl.complete, tm.complete, tr.complete)

# ideas:
#   - create superclass for methods like "check_if_complete"