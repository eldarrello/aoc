s = open('input.txt').read().splitlines()
s = [int(x) for x in s]
import random
combs = set()
mins = set()
min_comb = 10000
for i in range(2000000):
    sum = 0
    items = []
    while sum < 150:
        k = random.randrange(0, len(s))
        if k in items:
            continue
        items.append(k)
        sum += s[k]
    if sum == 150:
        items.sort()
        if len(items) < min_comb:
            min_comb = len(items)
            mins = set()
            mins.add(tuple(items))
        elif len(items) == min_comb:
            mins.add(tuple(items))
        combs.add(tuple(items))
print('Part 1:', len(combs))
print('Part 2:', len(mins))


