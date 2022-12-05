
# # function to find common denominator in compartments
# def find_common_denominator_bag(line):
#     common_denominator = ""
#     string1 = line[:len(line)//2]
#     string2 = line[len(line)//2:]
#     for letter1 in string1:
#         for letter2 in string2:
#             if letter1 == letter2:
#                 common_denominator = letter1
#     return common_denominator
#
#
# # compile and convert list of denominators
# def rugzak_value(filename):
#     list_of_denoms = []
#     rugzakvalue = 0
#     with open(filename) as inp:
#         for line in inp:
#             line = line.strip()
#             temp_denom = find_common_denominator_bag(line)
#             list_of_denoms.append(temp_denom)
#
#     for elem in list_of_denoms:
#
#         if elem.isupper():
#             tempvalue = (ord(elem) - 38)
#             rugzakvalue += tempvalue
#         elif elem.islower():
#             tempvalue = (ord(elem) - 96)
#             rugzakvalue += tempvalue
#     print(rugzakvalue)

def find_common_denominator_group(array_list):
    string1, string2, string3 = array_list
    string1 = set(string1)
    string2 = set(string2)
    string3 = set(string3)

    common_denominator = string1 & string2 & string3
    return common_denominator.pop()


def rugzak_value_group(filename):

    list_of_denoms = []
    rugzakvalue = 0

    # construct array of common denominators
    with open(filename) as inp:
        linecount = 0
        group_list = []
        for line in inp:
            line = line.strip()
            group_list.append(line)
            linecount += 1
            if linecount == 3:
               linecount = 0
               temp_denom = find_common_denominator_group(group_list)
               list_of_denoms.append(temp_denom)
               group_list = []

    # find value
    for elem in list_of_denoms:

        if elem.isupper():
            tempvalue = (ord(elem) - 38)
            rugzakvalue += tempvalue
        elif elem.islower():
            tempvalue = (ord(elem) - 96)
            rugzakvalue += tempvalue
    print(rugzakvalue)

rugzak_value_group("Input/day3full.txt")





