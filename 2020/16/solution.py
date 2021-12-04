ranges = []
valid = []
acc = 0
h = [[] for i in range(20)]
for line in open('input.txt').read().splitlines():
    if ' or ' in line:
        _, b = line.split(':')
        ranges.append([[int(x) for x in r.split('-')] for r in b.split(' or ')])
    elif ',' in line:
        fs = [int(x) for x in line.split(',')]
        w = []
        for u in fs:
            found = False
            for r in ranges:
                if ((u >= r[0][0] and u <= r[0][1]) or (u >= r[1][0] and u <= r[1][1])):
                    found = True
                else:
                    w.append((ranges.index(r), fs.index(u)))
            if found == False:
                acc += u
                break
        else:
            [h[i[0]].append(i[1]) for i in w]
            valid.append(fs)
print("Part 1:", acc)
acc = 1
for k in range(20):
    for i in h:
        if len(i) == 19:
            m = list(set(range(20)) - set(i))[0]
            if h.index(i) < 6:
                acc *= valid[0][m]
            [l.append(m) for l in h]
print("Part 2:", acc)