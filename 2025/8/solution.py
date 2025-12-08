s = open('input.txt').read().splitlines()
ps = [list(map(int, l.split(','))) for l in s]
ds = []
for i, (x1, y1, z1) in enumerate(ps):
    for j in range(i + 1, len(ps)):
        x2, y2, z2 = ps[j]
        dx = x2 - x1
        dy = y2 - y1
        dz = z2 - z1
        d = dx * dx + dy * dy + dz * dz
        ds.append((d, i, j))
c = 0
cs = {}
ijs = {}
for k, (d, i, j) in enumerate(sorted(ds)):
    if i not in ijs and j not in ijs:
        ijs[i] = c
        ijs[j] = c
        if c not in cs:
            cs[c] = set()
        cs[c].add(i)
        cs[c].add(j)
        c += 1
    elif i in ijs and j in ijs:
        c1 = ijs[i]
        c2 = ijs[j]
        if c1 != c2:
            for ij in cs[c2]:
                cs[c1].add(ij)
                ijs[ij] = c1
            del cs[c2]
    elif i in ijs:
        c1 = ijs[i]
        ijs[j] = c1
        cs[c1].add(j)
    else:
        c1 = ijs[j]
        ijs[i] = c1
        cs[c1].add(i)
    if len(list(cs.values())[0]) == len(ps):
        print("Part 2:", ps[i][0] * ps[j][0])
        break
    if k == 1000:
        ss = sorted([len(v) for v in cs.values()], reverse=True)
        print("Part 1:", ss[0] * ss[1] * ss[2])