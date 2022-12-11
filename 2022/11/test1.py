monkey_worry_levels = {0 : [79, 98], 1 : [54, 65, 75, 74], 2: [79, 60, 97], 3: [74]}
monkey_operations = {0: "m_19", 1 : "a_6", 2: "m_old", 3: "a_3"}
monkey_tests = {0 : 23, 1 : 19, 2: 13, 3: 17}
monkey_throw_true = {0 : 2, 1: 2, 2: 1, 3: 0}
monkey_throw_false = {0 :3, 1: 0, 2: 3, 3: 1}
monkey_active_for = {0: 0, 1: 0, 2: 0,3: 0}
M = 23 * 19 * 13 * 17
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
    for m in range(0, 4): # monkeys
        worry_levels = monkey_worry_levels[m]
        while(worry_levels):
            monkey_active_for[m] = monkey_active_for[m] + 1
            worry = worry_levels.pop(0)
            operation = monkey_operations[m]
            worry_level = operate(operation, worry)
            # worry_level = int(worry_level / 3)
            worry_level = worry_level % M
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
