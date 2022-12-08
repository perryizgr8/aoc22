with open("day8/input.txt", "r") as f:
    lines = f.readlines()
    n_outer = (2 * len(lines[0].rstrip())) + ((len(lines) - 2) * 2)
    print(n_outer)
    rows = []
    for line in lines:
        line = line.rstrip()
        rows.append([c for c in line])

n = len(rows)
print(f"{n}x{n} grid populated")


def vis_from_right(r, c):
    cell = rows[r][c]
    for col in range(c + 1, n):
        if cell <= rows[r][col]:
            return False
    return True


def vis_from_left(r, c):
    cell = rows[r][c]
    for col in range(0, c):
        if cell <= rows[r][col]:
            return False
    return True


def vis_from_bottom(r, c):
    cell = rows[r][c]
    for row in range(r + 1, n):
        if cell <= rows[row][c]:
            return False
    return True


def vis_from_top(r, c):
    cell = rows[r][c]
    for row in range(0, r):
        if cell <= rows[row][c]:
            return False
    return True


def is_vis(r, c):
    if vis_from_right(r, c):
        return True
    if vis_from_left(r, c):
        return True
    if vis_from_bottom(r, c):
        return True
    if vis_from_top(r, c):
        return True
    return False


n_vis = 0
for r in range(1, n - 1):
    for c in range(1, n - 1):
        # print(f"{r},{c}")
        visible = is_vis(r, c)
        if visible:
            # print("visible")
            n_vis += 1

print(n_outer + n_vis)
