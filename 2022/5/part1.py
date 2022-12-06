test_stacks = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
main_stacks = [['Z', 'J', 'G'],['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],['F', 'P', 'M', 'C', 'L', 'G', 'R'],['L', 'F', 'B', 'W', 'P', 'H', 'M'],['G', 'C', 'F', 'S', 'V', 'Q'],['W','H', 'J','Z','M','Q','T','L'],['H','F','S','B','V'],['F','J','Z','S'],['M','C','D','P','F','H','B','T']]
stacks = main_stacks
for i in stacks:
    print(i)
print("#######")
for line in open("in.txt", "r"):
    line = line.strip()
    inst = line.split(" ")
    num_items_to_move = int(inst[1])
    from_stack = int(inst[3]) - 1
    to_stack = int(inst[5]) - 1
    for i in range(0, num_items_to_move):
        item = stacks[from_stack].pop()
        stacks[to_stack].append(item)

for i in stacks:
    print(i.pop(), end="")
