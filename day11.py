import re
import math

def parse_input(filename):
    # regex matches for filtering
    monkey_match = r"Monkey (.*):"  # find monkey number
    starting_items_match = r"Starting items: (.*)"
    operation_match = r"Operation: new = (.*)" # find monkey operation
    test_match = r"Test: divisible by (.*)"
    true_match = r"If true: throw to monkey (.*)"
    false_match = r"If false: throw to monkey (.*)"

    monkey_list = []

    with open(filename) as f:
        split_monkeys = f.read().split('\n\n')
    # set monkey in dictionairy with things
    for monkey in split_monkeys:
        monkey.strip()
        monkey_no = int(re.search(monkey_match, monkey).group(1))
        starting_items = re.findall(starting_items_match, monkey) # re.findall('\d+',monkey_split[1])
        starting_items = [int(x) for x in starting_items[0].split(',')]
        operation = re.search(operation_match, monkey).group(1)
        divisible_by = int(re.search(test_match, monkey).group(1))
        if_true = int(re.search(true_match, monkey).group(1))
        if_false = int(re.search(false_match, monkey).group(1))
        inspection_count = 0

        monkey_list.append([operation, divisible_by, if_true, if_false, inspection_count, starting_items])

    return monkey_list

def solve_operation(operation, item_value):
    part_1, operator, part_2 = operation.split()

    part_1 = item_value if part_1 == "old" else int(part_1)
    part_2 = item_value if part_2 == "old" else int(part_2)
    new_value = 0

    if operator == "*":
        new_value = part_1 * part_2
    elif operator == "+":
        new_value = part_1 + part_2
    return new_value






def monkey_time(filename, rounds):
    monkey_list = parse_input(filename)
    counts = []
    # rounds
    for round in range(rounds):
        for j, monkey in enumerate(monkey_list):
            operation = monkey[0]
            divisible_by = monkey[1]
            if_true = monkey[2]
            if_false = monkey[3]
            count = 0
            items = monkey[5]

            for item in items:
                count += 1
                item = math.floor(solve_operation(operation, item))

                if item % divisible_by == 0:
                    item = item
                    monkey_list[if_true][5].append(item)
                else:
                    monkey_list[if_false][5].append(item)
            monkey_list[j][5] = []
            monkey_list[j][4] += count

    for monkey in monkey_list:
        counts.append(monkey[4])
    counts.sort(reverse= True)

    total = counts[0] * counts[1]
    print(counts)
    print(total)
















monkey_time("input/day11test.txt", 20)

