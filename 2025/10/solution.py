from z3.z3 import Int, Optimize, Sum
import itertools
s = open('input.txt').read().splitlines()
acc = 0
acc2 = 0
for q, l in enumerate(s):
    a, b = l.split('] ')
    target = int(a[1:].replace('#', '1').replace('.', '0'), 2)
    bs, c = b.split(' {')
    target2 = list(map(int, c[:-1].split(',')))
    bs = bs.split()
    bis = []
    for i, v in enumerate(bs):
        r = ['0'] * len(a[1:])
        inds = list(map(int, v[1:-1].split(',')))
        for ind in inds:
            r[ind] = '1'
        bs[i] = int(''.join(r), 2)
        bis.append(inds)
    done = False
    for i in range(1, len(bs)):
        for k in itertools.combinations(bs, i):
            state = 0
            for c in k:
                state ^= c
            if state == target:
                acc += i
                done = True
                break
        if done:
            break

    s = Optimize()
    vars = [Int(f'x_{i}') for i in range(len(bis))]
    for var in vars:
        s.add(var >= 0)
    for i, target in enumerate(target2):
        constraint = sum([vars[k] for k in range(len(bis)) if i in bis[k]])
        s.add(constraint == target)
    presses = Sum(*vars)
    s.minimize(presses)
    s.check()
    acc2 += s.model().evaluate(presses).as_long()
print("Part 1:", acc)
print("Part 2:", acc2)
#todo::without z3?
