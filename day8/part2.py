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


def vdist_from_right(r, c):
    d = 0
    cell = rows[r][c]
    for col in range(c + 1, n):
        d += 1
        if cell <= rows[r][col]:
            return d
    return d


def vdist_from_left(r, c):
    d = 0
    cell = rows[r][c]
    for col in reversed(range(0, c)):
        d += 1
        if cell <= rows[r][col]:
            return d
    return d


def vdist_from_bottom(r, c):
    d = 0
    cell = rows[r][c]
    for row in range(r + 1, n):
        d += 1
        if cell <= rows[row][c]:
            return d
    return d


def vdist_from_top(r, c):
    d = 0
    cell = rows[r][c]
    for row in reversed(range(0, r)):
        d += 1
        if cell <= rows[row][c]:
            return d
    return d


def vdist(r, c):
    return (
        vdist_from_right(r, c)
        * vdist_from_left(r, c)
        * vdist_from_bottom(r, c)
        * vdist_from_top(r, c)
    )


maxd = 0
# vdist(2,1)
for r in range(1, n - 1):
    for c in range(1, n - 1):
        # print(f"{r},{c}")
        maxd = max(maxd, vdist(r, c))

print(maxd)
