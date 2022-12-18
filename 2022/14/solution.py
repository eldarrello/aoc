s = open('input.txt').read().splitlines()
m = set()
max_y = 0
for line in s:
    ps = [(int(p.split(',')[0]), int(p.split(',')[1])) for p in line.split(' -> ')]
    for i in range(1, len(ps)):
        dx = ps[i][0] - ps[i - 1][0]
        dy = ps[i][1] - ps[i - 1][1]
        m.add((ps[i - 1][0], ps[i - 1][1]))
        max_y = max(max_y, ps[i - 1][1])
        max_y = max(max_y, ps[i][1])
        for x in range(abs(dx)):
            m.add((ps[i - 1][0] + int(x * dx / abs(dx)), ps[i - 1][1]))
        for y in range(abs(dy)):
            m.add((ps[i - 1][0], ps[i - 1][1] + int(y * dy / abs(dy))))
        m.add((ps[i][0], ps[i][1]))
def eval(n):
    part_1 = 0
    while True:
        sx = 500
        sy = 0
        while (sx, sy) not in m:
            sy += 1
            if (sx, sy) in m:
                if (sx - 1, sy) not in m:
                    sx -= 1
                elif (sx + 1, sy) not in m:
                    sx += 1
            if sy > max_y + 1:
                if part_1 == 0:
                    part_1 = len(m) - n
                break
        m.add((sx, sy - 1))
        if sy == 1:
            return part_1, len(m) - n
print("Part 1: {}\nPart 2: {}".format(*eval(len(m))))
