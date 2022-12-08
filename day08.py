def grid_make(filename):
    grid = []
    height = 0
    with open(filename) as f:
        for line in f:
            height += 1
            line = line.strip()
            line = list(line)
            line = [int(x) for x in line]
            grid.append(line)
    return grid


def rotate_grid(grid):
    vertical_grid = []
    for i in range(len(grid)):
        temparray = []
        for j in range(len(grid)):
            tempvar = grid[j][i]
            temparray.append(tempvar)
        vertical_grid.append(temparray)
    return vertical_grid


def find_coord(grid, direction: int):
    tree_coordinates = []
    for row in grid:
        y = grid.index(row)
        if direction == - 1:
            row = list(reversed(row))

        for i in range(len(row)):
            bigger = True
            value = row[i]
            for element in row[i + 1: len(row)]:
                if value <= element:
                    bigger = False

            if bigger:
                if direction == -1:
                    i = len(row) - i - 1
                tree_coordinates.append((i, y))

    return tree_coordinates


def boompjens_telle(filename):
    grid = grid_make(filename)
    vertical_grid = rotate_grid(grid)
    hor_coord = []
    vert_coord = []
    tot_coord = set()

    hor_coord.append(find_coord(grid, -1))
    hor_coord.append(find_coord(grid, 1))
    vert_coord.append(find_coord(vertical_grid, 1))
    vert_coord.append(find_coord(vertical_grid, -1))

    for list in vert_coord:
        for coord in list:
            y, x = coord
            tot_coord.add((x, y))
    for list in hor_coord:
        for coord in list:
            tot_coord.add(coord)

    visible_trees = len(tot_coord)
    print(visible_trees)

    return tot_coord


def scenic_calc(filename):
    list_of_coords = boompjens_telle(filename)


boompjens_telle("input/day8full.txt")

