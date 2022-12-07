# the start of a packet is indicated by a sequence of four characters that are all different.
# your subroutine needs to identify the first position where the four most recently received characters were all different


for line in open("in.txt", "r"):
    seen = []
    index = -1
    for c in line.strip():
        if len(seen) == 14:
            break
        index = index + 1
        while c in seen:
            seen.pop(0)
            # print(seen)
        seen.append(c)
        # print(seen)
    # print(seen)
    print(index+1)

        
