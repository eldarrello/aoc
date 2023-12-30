import itertools
bs = [list(map(int,i.replace(' @', ',').split(', '))) for i in open('input.txt').read().splitlines()]
acc = 0
for (x, y, _, dx, dy, _), (x2, y2, _, dx2, dy2, _) in itertools.combinations(bs, 2):
    d = dy * dx2 - dx * dy2
    if d != 0:
        t2 = (dx * (y2 - y) - dy * (x2 - x)) / d
        t1 = ((y2 - y) + t2 * dy2) / dy
        min_v = 200000000000000
        max_v = 400000000000000
        if min_v <= x + t1 * dx <= max_v and min_v <= y + t1 * dy <= max_v and t1 >= 0 and t2 >= 0:
            acc += 1
print("Part 1:", acc)
from z3 import *
rs = RealVector('r', 6)
ts = RealVector('t', 3)
s = Solver()
s.add(*[rs[d] + rs[d+3] * t == b[d] + b[d+3] * t for t, b in zip(ts, bs) for d in range(3)])
s.check()
print("Part 2:", s.model().eval(sum(rs[:3])))
#Todo::own implementation without Z3
