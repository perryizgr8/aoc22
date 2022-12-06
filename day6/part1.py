buff = []

with open("day6/input.txt", "r") as f:
    lines = f.readlines()
    for i in range(4):
        buff.append(lines[0][i])
    if len(set(buff)) == 4:
        print(4)
    for i in range(4, len(lines[0])):
        buff.pop(0)
        buff.append(lines[0][i])
        if len(set(buff)) == 4:
            print(i + 1)
            break
