def parse_input(filename):
    with open(filename) as f:
        direction_array = []
        for line in f:
            direction, steps = line.strip().split()
            direction_array.append([direction, int(steps)])
        return direction_array


def count_locations(filename):
    directions = parse_input(filename)
    tail_positions = set()

    pos_h = (0, 0)
    pos_t = (0, 0)

    # loop through directions to move the head
    for direction_set in directions:
        direction, steps = direction_set
        pos_h, pos_t, positions = move_rope(pos_h, pos_t, direction, steps)
        # add all new tail positions to positions set
        for position in positions:
            tail_positions.add(position)

    # print amount of unique positions
    print(len(tail_positions))


def move_rope(pos_h, pos_t , direction, steps):
    x, y = pos_h
    a, b = pos_t
    positions = []
    up_or_down = True # check if going + or -
    print(f"{direction}{steps} \n--")
    for i in range(steps):
        # adjust position head
        if direction == "R" or direction == "U":
            up_or_down = True
            if direction == "R":
                x += 1
            else:
                y += 1

        elif direction == "L" or direction == "D":
            up_or_down = False
            if direction == "L":
                x -= 1
            else:
                y -= 1

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


count_locations("input/day9full.txt")
