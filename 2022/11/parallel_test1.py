import multiprocessing as mp
import pprint

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

def mapper(data, m):
    print("Executing monkey: ", m)
    worry_levels = data['monkey_worry_levels'][m]
    while(worry_levels):
        data["monkey_active_for"][m] = data["monkey_active_for"][m] + 1
        worry = worry_levels.pop(0)
        operation = data["monkey_operations"][m]
        worry_level = operate(operation, worry)
        # worry_level = int(worry_level / 3)
        test_op = data["monkey_tests"][m]
        true_monkey = data["monkey_throw_true"][m]
        false_monkey = data["monkey_throw_false"][m]
        if test(worry_level, test_op):
            true_monkey_worry_levels = data["monkey_worry_levels"][true_monkey]
            true_monkey_worry_levels.append(worry_level)
            data["monkey_worry_levels"][true_monkey] = true_monkey_worry_levels
        else:
            false_monkey_worry_levels = data["monkey_worry_levels"][false_monkey]
            false_monkey_worry_levels.append(worry_level)
            data["monkey_worry_levels"][false_monkey] = false_monkey_worry_levels
    # print(data["monkey_active_for"])


if __name__ == '__main__':
    processes = []
    manager = mp.Manager()
    data = manager.dict()
    data["monkey_worry_levels"] = {0 : [79, 98], 1 : [54, 65, 75, 74], 2: [79, 60, 97], 3: [74]}
    data["monkey_operations"] = {0: "m_19", 1 : "a_6", 2: "m_old", 3: "a_3"}
    data["monkey_tests"] = {0 : 23, 1 : 19, 2: 13, 3: 17}
    data["monkey_throw_true"] = {0 : 2, 1: 2, 2: 1, 3: 0}
    data["monkey_throw_false"] = {0 :3, 1: 0, 2: 3, 3: 1}
    data["monkey_active_for"] = {0: 0, 1: 0, 2: 0,3: 0}


    for i in range(0, 4):
        p = mp.Process(target=mapper, args=(data, i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()
    
    pprint.pprint(dict(data)["monkey_worry_levels"])
    