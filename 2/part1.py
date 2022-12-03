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

matrix = {
    "A" : {
        "X" : 3 + 1,
        "Y" : 6 + 2,
        "Z" : 0 + 3
    },
    "B" : {
        "X" : 0 + 1,
        "Y" : 3 + 2,
        "Z" : 6 + 3
    },
    "C" : {
        "X" : 6 + 1,
        "Y" : 0 + 2,
        "Z" : 3 + 3
    }
}

round = 0
for line in open("in.txt", "r"):
    (oppo, you) = tuple(line.strip().split(" "))
    round = round + matrix[oppo][you]
print(round)
    