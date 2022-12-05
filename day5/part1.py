from parse import parse


def get_crates(line):
    n_stacks = int((len(line) + 1) / 4)
    crates = []
    for i in range(n_stacks):
        # 1 5 9 13...
        crates.append(line[1 + (i * 4)])
    return crates


def get_n_stacks(line):
    return int((len(line) + 1) / 4)


def get_move(line):
    res = parse("move {} from {} to {}", line)
    return int(res[0]), int(res[1]), int(res[2])


def perform_move(stacks, line):
    n, src, dst = get_move(line)
    for _ in range(n):
        crate = stacks[src - 1].pop()
        stacks[dst - 1].append(crate)
    return stacks


with open("day5/input.txt", "r") as f:
    lines = f.readlines()
    n_stacks = get_n_stacks(lines[0])
    stacks = [[] for x in range(n_stacks)]
    moving = False
    for line in lines:
        if line == "\n":
            continue
        if not moving and line[1] == "1":
            # end of crate stacks
            stacks = [stack[::-1] for stack in stacks]
            moving = True
            continue
        if not moving:
            crates = get_crates(line.rstrip())
            for c in range(n_stacks):
                if crates[c] != " ":
                    stacks[c].append(crates[c])
        else:
            stacks = perform_move(stacks, line.rstrip())
    tops = [stack.pop() for stack in stacks]
    tops_str = ""
    for top in tops:
        tops_str += top
    print(tops_str)
