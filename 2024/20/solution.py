def eval(n):
    area = [(x, y) for y in range(-n, n + 1) for x in range(-n, n + 1) if abs(x) + abs(y) <= n]
    return sum([1 for (x, y), i in t.items() for dx, dy in area if (x + dx, y + dy) in t and t[(x + dx, y + dy)] - i - abs(dx) - abs(dy) >= 100])
s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
x, y = [k for k, v in m.items() if v == 'S'][0]
track = [(x, y)]
while True:
    for x, y in [(nx, ny) for (nx, ny) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if (nx, ny) in m and (nx, ny) not in track and m[(nx, ny)] != '#']:
        track.append((x, y))
        break
    else:
        break
t = {p: i for i, p in enumerate(track)}
print("Part 1:", eval(2))
print("Part 2:", eval(20))


