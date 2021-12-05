s = open('input.txt').read().splitlines()

def calc(part_2):
    g = {}
    for i in s:
        l = [int(k) for k in i.replace(' -> ', ',').split(',')]
        dy = l[3] - l[1]
        dx = l[2] - l[0]
        if dx * dy == 0 or part_2 and (abs(dx) == abs(dy)):
            for k in range(max(abs(dy), abs(dx)) + 1):
                p = (l[0] + (0 if dx == 0 else k if dx > 0 else -k), l[1] + (0 if dy == 0 else k if dy > 0 else -k))
                g[p] = g[p] + 1 if p in g else 1
    return sum([1 for i in g.values() if i > 1])

print("Part 1:", calc(False))
print("Part 2:", calc(True))

