s = open('input.txt').read().splitlines()

def add(g, x, y):
    if (x, y) in g:
        g[(x, y)] += 1
    else:
        g[(x, y)] = 1

def build(part_2):
    g = {}
    for i in s:
        ps = i.split(' -> ')
        p1s = ps[0].split(',')
        p2s = ps[1].split(',')
        p1x = int(p1s[0])
        p1y = int(p1s[1])
        p2x = int(p2s[0])
        p2y = int(p2s[1])
        if p1x == p2x:
            for y in range(min(p1y, p2y), max(p1y, p2y) + 1):
                add(g, p1x, y)
        if p1y == p2y:
            for x in range(min(p1x, p2x), max(p1x, p2x) + 1):
                add(g, x, p1y)
        if part_2:
            dy = p2y - p1y
            dx = p2x - p1x
            if dx == dy or -dx == dy:
                if p1y < p2y:
                    sx = p1x
                    if p1x < p2x:
                        dx = 1
                    else:
                        dx = -1
                else:
                    sx = p2x
                    if p2x < p1x:
                        dx = 1
                    else:
                        dx = -1
                for y in range(min(p1y, p2y), max(p1y, p2y) + 1):
                    add(g, sx, y)
                    sx += dx
    return sum([1 for i in g.values() if i > 1])

print("Part 1:", build(False))
print("Part 2:", build(True))

