import math
s = open('input.txt').read().splitlines()
map = {(y, x):int(s[y][x]) for y in range(len(s)) for x in range(len(s[y]))}
lows = []
for yx in map.keys():
    for m in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        g = (yx[0] + m[0], yx[1] + m[1])
        if g in map and map[g] <= map[yx]:
            break
    else:
        lows.append(yx)
print("Part 1:", sum([map[p] + 1 for p in lows]))
def eval(p):
    c = set()
    nodes = [p]
    while nodes:
        p = nodes.pop(0)
        c.add(p)
        for m in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            g = (p[0] + m[0], p[1] + m[1])
            if g in map and map[g] > map[p] and map[g] < 9:
                nodes.append(g)
    return len(c)
print("Part 2:", math.prod(sorted([eval(i) for i in lows])[-3:]))

