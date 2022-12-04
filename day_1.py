
def find_most_cals(textfile):
    # construct dictionary
    elfcount = 1
    elf_dict = {}
    calories = 0
    elf1 = 0
    elf2 = 0
    elf3 = 0
    max_calories = 0
    cal2 = 0
    cal3 = 0

    with open(textfile) as inp:
        for line in inp:
            line = line.replace("\n", "")
            try:
                calories += int(line)
                elf_dict[elfcount] = calories
            except:
                if line == "":
                    calories = 0
                    elfcount += 1

    # Find highest 3 calorie counts
    for elem in elf_dict:
        if elf_dict[elem] > max_calories:
            elf3 = elf2
            cal3 = cal2
            elf2 = elf1
            cal2 = max_calories
            max_calories = int(elf_dict[elem])
            elf1 = elem
        elif elf_dict[elem] > cal2:
            elf3 = elf2
            cal3 = cal2
            cal2 = int(elf_dict[elem])
            elf2 = elem
        elif elf_dict[elem] > cal3:
            elf3 = elem
            cal3 = elf_dict[elem]

        caloriesum = max_calories + cal2 + cal3

    print(f"the highest amount of calories is held by elf {elf1} with {max_calories} calories")
    print(f"the total calories held by top 3 elfs {elf1}, {elf2} and {elf3} with {caloriesum} calories")

find_most_cals("day1full.txt")
