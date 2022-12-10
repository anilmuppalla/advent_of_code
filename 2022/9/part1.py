T = H = (0,0)
visited = set()

def move_tail(H, T):
    (hx, hy) = H
    (tx, ty) = T
    if abs(hx - tx) > 1 and hy == ty:
        if (hx > tx):
            return (tx + 1, ty)
        else:
            return (tx - 1, ty)
    if abs(hy - ty) > 1 and hx == tx:
        if (hy > ty):
            return (tx, ty + 1)
        else:
            return (tx, ty - 1)
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        if (hx > tx) and (hy > ty):
            return (tx + 1, ty + 1)
        if (hx < tx) and (hy < ty):
            return (tx - 1, ty - 1)
        if (hx < tx) and (hy > ty):
            return (tx - 1, ty + 1)
        if (hx > tx) and (hy < ty):
            return (tx + 1, ty - 1)
    return (tx, ty)


def move_head(H, N):
    (hx, hy) = H
    (nx, ny) = N
    new_h = (hx + nx, hy + ny)
    new_t = move_tail(new_h, T)
    visited.add(new_t)
    print(new_h, new_t)
    return (new_h, new_t)


for line in open("/Users/zuko/Code/advent-of-code/2022/9/in.txt", "r"):
    (dir, step) = tuple(line.strip().split(" "))
    step = int(step)
    if dir == "R":
        for i in range(0, step):
            (H, T) = move_head(H, (1, 0))
    if dir == "L":
        for i in range(0, step):
            (H, T) = move_head(H, (-1, 0))
    if dir == "U":
        for i in range(0, step):
            (H, T) = move_head(H, (0, 1))
    if dir == "D":
        for i in range(0, step):
            (H, T) = move_head(H, (0, -1))

print(len(list(visited)))    

