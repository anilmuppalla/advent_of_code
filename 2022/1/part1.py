maxVal = 0
sum = 0

for line in open("test.txt", "r", encoding="UTF-8"):
    if line == '\n':
        print(sum)
        maxVal = max(maxVal, sum)
        sum = 0
    else:
        sum = sum + int(line)

print(sum)
maxVal = max(maxVal, sum)
print(maxVal)
# print(maxVal)
