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
    for k in range(i+1, num_rows):
        if forest[k][j] >= forest[i][j]:
            return False 
    return True

def check_bottom(i,j):
    for k in range(0, i):
        if forest[k][j] >= forest[i][j]:
            return False
    return True 

def check_right(i,j):
    for k in range(j+1, num_columns):
        if forest[i][k] >= forest[i][j]:
            return False 
    return True

def check_left(i,j):
    for k in range(0, j):
        if forest[i][k] >= forest[i][j]:
            return False
    return True


def check_visible(i,j):
    return check_left(i,j) or check_right(i,j) or check_bottom(i,j) or check_top(i,j)

for i in range(1, num_rows - 1):
    for j in range(1, num_columns - 1):
        if check_visible(i,j):
            total += 1

            

print(total)