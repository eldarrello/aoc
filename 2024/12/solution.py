s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
areas = []
for (x, y), v in m.items():
    ks = []
    for nn in [(x - 1, y), (x, y - 1)]:
        for k, area in enumerate(areas):
            if nn in area and m[nn] == v and k not in ks:
                areas[k].add((x, y))
                ks.append(k)
                break
    if len(ks) == 0:
        areas.append(set({(x, y)}))
    elif len(ks) == 2:
        areas[ks[0]].update(areas[ks[1]])
        areas.pop(ks[1])
acc = 0
acc2 = 0
for area in areas:
    fence = 0
    sides = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        prev = False
        for x, y in [(x, y) for y in range(-1, len(s) + 1) for x in range(-1, len(s[0]) + 1)]:
            if dx:
                x, y = y, x
            if (x, y) not in area and (x + dx, y + dy) in area:
                fence += 1
                sides += 0 if prev else 1
                prev = True
            else:
                prev = False
    acc += fence * len(area)
    acc2 += sides * len(area)
print("Part 1:", acc)
print("Part 2:", acc2)
