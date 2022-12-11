# Starting items lists your worry level for each item the monkey is currently holding in the order they will be inspected.

# Operation shows how your worry level changes as that monkey inspects an item. (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.

# After each monkey inspects an item but before it tests your worry level, your relief that the monkey's inspection didn't damage the item causes your worry level to be divided by three and rounded down to the nearest integer.

# Test shows how the monkey uses your worry level to decide where to throw an item next.
# If true shows what happens with an item
# If false shows what happens with an item

# Monkey inspects and throws all of the items it is holding one at a time and in the order listed.

# When a monkey throws an item to another monkey, the item goes on the end of the recipient monkey's list. 
    # monkey list = []

# If a monkey is holding no items at the start of its turn, its turn ends.

# Monkey 0
# if monkey list is empty go to next monkey
# perform operation
# reduce worry level / 3
# test worry level and add to the end of the correct recipient monkey list

# focus on the two most active monkeys if you want any hope of getting your stuff back. Count the total number of times each monkey inspects items over 20 rounds:

# the level of monkey business in this situation can be found by multiplying these together: 10605.

monkey_worry_levels = {0 : [57], 1 : [58, 93, 88, 81, 72, 73, 65], 2: [65, 95], 3: [58, 80, 81, 83], 4: [58,89, 90, 96, 55], 5: [66, 73, 87, 58, 62, 67], 6: [85, 55, 89], 7: [73, 80, 54, 94, 90, 52, 69, 58]}
monkey_operations = {0: "m_13", 1 : "a_2", 2: "a_6", 3: "m_old", 4: "a_3", 5: "m_7", 6: "a_4", 7: "a_7" }
monkey_tests = {0 : 11, 1 : 7, 2: 13, 3: 5, 4: 3, 5: 17, 6: 2, 7: 19}
monkey_throw_true = {0 : 3, 1: 6, 2: 3, 3: 4, 4: 1, 5: 4, 6: 2, 7: 6 }
monkey_throw_false = {0 :2, 1: 7, 2: 5, 3: 5, 4: 7, 5: 1, 6: 0, 7: 0 }
monkey_active_for = {0: 0, 1: 0, 2: 0, 3: 0, 4:0, 5: 0, 6: 0, 7: 0}

M = 11 * 7 * 13 * 5 * 3 * 17 * 2 * 19

def add_multiply(o: str, worry: int, by: int):
    if (o == "m"):
        return worry * by
    else: 
        return worry + by

def operate(operation: str, worry: int) -> int:
    o, num = operation.split('_')
    if (num == "old"):
        return add_multiply(o, worry, worry)
    else:
        return add_multiply(o, worry, int(num))
    
def test(worry: int, diby: int):
    if worry % diby == 0:
        return True
    return False

for round in range(1, 10001): # rounds
    for m in range(0, 8): # monkeys
        worry_levels = monkey_worry_levels[m]
        while(worry_levels):
            monkey_active_for[m] = monkey_active_for[m] + 1
            worry = worry_levels.pop(0)
            operation = monkey_operations[m]
            worry_level = operate(operation, worry)
            worry_level = worry_level % M
            # worry_level = int(worry_level / 3)
            test_op = monkey_tests[m]
            true_monkey = monkey_throw_true[m]
            false_monkey = monkey_throw_false[m]
            if test(worry_level, test_op):
                true_monkey_worry_levels = monkey_worry_levels[true_monkey]
                true_monkey_worry_levels.append(worry_level)
                monkey_worry_levels[true_monkey] = true_monkey_worry_levels
            else:
                false_monkey_worry_levels = monkey_worry_levels[false_monkey]
                false_monkey_worry_levels.append(worry_level)
                monkey_worry_levels[false_monkey] = false_monkey_worry_levels
             # remove processed worry level

print(monkey_active_for)
active = list(monkey_active_for.values())
active.sort(reverse=True)
top_1 = active[0]
top_2 = active[1]
print(top_1 * top_2)

