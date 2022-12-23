s = open('input.txt').read().splitlines()
m = {(x, y) for y in range(len(s)) for x in range(len(s[0])) if s[y][x] == '#'}
dirs = [(1, -1), (1, 1), (1, 0), (-1, -1), (1, -1), (0, -1), (-1, 1), (1, 1), (0, 1), (-1, -1), (-1, 1), (-1, 0)]
for round in range(1, 10000):
    proposed = {}
    for x, y in m:
        if [1 for dx, dy in dirs if (x + dx, y + dy) in m]:
            for i in range(4):
                for k in range(3):
                    dx, dy = dirs[((round + i) % 4) * 3 + k]
                    p = (x + dx, y + dy)
                    if p in m:
                      break
                else:
                    proposed[p] = (x, y) if p not in proposed else None
                    break
    m.update({k for k, v in proposed.items() if v})
    m = m - {v for v in proposed.values() if v}
    if len(proposed) == 0:
        break
    if round == 10:
        w = max(m, key = lambda p: p[0])[0] - min(m, key = lambda p: p[0])[0] + 1
        h = max(m, key = lambda p: p[1])[1] - min(m, key = lambda p: p[1])[1] + 1
        print("Part 1:", w * h - len(m))
print("Part 2:", round)
