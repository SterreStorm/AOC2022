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

    pos_h = knots[0][1]
    pos_t = knots[1][1]

    # loop through directions to move the head
    for direction_set in directions:
        direction, steps = direction_set

        pos_h, pos_t, positions = move_rope(pos_h, pos_t, direction, steps)
        knots[0][1] = pos_h
        knots[1][1] = pos_t

        # add all new tail positions to positions set
        for position in positions:
            tail_positions.add(position)

    # print amount of unique positions
    print(len(tail_positions))


def move_rope(pos_h, pos_t, direction, steps):
    x, y = pos_h
    a, b = pos_t
    positions = []

    for i in range(steps):
        # adjust position head
        x, y = move_head((x, y), direction)

        # calculate space between head and tail
        d_w = abs(x - a)
        d_h = abs(y - b)
        w = x - a
        h = y - b

        # tail movement

        # non-diagonal
        if d_w == 0 and d_h > 1 or d_h == 0 and d_w > 1:
            if d_w == 0:
                if h > 0:
                    b += 1
                else:
                    b -= 1
            elif d_h == 0:
                if w > 0:
                    a += 1
                else:
                    a -= 1

        # diagonaal
        elif d_w == 1 and d_h > 1:
            if w > 0:
                a += 1
            else:
                a -= 1

            if h > 0:
                b += 1
            else:
                b -= 1

        elif d_h == 1 and d_w > 1:
            if h > 0:
                b += 1
            else:
                b -= 1

            if w > 0:
                a += 1
            else:
                a -= 1

        positions.append((a, b))
        print(f"H: ({x}, {y})")
        print(f"T: ({a}, {b})")
        (print("--"))

    return (x, y), (a, b), positions


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


count_locations("input/day9full.txt", 2)
