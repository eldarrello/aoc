a, b = open('input.txt').read().split('\n\n')
f = {}
for i in a.splitlines():
    key, r = i.split('{')
    f[key] = r[:-1].split(',')
acc1 = 0
for i in b.splitlines():
    for c in i[1:-1].split(','):
        exec(c)
    key = 'in'
    while key not in 'AR':
        w = f[key]
        for key in w:
            if ':' in key:
                cond, key = key.split(':')
                if eval(cond):
                    break
            else:
                break
        if key == 'A':
            acc1 += x + m + a + s
print("Part 1:", acc1)

nodes = [('in', [])]
cs = set()
while nodes:
    key, conds = nodes.pop()
    new_conds = []
    for k in f[key]:
        if ':' in k:
            cond, k = k.split(':')
            if k == 'A':
                cs.add(','.join(conds + new_conds + [cond]))
            elif k != 'R':
                nodes.append((k, conds + new_conds + [cond]))
            new_conds.append([cond.replace(k, v) for k, v in {'>=':'<', '<=':'>', '>':'<=', '<':'>='}.items() if k in cond][0])
        else:
            if k == 'A':
                cs.add(','.join(conds + new_conds))
            elif k != 'R':
                nodes.append((k, conds + new_conds))
import math
acc2 = 0
for i in cs:
    d = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    for k in i.split(','):
        for c, y in {'>=': (0, max, 0), '>': (0, max, 1), '<=': (1, min, 0), '<': (1, min, -1)}.items():
            if c in k:
                l, v = k.split(c)
                d[l][y[0]] = y[1](d[l][y[0]], int(v) + y[2])
                break
    acc2 += math.prod([max(0, high - low + 1) for low, high in d.values()])
print("Part 2:", acc2)



