# if a group's badge is item type B, 
# then all three Elves will have item type B somewhere in their rucksack

# The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

def priority(c):
    if c.islower():
        return ord(c) % 96
    else:
        return (ord(c) % 64) + 26


#[print(priority(c)) for c in ['a', 'b', "z", "A", "Z"]]

def find_common(lines) -> set:
    # print(lines)
    s1 = set()
    s2 = set()
    s3 = set()
    for i in lines[0]:
        # print(line[i], end=" ")
        s1.add(i)
    for i in lines[1]:
        # print(line[i], end=" ")
        s2.add(i)
    for i in lines[2]:
        # print(line[i], end=" ")
        s3.add(i)
    return s1 & s2 & s3

i = 0
lines = []
total_prio = 0
for line in open("in.txt", "r"):
    lines.append(line.strip())
    if i == 2:
        common_set = find_common(lines)
        common_char = common_set.pop()
        total_prio = total_prio + priority(common_char)
        i = 0
        lines = []
    else: 
        i = i + 1

print(total_prio)
