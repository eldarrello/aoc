import math
def moves(yx):
    return [(yx[0] + m[0], yx[1] + m[1]) for m in [(-1, 0), (0, -1), (0, 1), (1, 0)]]
def eval(p):
    c = set()
    nodes = [p]
    while nodes:
        p = nodes.pop(0)
        c.add(p)
        nodes += [m for m in moves(p) if m in map and map[m] > map[p] and map[m] < 9]
    return len(c)
s = open('input.txt').read().splitlines()
map = {(y, x):int(s[y][x]) for y in range(len(s)) for x in range(len(s[y]))}
lows = [yx for yx in map.keys() if not [1 for m in moves(yx) if m in map and map[m] <= map[yx]]]
print("Part 1:", sum([map[p] + 1 for p in lows]))
print("Part 2:", math.prod(sorted([eval(i) for i in lows])[-3:]))

