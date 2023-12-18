def polygon_area(part_2):
    x = 0
    y = 0
    cs = []
    for i in open('input.txt').read().splitlines():
        d, v, c = i.split()
        if part_2:
            v = int(c[2:-2], 16)
            d = int(c[-2:-1])
        else:
            v = int(v)
            d = 'RDLU'.index(d)
        x, y = [(x + v, y), (x, y + v), (x - v, y), (x, y - v)][d]
        cs.append((x, y))
    area = 0
    for i in range(len(cs)):
        j = (i + 1) % len(cs)
        area += cs[i][0] * cs[j][1] - cs[j][0] * cs[i][1]
        area += abs(cs[i][0] - cs[j][0]) + abs(cs[i][1] - cs[j][1])
    return area // 2 + 1    # Based on Pick's theorem
print("Part 1:", polygon_area(False))
print("Part 2:", polygon_area(True))
