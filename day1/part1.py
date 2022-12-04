with open("day1/input.txt", "r") as f:
    lines = f.readlines()
    max_sum = 0
    curr_sum = 0
    for line in lines:
        if line == "\n":
            max_sum = max(max_sum, curr_sum)
            curr_sum = 0
            continue
        curr_sum += int(line)
    print(max_sum)
