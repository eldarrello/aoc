s = open('input.txt').read().splitlines()

def rotate(p):
    return [''.join(i) for i in zip(*p[::-1])]

def flip_h(p):
    return [i[::-1] for i in p]

def get(p):
    return sum([[p:=rotate(p), flip_h(p)] for i in range(4)], [])

map = {}
for i in s:
    a, b = i.split(' => ')
    for i in get(a.split('/')):
        map[str(i)] = b.split('/')

def run(n):
    g = ['.#.', '..#', '###']
    for i in range(n):
        f = 2 if len(g) % 2 == 0 else 3
        n = len(g) // f
        gs = []
        for y in range(0, len(g), f):
            for j in range(n):
                gs.append([g[y + i][j*f:(j+1)*f] for i in range(f)])
        for t, p in enumerate(gs):
            gs[t] = map[str(p)]
        w = f + 1
        g = ['' for i in range(n * w)]
        for i, p in enumerate(gs):
            for y, t in enumerate(p):
                g[w * (i // n) + y] += t
    return sum(i.count('#') for i in g)

print("Part 1:", run(5))
print("Part 2:", run(18))