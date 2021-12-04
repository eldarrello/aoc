d = [(0,0),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
def neighbors(p):
    out = []
    for k in part:
        for j in range(-1, 2):
            out += [(p[0] + i[1], p[1] + i[0], p[2] + j, p[3] + k) for i in d if not (i == (0,0) and k == 0 and j == 0)]
    return out
def value(p, n):
    c = sum(1 for i in n if i in m)
    return c == 3 or (c == 2 and p in m)
for i, part in enumerate([[0], [-1, 0, 1]]):
    s = open('input.txt').read().splitlines()
    m = {(x, y, 0, 0) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '#'}
    for t in range(6):
        m1 = set()
        for p in m:
            n = neighbors(p)
            if value(p, n):
                m1.add(p)
            for np in n:
                if np not in m and np not in m1:
                    if value(np, neighbors(np)):
                        m1.add(np)
        m = m1
    print("Part {}:".format(i + 1), len(m))