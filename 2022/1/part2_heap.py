import heapq
heap = []
total = 0
for line in open("in.txt", "r", encoding="UTF-8"):
    if line == '\n':
        heapq.heappush(heap, total)
        total = 0
        # print(max1, max2, max3)
    else:
        total = total + int(line)

heapq.heappushpop(heap, total)
print(sum(heapq.nlargest(3, heap)))
