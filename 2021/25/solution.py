def step(m, d):
    mm = {}
    for yx, v in m.items():
        y, x = yx
        if yx not in mm:
            mm[yx] = m[yx]
        if v == d:
            nyx = {'>': (y, x + 1 if x < len(s[0]) - 1 else 0), 'v': (y + 1 if y < len(s) - 1 else 0, x)}[d]
            if m[nyx] == '.':
                mm[nyx] = d
                mm[yx] = '.'
            else:
                mm[yx] = d
    return mm
s = open('input.txt').read().splitlines()
m = {(y, x): s[y][x] for y in range(len(s)) for x in range(len(s[y]))}
c = 0
while True:
    m1 = step(m, '>')
    m = step(m1, 'v')
    c += 1
    if m1 == m:
        break
print("Part 1:", c)