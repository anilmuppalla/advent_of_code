max1 = 0
max2 = 0
max3 = 0
sum = 0
    

for line in open("in.txt", "r", encoding="UTF-8"):
    if line == '\n':
        if (sum > max1):
            max3 = max2
            max2 = max1
            max1 = sum
        elif (sum > max2):
            max3 = max2
            max2 = sum
        elif (sum > max3):
            max3 = sum
        sum = 0
        # print(max1, max2, max3)
    else:
        sum = sum + int(line)

if (sum > max1):
    max3 = max2
    max2 = max1
    max1 = sum
elif (sum > max2):
    max3 = max2
    max2 = sum
elif (sum > max3):
    max3 = sum

print(max1 + max2 + max3)
