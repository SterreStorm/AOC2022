import numpy as np
def overlap_area(filename):
    with open(filename) as inp:
        count = 0
        for line in inp:
            line.strip()
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            if (int(a1) <= int(b1) and int(a2) >= int(b2)) or (int(a1) >= int(b1) and int(a2) <= int(b2)):
                count += 1
        print(count)


overlap_area("input/day4full.txt")