# Rock defeats Scissors 
# Paper defeats Rock
# Scissors defeats Paper

# A = Rock = X  = 1pt
# B = Paper = Y = 2pt
# C = Scissors = X = 3pt
# win = 6pts
# draw = 3pts
# loss = 0pts

#total = points of A/B/C Or X/Y/Z + win/draw/loss

# X - loss
# Y - draw
# Z - win

win = 6
loss = 0
draw = 3

rock = 1
paper = 2
scissors = 3

matrix = {
    "A" : { # rock
        "X" : loss + scissors, # loss
        "Y" : draw + rock, # draw
        "Z" : win + paper  # win
    },
    "B" : { # paper
        "X" : loss + rock, # loss
        "Y" : draw + paper, # draw
        "Z" : win + scissors  # win
    },
    "C" : { #scissors
        "X" : loss + paper, # loss
        "Y" : draw + scissors, # draw
        "Z" : win + rock  # win
    }
}

def cal_points(oppo, you):
    return matrix[oppo][you]

round = 0
for line in open("in.txt", "r"):
    (oppo, you) = tuple(line.strip().split(" "))
    pts = cal_points(oppo, you)
    round = round + pts
print(round)
    