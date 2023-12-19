import math
a, b = open('input.txt').read().split('\n\n')
f = {}
for i in a.splitlines():
    key, r = i.split('{')
    f[key] = r[:-1].split(',')
acc2 = 0
acc1 = 0
nodes = [('in', [])]
while nodes:
    key, conds = nodes.pop()
    for k in f[key]:
        cond = 'x>0'
        if ':' in k:
            cond, k = k.split(':')
        if k == 'A':
            d = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
            for k in conds + [cond]:
                for c, y in {'>=': (0, max, 0), '>': (0, max, 1), '<=': (1, min, 0), '<': (1, min, -1)}.items():
                    if c in k:
                        l, v = k.split(c)
                        d[l][y[0]] = y[1](d[l][y[0]], int(v) + y[2])
                        break
            acc2 += math.prod([max(0, high - low + 1) for low, high in d.values()])
            for i in b.splitlines():
                acc = 0
                for c in i[1:-1].split(','):
                    k, v = c.split('=')
                    acc += int(v) if d[k][0] <= int(v) <= d[k][1] else -4 * 4000
                acc1 += max(0, acc)
        elif k != 'R':
            nodes.append((k, conds  + [cond]))
        conds.append([cond.replace(k, v) for k, v in {'>=':'<', '<=':'>', '>':'<=', '<':'>='}.items() if k in cond][0])
print("Part 1:", acc1)
print("Part 2:", acc2)



