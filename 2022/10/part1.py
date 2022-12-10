# The CPU has a single register, X, which starts with the value 1.
# addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# noop takes one cycle to complete. It has no other effect.

wanted_cycles = set([20, 60, 100, 140, 180, 220])

def cal_sig_strength(current_cycle, X):
    print("c:{}, x:{}".format(current_cycle, X))
    if (current_cycle in wanted_cycles):
        return current_cycle * X
    return 0

def compute_signal_strength():
    X = 1
    current_cycle = 0
    sum = 0
    for line in open("/Users/zuko/Code/advent-of-code/2022/10/in.txt", "r"):
        line = line.strip()
        if (line == "noop"):
            current_cycle = current_cycle + 1
            sum = sum + cal_sig_strength(current_cycle, X)
        else:
            inst, V = line.split(" ")
            current_cycle = current_cycle + 1
            sum = sum + cal_sig_strength(current_cycle, X)
            current_cycle = current_cycle + 1
            sum = sum + cal_sig_strength(current_cycle, X)
            X = X + int(V)
        print("c:{}, x:{}".format(current_cycle, X))
    
    return sum

print(compute_signal_strength())
        
        


