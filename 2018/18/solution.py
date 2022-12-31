s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
m = {(y, x): s[y][x] for y in range(h) for x in range(w)}
def round():
    n = {}
    for y in range(h):
        for x in range(w):
            c = []
            for dx, dy in [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]:
                if (x + dx, y + dy) in m:
                    c.append(m[(x + dx, y + dy)])
            if m[(x, y)] == '.' and c.count('|') >= 3:
                n[(x, y)] = '|'
            elif m[(x, y)] == '|':
                if c.count('#') >= 3:
                    n[(x, y)] = '#'
                else:
                    n[(x, y)] = '|'
            elif m[(x, y)] == '#':
                n[(x, y)] = '#' if '#' in c and '|' in c else '.'
            else:
                n[(x, y)] = '.'
    return n, list(n.values()).count('|') * list(n.values()).count('#')
for i in range(10):
    m, r = round()
print("Part 1:", r)
for i in range(1000 - 10):
    m, r1 = round()
for i in range(2000):
    m, r = round()
    if r1 == r:
        d = i + 1
        break
for i in range((1000000000 - 1000 - d) % d):
    m, r = round()
print("Part 2:", r)