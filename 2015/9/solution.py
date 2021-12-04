s = open('input.txt').read().splitlines()
d = {}
c = set()
for i in s:
    a = i.split(' ')
    d[(a[0], a[2])] = int(a[4])
    c.add(a[0])
    c.add(a[2])

import itertools

cs = itertools.permutations(c)
min_total = 1000000
max_total = 0
for i in cs:
    total = 0
    for k in range(len(i) - 1):
        if (i[k], i[k + 1]) in d:
            total += d[(i[k], i[k + 1])]
        elif (i[k + 1], i[k]) in d:
            total += d[(i[k + 1], i[k])]
        else:
            total = -1
            break
    if total > 0:
        if total < min_total:
            min_total = total
        elif total > max_total:
            max_total = total
print('Part 1:', min_total)
print('Part 2:', max_total)
