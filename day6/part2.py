buff = []

with open("day6/input.txt", "r") as f:
    lines = f.readlines()
    for i in range(14):
        buff.append(lines[0][i])
    if len(set(buff)) == 14:
        print(4)
    for i in range(14, len(lines[0])):
        buff.pop(0)
        buff.append(lines[0][i])
        if len(set(buff)) == 14:
            print(i + 1)
            break
