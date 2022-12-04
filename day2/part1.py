# A, X -> rock     --> 1
# B, Y -> paper    --> 2
# C, Z -> scissors --> 3
# lose --------------> 0
# draw --------------> 3
# win  --------------> 6


def rps_outcome(ur_move, my_move):
    if ur_move == "A":
        if my_move == "X":
            return "draw"
        if my_move == "Y":
            return "win"
        if my_move == "Z":
            return "lose"
    if ur_move == "B":
        if my_move == "Y":
            return "draw"
        if my_move == "Z":
            return "win"
        if my_move == "X":
            return "lose"
    if ur_move == "C":
        if my_move == "Z":
            return "draw"
        if my_move == "X":
            return "win"
        if my_move == "Y":
            return "lose"


def outcome_score(outcome):
    if outcome == "draw":
        return 3
    if outcome == "win":
        return 6
    if outcome == "lose":
        return 0


def move_score(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    if move == "Z":
        return 3


def round_score(line):
    score = 0
    line = line.strip().split(" ")
    ur_move = line[0]
    my_move = line[1]
    outcome = rps_outcome(ur_move, my_move)
    score += outcome_score(outcome)
    score += move_score(my_move)
    return score


with open("day2/input.txt", "r") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += round_score(line)
    print(total)
