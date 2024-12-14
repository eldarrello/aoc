ps = [tuple(map(int, i.replace('p=', '').replace(' v=', ',').split(','))) for i in open('input.txt').read().splitlines()]
w = 101
h = 103
dds = []
for i in range(1, 10000):
    ps = [((x + dx + w) % w, (y + dy + h) % h, dx, dy) for (x, y, dx, dy) in ps]
    if i == 100:
        qs = [2 * (2 * y // h) + 2 * x // w for (x, y, dx, dy) in ps if x != w // 2 and y != h // 2]
        print("Part 1:", qs.count(0) * qs.count(1) * qs.count(2) * qs.count(3))
    dds.append(sum([(ps[k][0] - ps[k + 1][0]) ** 2 + (ps[k][1] - ps[k + 1][1]) ** 2 for k, r in enumerate(ps[:-1])]))
print("Part 2:", dds.index(min(dds)) + 1)