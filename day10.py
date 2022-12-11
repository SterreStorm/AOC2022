import re


def run(filename):
    cycle = 1
    x = 1
    cycle_values = []
    # regex
    add_match = r"^addx (.*)"
    noop_match = r"^noop"

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if re.match(noop_match, line):  # noop cycle
                cycle_values.append([cycle, x])
                cycle += 1


            else: # addx cycle
                v = int(re.search(add_match, line).group(1))
                cycle_values.append([cycle, x])
                cycle += 1
                cycle_values.append([cycle, x])
                cycle += 1
                x += v

    return cycle_values


def calculate_signal_strength(filename, location_array):
    cycle_values = run(filename)
    signal_strength = 0
    for number in location_array:
        for cycle in cycle_values:
            if cycle[0] == number:
                cycle_strength = cycle[0] * cycle[1]
                signal_strength += cycle_strength
                print(number, cycle_strength)
                continue

    print(signal_strength)




location_array = [20, 60, 100, 140, 180, 220]

calculate_signal_strength("input/day10full.txt", location_array)