s = open('input.txt').read().splitlines()
ps = []
for i in s:
    a, b = i.split(', ')
    ps.append((int(a), int(b)))
m = {}
for y in range(360):        #360 - max cordinate from input file
    for x in range(360):
        min_d = 1000
        for i in range(len(ps)):
            xy = ps[i]
            d = abs(xy[0] - x) + abs(xy[1] - y)
            if d < min_d:
                min_d = d
                min_i = i
            elif d == min_d:
                min_d = 1000
                min_i = 1000
        m[(x, y)] =  min_i
exclude = set()
for k, v in m.items():
    if k[0] == 0 or k[0] == 360 - 1 or k[1] == 0 or k[1] == 360 - 1:
        exclude.add(v)
acc = 0
for i in range(len(ps)):
    c = list(m.values()).count(i)
    if c > acc and i not in exclude:
        acc = c
print("Part 1:", acc)
acc = 0
for k in m.keys():
    d = 0
    for xy in ps:
        d += abs(xy[0] - k[0]) + abs(xy[1] - k[1])
    if d < 10000:
        acc += 1
print("Part 2:", acc)