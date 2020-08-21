from subgrid import Subgrid

row1 = [1,2,3,4,5,6,7,8,9]
row2 = [4,5,6,7,8,9,1,2,3]
row3 = [7,8,9,1,2,3,4,5,6]

tl = Subgrid()
tm = Subgrid()
tr = Subgrid()

tl.populate(row1, row2, row3, "tl")
tm.populate(row1, row2, row3, "tm")
tr.populate(row1, row2, row3, "tr")

tl.check_if_complete()
tm.check_if_complete()
tr.check_if_complete()

print(tl.complete, tm.complete, tr.complete)
