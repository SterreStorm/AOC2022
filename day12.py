from collections import deque


def parse_input(filename):
    map = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = list(line)
            for i, letter in enumerate(line):
                # set starting value to 0
                if letter == "S":
                    line[i] = 0
                # set ending value to 27
                elif letter == "E":
                    line[i] = 27
                # set a-z to 1-26 respectively
                else:
                    line[i] = ord(letter) - 96
            map.append(line)

    return map


def find_start_and_end(map):
    start_coord = (0, 0)
    end_coord = (0, 0)
    for r, row in enumerate(map):
        for v, value in enumerate(row):
            if value == 0:
                start_coord = (v, r)
                map[r][v] = 1
            if value == 27:
                end_coord = (v, r)
                map[r][v] = 26

    return start_coord, end_coord, map

def find_all_a(map):
    all_a = []
    for r, row in enumerate(map):
        for v, value in enumerate(row):
            if value == 1:
                all_a.append((v, r))
    return all_a


def get_dist(grid, start, end):
    # code from https://wooledge.org/~greg/advent/2022/12a used as learning purpose,
    # as I am not familiar with BFS or Dijkstra's algorithm
    visited = {}
    visited[start] = 0

    # form double ended queue
    to_visit = deque()
    to_visit.append(start)

    # deltas for  up, down, right, left respectively
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # loop through everything to visit and check surrounding coordinates and steps to get there
    while to_visit:
        # set current coordinate
        (cx, cy) = to_visit.popleft()
        # add coordinate and steps to get there to dictionary
        current_steps = visited[(cx, cy)]
        # loop to find coordinates around current coordinates and adding them to the to-visit
        for (dx, dy) in deltas:
            nx, ny = (cx + dx, cy + dy)
            # als al geweest of als buiten de grid, stom
            if (nx, ny) in visited or nx in [-1, len(grid[0])] or ny in [-1, len(grid)]:
                continue
            # als het verschil in value 1 of minder is mag je er heen en bint het nice
            if grid[ny][nx] - grid[cy][cx] <= 1:
                visited[(nx, ny)] = current_steps + 1
                to_visit.append((nx, ny))
                # als je er bent heb je de stanpjens
                if (nx, ny) == end:
                    return current_steps + 1

    return None


def traverse_map(filename):
    all_steps = []
    start, end, map = find_start_and_end(parse_input(filename))  # coordinate tuples for beginning and end point
    # print(get_dist(map, start, end)) # part 1
    all_a = find_all_a(map)
    for coordinate in all_a:
        steps = get_dist(map, coordinate, end)
        if steps != None:
            all_steps.append(steps)

    all_steps.sort()
    print(all_steps)



traverse_map("input/day12full.txt")
