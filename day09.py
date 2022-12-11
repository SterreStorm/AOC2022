def parse_input(filename):
    with open(filename) as f:
        direction_array = []
        for line in f:
            direction, steps = line.strip().split()
            direction_array.append([direction, int(steps)])
        return direction_array


def construct_lib(no_knots):
    knot_locations = []
    for i in range(no_knots):
        if i == 0:
            knot_locations.append(["H", (0, 0)])
        else:
            knot_locations.append([i, (0, 0)])
    return knot_locations


def count_locations(filename, no_knots):
    directions = parse_input(filename)
    tail_positions = set()
    knots = construct_lib(no_knots)
    positions = []



    # loop through directions to move the head
    for direction_set in directions:
        direction, steps = direction_set
        for step in range(steps):
            for j in range(1, len(knots)):
                if j == 1:
                    pos_1 = knots[j-1][1]
                    pos_1 = move_head((pos_1), direction)
                    knots[j-1][1] = pos_1

                    pos_2 = knots[j][1]
                    pos_2, positions = move_rope(pos_1, pos_2)
                    knots[j][1] = pos_2

                else:
                    pos_1 = knots[j - 1][1]
                    pos_2 = knots[j][1]
                    pos_2, positions = move_rope(pos_1, pos_2)
                    knots[j][1] = pos_2

                if j == len(knots) - 1:
                    # add all new tail positions to positions set
                    for position in positions:
                        tail_positions.add(position)

    # print amount of unique positions
    print(len(tail_positions))


def move_rope(pos_h, pos_t):
    x, y = pos_h
    a, b = pos_t
    positions = []

    # verschil breedte
    d_w = abs(x - a)
    w = x - a

    # verschil hoogte
    d_h = abs(y - b)
    h = y - b

    # non-diagonal
    if a == x:  # same row
        if d_h > 1:
            if h > 0:
                b += 1
            elif h < 0:
                b -= 1
    elif b == y:  # same column
        if d_w > 1:
            if w > 0:
                a += 1
            elif w < 0:
                a -= 1

    else:
        if d_w <= 1 and d_h <= 1:
            pass
        else:
            if x > a:
                a += 1
            elif x < a:
                a -= 1
            if y > b:
                b += 1
            elif y < b:
                b -= 1
    positions.append((a, b))

    return (a, b), positions


def move_head(head_coordinates, direction):
    x, y = head_coordinates
    if direction == "R" or direction == "U":
        if direction == "R":
            x += 1
        else:
            y += 1

    elif direction == "L" or direction == "D":
        if direction == "L":
            x -= 1
        else:
            y -= 1
    return x, y


count_locations("input/day9full.txt", 10)
