add = lambda a, b: (a[0] + b[0], a[1] + b[1], a[2] + b[2])
oris = lambda x, y ,z: [(x, y, z), (x, z, -y), (x, -y, -z), (x, -z, y), (-x, -y, z), (-x, -z, -y), (-x, y, -z), (-x, z, y),
        (y, -x, z), (y, z, x), (y, x, -z), (y, -z, -x), (-y, x, z), (-y, -z, x), (-y, -x, -z), (-y, z, -x),
        (z, y, -x), (z, x, y), (z, -y, x), (z, -x, -y), (-z, -y, -x), (-z, -x, y), (-z, y, x), (-z, x, -y)]
s = open('input.txt').read().split('\n\n')
ss = []
for i in s:
    vars = []
    for v in range(24):
        bs = []
        for k in i.splitlines():
            if ('---') in k:
                continue
            x, y, z = list(map(int, k.split(',')))
            bs.append(oris(x, y, z)[v])
        vars.append(bs)
    ss.append(vars)

def get_dif(a, b):
    for o in range(24):
        m = {}
        for x, y, z in a:
            for x1, y1, z1 in ss[b][o]:
                d = (x - x1, y - y1, z - z1)
                m[d] = 1 if d not in m else (m[d] + 1)
                if m[d] >= 12:
                    orientations[b] = o
                    return d
scanners = range(len(s))
pos = {0:(0, 0, 0)}
orientations = {0: 0}
not_found = list(scanners)
ps = set()
nodes = [0]
while nodes:
    node = nodes.pop()
    for next in list(not_found):
        d = get_dif(ss[node][orientations[node]], next)
        if d:
            pos[next] = add(pos[node], d)
            not_found.remove(next)
            nodes.append(next)
            for d in ss[next][orientations[next]]:
                ps.add(add(pos[next], d))
print("Part 1:", len(ps))
max_d = 0
for i in scanners:
    x, y, z = pos[i]
    for k in scanners:
        dx, dy, dz = pos[k]
        max_d = max(max_d, abs(x - dx) + abs(y - dy) + abs(z - dz))
print("Part 2:", max_d)