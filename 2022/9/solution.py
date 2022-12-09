def eval(k):
    s = open('input.txt').read().splitlines()
    p = [(0, 0) for i in range(k)]
    m = set()
    for i in s:
        s, n = i.split()
        for k in range(int(n)):
            p[0] = tuple(map(sum, zip(p[0], {'U':(-1, 0), 'D':(1, 0), 'L':(0, -1), 'R':(0, 1)}[s])))
            for j in range(1, len(p)):
                dx = int((p[j][1] - p[j - 1][1]) / 2)
                dy = int((p[j][0] - p[j - 1][0]) / 2)
                p[j] = p[j] if dx | dy == 0 else (p[j - 1][0] + dy, p[j - 1][1] + dx)
            m.add(p[-1])
    return len(m)
print("Part 1:", eval(2))
print("Part 2:", eval(10))
