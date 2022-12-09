p = [(0, 0) for i in range(10)]
m = [set(), set()]
for i in open('input.txt').read().splitlines():
    s, n = i.split()
    for k in range(int(n)):
        p[0] = tuple(map(sum, zip(p[0], {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}[s])))
        for j in range(1, len(p)):
            d = (int((p[j][0] - p[j - 1][0]) / 2), int((p[j][1] - p[j - 1][1]) / 2))
            p[j] = p[j] if d == (0, 0) else tuple(map(sum, zip(p[j - 1], d)))
        m[0].add(p[1])
        m[1].add(p[-1])
print("Part 1:", len(m[0]))
print("Part 2:", len(m[1]))
