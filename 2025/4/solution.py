def reduce():
    q = []
    for y, x in m:
        c = 0
        for dy, dx in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
            if (y + dy, x + dx) in m:
                c += 1
        if c < 4:
            q.append((y, x))
    for y, x in q:
        m.remove((y, x))
    return len(q)
s = open('input.txt').read().splitlines()
m = {(y, x) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '@'}
acc = len(m)
print("Part 1:", reduce())
while(reduce()):
    pass
print("Part 2:", acc - len(m))
