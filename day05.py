import re
import pandas as pd
import numpy as np


def create_matrices(filename):
    sequencematrix = []
    stacks = []
    M1 = []
    with open(filename) as inp:
        crates, directions = inp.read().split("\n\n")

    # het nice maken
    crates = crates.split('\n')
    for elem in crates:
        tempmatrix = []
        for i in range(len(elem)):
            if i % 4 == 1:
                tempmatrix.append(elem[i])
        M1.append(tempmatrix)
    # stonx
    for i in range(int(M1[-1][-1])):
        temparray = []
        for j in range(len(M1) - 1):
            try:
                tempvar = M1[j][i]
                if tempvar != " ":
                    temparray.append(tempvar)
            except IndexError:
                pass
        temparray.reverse()
        stacks.append(temparray)

    # find directions matrix
    directions = directions.split('\n')
    for line in directions:
        reg = re.findall(r"\d+", line)
        sequence = [int(x) for x in reg]
        sequencematrix.append(sequence)
    return stacks, sequencematrix


def doe_dan(filename):
    stacks, directions = create_matrices(filename)

    # big moving things
    for elem in directions:
        count = elem[0] # only for pt 2
        for i in range(0, elem[0]):
            # pt 1 1
            # stacks[elem[2] - 1].append(stacks[elem[1] - 1][- 1])
            # stacks[elem[1] - 1].pop()
            stacks[elem[2] - 1].append(stacks[elem[1] - 1][- count])
            stacks[elem[1] - 1].pop(- count)
            count -= 1
    print(stacks)

    # antwoordje zoeken denk
    answer = []
    for elem in stacks:
        answer.append(elem[-1])
    print(answer)


doe_dan("input/day5full.txt")
