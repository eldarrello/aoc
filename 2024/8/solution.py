import itertools
s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
def eval(n):
    ps = set()
    for c in [chr(i) for i in range(ord('0'), ord('z') + 1)]:
        l = [k for k, v in m.items() if v == c]
        if len(l) > 1:
            for a, b in itertools.combinations(l, 2):
                dx, dy = a[0] - b[0], a[1] - b[1]
                for i in n:
                    if (a[0] + i * dx, a[1] + i * dy) in m:
                        ps.add((a[0] + i * dx, a[1] + i * dy))
                    if (b[0] - i * dx, b[1] - i * dy) in m:
                        ps.add((b[0] - i * dx, b[1] - i * dy))
    return len(ps)
print("Part 1:", eval(range(1, 2)))
print("Part 2:", eval(range(50)))

