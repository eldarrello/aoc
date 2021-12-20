add = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])
oris = lambda x, y, z: [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y), (-x, -y, z), (-x, -z, -y), (-x, y, -z), (-x, z, y),
        (y, -x, z), (y, z, x), (y, x, -z), (y, -z, -x), (-y, x, z), (-y, -z, x), (-y, -x, -z), (-y, z, -x),
        (z, y, -x), (z, x, y), (z, -y, x), (z, -x, -y), (-z, -y, -x), (-z, -x, y), (-z, y, x), (-z, x, -y)]
def get_dif(a, b):
    for o in range(24):
        m = {}
        for x, y, z in a:
            for x1, y1, z1 in ss[b][o]:
                d = (x - x1, y - y1, z - z1)
                m[d] = 1 if d not in m else (m[d] + 1)
                if m[d] >= 12:
                    return d, o
ss = [[[oris(*list(map(int, k.split(','))))[v] for k in i.splitlines() if ('---') not in k] for v in range(24)] for i in open('input.txt').read().split('\n\n')]
pos = {0: (0, 0, 0)}
ps = set(ss[0][0])
nodes = [(0, 0)]
while nodes:
    node, o = nodes.pop()
    for next in [i for i in range(30) if i not in pos]:
        if d := get_dif(ss[node][o], next):
            pos[next] = add(pos[node], d[0])
            nodes.append((next, d[1]))
            ps |= {add(pos[next], p) for p in ss[next][d[1]]}
print("Part 1:", len(ps))
print("Part 2:", max([abs(pos[a][0] - pos[b][0]) + abs(pos[a][1] - pos[b][1]) + abs(pos[a][2] - pos[b][2]) for a in range(30) for b in range(30)]))