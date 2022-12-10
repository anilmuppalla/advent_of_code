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
    return new_h

def do_work():
    H = (0,0)
    T = [(0,0) for x in range(0, 9)]
    for line in open("/Users/zuko/Code/advent-of-code/2022/9/in.txt", "r"):
        (dir, step) = tuple(line.strip().split(" "))
        step = int(step)
        if dir == "R":
            for i in range(0, step):
                H = move_head(H, (1, 0))
                T[0] = move_tail(H, T[0])
                for i in range(1, 9):
                    T[i] = move_tail(T[i-1], T[i])
                visited.add(T[8])
        if dir == "L":
            for i in range(0, step):
                H = move_head(H, (-1, 0))
                T[0] = move_tail(H, T[0])
                for i in range(1, 9):
                    T[i] = move_tail(T[i-1], T[i])
                visited.add(T[8])
        if dir == "U":
            for i in range(0, step):
                H = move_head(H, (0, 1))
                T[0] = move_tail(H, T[0])
                for i in range(1, 9):
                    T[i] = move_tail(T[i-1], T[i])
                visited.add(T[8])
        if dir == "D":
            for i in range(0, step):
                H = move_head(H, (0, -1))
                T[0] = move_tail(H, T[0])
                for i in range(1, 9):
                    T[i] = move_tail(T[i-1], T[i])
                visited.add(T[8])

do_work()                                
print(len(list(visited)))    

