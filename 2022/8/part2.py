forest = []
for line in open("/Users/zuko/Code/advent-of-code/2022/8/in.txt", "r"):
    row = []
    for num in line.strip():
        row.append(int(num))
    forest.append(row)

num_rows = len(forest)
num_columns = len(forest[0])

total = 2 * num_rows + 2 * num_columns - 4


def check_top(i,j):
    c = 0
    for k in range(i+1, num_rows):
        c += 1
        if forest[k][j] >= forest[i][j]:
            break
    return c

def check_bottom(i,j):
    c = 0
    for k in range(i-1, -1, -1):
        c += 1
        if forest[k][j] >= forest[i][j]:
            break
    return c

def check_right(i,j):
    c = 0
    for k in range(j+1, num_columns):
        c += 1
        if forest[i][k] >= forest[i][j]:
            break
    return c

def check_left(i,j):
    c = 0
    for k in range(j-1, -1, -1):
        c += 1
        if forest[i][k] >= forest[i][j]:
            break
    return c


def scenic_score(i,j):
    return check_left(i,j) * check_right(i,j) * check_bottom(i,j) * check_top(i,j)

max = 0
for i in range(1, num_rows - 1):
    for j in range(1, num_columns - 1):
        score = scenic_score(i,j)
        if score > max:
            max = score

print(max)