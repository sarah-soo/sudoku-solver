grid0 = {
    'x': range(3),
    'y': range(3)
}

grid1 = {
    'x': range(3),
    'y': range(3, 6)
}

grid2 = {
    'x': range(3),
    'y': range(6, 9)
}

grid3 = {
    'x': range(3, 6),
    'y': range(3)
}

grid4 = {
    'x': range(3, 6),
    'y': range(3, 6)
}

grid5 = {
    'x': range(3, 6),
    'y': range(6, 9)
}

grid6 = {
    'x': range(6, 9),
    'y': range(3)
}

grid7 = {
    'x': range(6, 9),
    'y': range(3, 6)
}

grid8 = {
    'x': range(6, 9),
    'y': range(6, 9)
}

grids = (grid0, grid1, grid2, grid3, grid4, grid5, grid6, grid7, grid8)

coord = [8, 8]

counter = 0
for grid in grids:
    if coord[0] in grid['x'] and coord[1] in grid['y']:
        print(counter)
    counter += 1