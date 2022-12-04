def a_to_i(a):
    ascii = ord(a)
    if 97 <= ascii <= 122:
        return ascii - 96
    if 65 <= ascii <= 90:
        return ascii - 38


def priority_of_common_item(things):
    n_things = len(things)
    left = set()
    right = set()
    for i in range(n_things // 2):
        left.add(things[i])
    for i in range(n_things // 2, n_things):
        right.add(things[i])
    common_item = left & right
    return a_to_i(common_item.pop())


with open("day3/input.txt", "r") as f:
    total = 0
    lines = f.readlines()
    for line in lines:
        total += priority_of_common_item(line.strip())
    print(total)
