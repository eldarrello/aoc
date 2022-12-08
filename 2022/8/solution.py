def eval(y, x):
    left = [xx for xx in range(x - 1, -1, -1) if s[y][xx] >= s[y][x]]
    cc = x - (left + [0])[0]
    right = [xx for xx in range(x + 1, w, 1) if s[y][xx] >= s[y][x]]
    cc *= (right + [w - 1])[0] - x
    up = [yy for yy in range(y - 1, -1, -1) if s[yy][x] >= s[y][x]]
    cc *= y - (up + [0])[0]
    down = [yy for yy in range(y + 1, h, 1) if s[yy][x] >= s[y][x]]
    cc *= (down + [h - 1])[0] - y
    return cc, len(left) * len(right) * len(up) * len(down) == 0

s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
ff = [eval(y, x) for y in range(1, h - 1) for x in range(1, w - 1)]
print("Part 1:", sum([i[1] for i in ff]) + 2 * w + 2 * h - 4)
print("Part 2:", max([i[0] for i in ff]))