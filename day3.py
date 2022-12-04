
# function to find common denominator in compartments
def find_common_denominator(line):
    common_denominator = ""
    line = line.strip()
    string1 = line[:len(line)//2]
    string2 = line[len(line)//2:]
    for letter1 in string1:
        for letter2 in string2:
            if letter1 == letter2:
                common_denominator = letter1
    return common_denominator

# compile and convert list of denominators
def rugzak_value(filename):
    list_of_denoms = []
    rugzakvalue = 0
    with open(filename) as inp:
        for line in inp:
            line = line.strip()
            temp_denom = find_common_denominator(line)
            list_of_denoms.append(temp_denom)

    for elem in list_of_denoms:

        if elem.isupper():
            tempvalue = (ord(elem) - 38)
            rugzakvalue += tempvalue
        elif elem.islower():
            tempvalue = (ord(elem) - 96)
            rugzakvalue += tempvalue
    print(rugzakvalue)

    print(list_of_denoms)

rugzak_value("day3full.txt")




