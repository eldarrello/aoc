def step(m, d):
    mm = m.copy()
    for (y, x), v in m.items():
        if v == d:
            nyx = {'>': (y, x + 1 if x < len(s[0]) - 1 else 0), 'v': (y + 1 if y < len(s) - 1 else 0, x)}[d]
            if m[nyx] == '.':
                mm[nyx], mm[(y, x)] = d, '.'
    return mm
s = open('input.txt').read().splitlines()
m = {(y, x): s[y][x] for y in range(len(s)) for x in range(len(s[y]))}
ms = [m:=step(step(m,'>'), 'v') for i in range(500)]
print("Part 1:", sum([ms[i] != ms[i + 1] for i in range(0, len(ms) - 1)]) + 2)