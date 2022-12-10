#  If the sprite is positioned such that one of its three pixels is the pixel currently being drawn, the screen produces a lit pixel (#); otherwise, the screen leaves the pixel dark (.)

# if current_cycle = X or X+1 or X+2 then "#" else "."

def jump_line(crt):
    if (crt % 40 == 0):
        print("\n")
    return crt % 40

def draw_pixel(crt, X):
    if crt == X-1 or crt == X or crt == X+1:
        print("#" , end="")
    else:
        print(".", end="")

def compute_signal_strength():
    X = 1
    current_cycle = 1
    crt = 0
    for line in open("/Users/zuko/Code/advent-of-code/2022/10/in.txt", "r"):
        line = line.strip()
        if (line == "noop"):
            current_cycle = current_cycle + 1
            draw_pixel(crt, X)
            crt = crt + 1
            crt = jump_line(crt)
        else:
            inst, V = line.split(" ")
            current_cycle = current_cycle + 1
            draw_pixel(crt, X)
            crt = crt + 1
            crt = jump_line(crt)
            current_cycle = current_cycle + 1
            draw_pixel(crt, X)
            crt = crt + 1
            crt = jump_line(crt)
            X = X + int(V)

compute_signal_strength()

        
        


