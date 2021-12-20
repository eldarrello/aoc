def eval(n):
    m = {(y, x): s[y][x] for y in range(100) for x in range(100)}
    for i in range(1, n + 1):
        m = {(y, x): e[0][int(''.join(map(str, [int(m[py] == '#') if py in m else (i + 1) % 2 for py in [(y + dy, x + dx) for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]]])), 2)] for y in range(-2 * i, 100 + 2 * i) for x in range(-2 * i, 100 + 2 * i)}
    return sum([1 for v in m.values() if v == '#'])
e, s = map(lambda x: x.split(), open('input.txt').read().split('\n\n'))
print("Part 1:", eval(2))
print("Part 2:", eval(50))