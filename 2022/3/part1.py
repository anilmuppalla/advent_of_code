def priority(c):
    if c.islower():
        return ord(c) % 96
    else:
        return (ord(c) % 64) + 26


#[print(priority(c)) for c in ['a', 'b', "z", "A", "Z"]]

def find_common(line):
    s1 = set()
    s2 = set()
    l = len(line)
    mid = int(l / 2)
    for i in range(0, mid):
        # print(line[i], end=" ")
        s1.add(line[i])
    # print('\n')
    for j in range(mid, l):
        # print(line[j], end=" ")
        s2.add(line[j])
    # print(s1)
    # print(s2)
    # print(s1 & s2)
    return s1 & s2

total_prio = 0    
for line in open("in.txt", "r"):
    common_set = find_common(line.strip())
    common_char = common_set.pop()
    total_prio = total_prio + priority(common_char)

print(total_prio)

