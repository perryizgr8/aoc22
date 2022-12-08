with open("day1/input.txt", "r") as f:
    lines = f.readlines()
    cals = []
    curr_sum = 0
    for line in lines:
        if line == "\n":
            cals.append(curr_sum)
            curr_sum = 0
            continue
        curr_sum += int(line)
    cals = sorted(cals, reverse=True)
    print(cals[0] + cals[1] + cals[2])
