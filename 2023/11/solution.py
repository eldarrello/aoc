import itertools
s = open('input.txt').read().splitlines()
m = [(x, y) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '#']
cols = [x for x in range(len(s[0])) if x not in [p[0] for p in m]]
rows = [y for y in range(len(s)) if y not in [p[1] for p in m]]
def eval(n):
    acc = 0
    for (x1, y1), (x2, y2) in itertools.combinations(m, 2):
        acc += sum([n - 1 for x in range(min(x1, x2), max(x1, x2)) if x in cols])
        acc += sum([n - 1 for y in range(min(y1, y2), max(y1, y2)) if y in rows])
        acc += abs(x2 - x1) + abs(y2 - y1)
    return acc
print("Part 1:", eval(2))
print("Part 2:", eval(1000000))



