# A ----> rock     --> 1
# B ----> paper    --> 2
# C ----> scissors --> 3
# X ----> lose ------> 0
# Y ----> draw ------> 3
# Z ----> win  ------> 6


def outcome_score(outcome):
    if outcome == "Y":
        return 3
    if outcome == "Z":
        return 6
    if outcome == "X":
        return 0


def move_score(move):
    if move == "rock":
        return 1
    if move == "paper":
        return 2
    if move == "scissors":
        return 3


def required_move(ur_move, outcome):
    if ur_move == "A":
        if outcome == "X":
            return "scissors"
        if outcome == "Y":
            return "rock"
        if outcome == "Z":
            return "paper"
    if ur_move == "B":
        if outcome == "X":
            return "rock"
        if outcome == "Y":
            return "paper"
        if outcome == "Z":
            return "scissors"
    if ur_move == "C":
        if outcome == "X":
            return "paper"
        if outcome == "Y":
            return "scissors"
        if outcome == "Z":
            return "rock"


def round_score(line):
    score = 0
    line = line.strip().split(" ")
    ur_move = line[0]
    outcome = line[1]
    score += outcome_score(outcome)
    my_move = required_move(ur_move, outcome)
    score += move_score(my_move)
    return score


with open("day2/input.txt", "r") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += round_score(line)
    print(total)
