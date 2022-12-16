def land_shape(si):
    global pi, max_y
    sx = 2
    sy = max_y + 4
    shape = [[(0, 0), (1, 0), (2, 0), (3, 0)],
          [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
          [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
          [(0, 0), (0, 1), (0, 2), (0, 3)],
          [(0, 0), (1, 0), (0, 1), (1, 1)]][si % 5]
    while True:
        dx = {'>': 1, '<': -1}[p[pi % len(p)]]
        pi += 1
        for px, py in shape:
            nx = sx + px + dx
            if (nx, sy + py) in m or nx < 0 or nx > 6:
                break
        else:
            sx += dx
        for px, py in shape:
            ny = sy + py - 1
            if (sx + px, ny) in m or ny < 1:
                for x, y in shape:
                    max_y = max(max_y, sy + y)
                    m[(sx + x, sy + y)] = '#'
                return max_y, pi % len(p)
        else:
            sy -= 1
p = open('input.txt').read()
m = {}
pi = 0
max_y = 0
ys = [land_shape(si) for si in range(0, 5000)]
print("Part 1:", ys[2022 - 1][0])
for i in range(len(ys) - 2, 0, -1):
    if ys[i][1] == ys[-1][1]:
        period = len(ys) - i - 1    # This period search is rather simple and may not work for all inputs!
        dy = ys[-1][0] - ys[i][0]
        break
q, r = divmod(1000000000000, period)
print("Part 2:", dy * q + ys[r - 1][0])