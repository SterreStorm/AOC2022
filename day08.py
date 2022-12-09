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

# day 2
def best_score(filename):
    grid = grid_make(filename)
    verical_grid = rotate_grid(grid)
    total_values = {}

    hor_1 = scenic_calc(grid, 1)
    hor_2 = scenic_calc(grid, -1)
    ver_1 = scenic_calc(verical_grid, 1, True)
    ver_2 = scenic_calc(verical_grid, -1, True)

    for coordinate in hor_1:
        total_values[coordinate] = hor_1[coordinate] * hor_2[coordinate] * ver_1[coordinate] * ver_2[coordinate]

    highest_scenic = max(total_values.values())
    print(highest_scenic)

def scenic_calc(grid, direction, vert: bool = False):
    scenicscore = {}

    for row in grid:
        y = grid.index(row)
        if direction == -1:
            row = list(reversed(row))
        # run through row by row
        for i in range(len(row)):
            value = row[i]
            direction_score = 0
            blocked = False

            #check how many visible
            for element in row[i + 1: len(row)]:
                if not blocked:
                    if value > element:
                        direction_score += 1
                    elif value <= element:
                        direction_score += 1
                        blocked = True

            x = i
            if direction == -1:
                x = len(row) - 1 - i

            if not vert:
                scenicscore[(x, y)] = direction_score
            else:
                scenicscore[(y, x)] = direction_score
    return scenicscore



best_score("input/day8full.txt")
