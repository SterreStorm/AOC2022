def full_overlap(filename):
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


full_overlap("input/day4full.txt")

def partial_overlap(filename):
    with open(filename) as inp:
        count = 0
        for line in inp:
            line.strip()
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")
            if int(a1) <= int(b2) and int(a2) >= int(b1):
                count += 1
        print(count)


partial_overlap("input/day4full.txt")