def a_to_i(a):
    ascii = ord(a)
    if 97 <= ascii <= 122:
        return ascii - 96
    if 65 <= ascii <= 90:
        return ascii - 38


def common_item(bags):
    set0 = set()
    set1 = set()
    set2 = set()
    for thing in bags[0]:
        set0.add(thing)
    for thing in bags[1]:
        set1.add(thing)
    for thing in bags[2]:
        set2.add(thing)
    return (set0 & set1 & set2).pop()


with open("day3/input.txt", "r") as f:
    lines = f.readlines()
    prio_sum = 0
    g_lines = []
    for line in lines:
        g_lines.append(line.strip())
        if len(g_lines) == 3:
            badge = common_item(g_lines)
            prio_sum += a_to_i(badge)
            g_lines = []

    print(prio_sum)
