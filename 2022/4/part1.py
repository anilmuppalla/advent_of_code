# elf1
# elf2

# elf2.start >= elf1.start && elf2.end <= elf1.end  then elf1 contains elf2
# elf1.start >= elf2.start && elf1.end <= elf2.end  then elf2 contains elf1

total_pairs = 0
for line in open("in.txt", "r"):
    (elf1, elf2) = tuple(line.strip().split(","))
    (elf1_start, elf1_end) = tuple(elf1.split("-"))
    (elf2_start, elf2_end) = tuple(elf2.split("-"))
    if (int(elf2_start) >= int(elf1_start) and int(elf2_end) <= int(elf1_end)):
        total_pairs = total_pairs + 1
    elif (int(elf1_start) >= int(elf2_start) and int(elf1_end) <= int(elf2_end)):
        total_pairs = total_pairs + 1

print(total_pairs)