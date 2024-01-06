def apply(d, cond, y = [(1, min, 0), (0, max, 0)]):
    dd = copy.deepcopy(d)
    y = y['<>'.index(cond[1])]
    i = 'xmas'.index(cond[0])
    dd[i][y[0]] = y[1](dd[i][y[0]], int(cond[2:]) + y[2])
    return dd

import math, copy
a, b = open('input.txt').read().split('\n\n')
f = {}
for i in a.splitlines():
    key, r = i.split('{')
    f[key] = r[:-1].split(',')
acc1 = 0
acc2 = 0
nodes = [('in', [[0, 4001], [0, 4001], [0, 4001], [0, 4001]])]
while nodes:
    key, d = nodes.pop()
    for k in f[key]:
        cond = 'x>0'
        if ':' in k:
            cond, k = k.split(':')
        if k == 'A':
            dd = apply(d, cond)
            acc2 += math.prod([max(0, high - low - 1) for low, high in apply(d, cond)])
            for i in b.splitlines():
                acc = 0
                for j, c in enumerate(i[1:-1].split(',')):
                    acc += int(c[2:]) if dd[j][0] < int(c[2:]) < dd[j][1] else -4 * 4001
                acc1 += max(0, acc)
        elif k != 'R':
            nodes.append((k, apply(d, cond)))
        d = apply(d, cond, [(0, max, -1), (1, min, 1)])
print("Part 1:", acc1)
print("Part 2:", acc2)



