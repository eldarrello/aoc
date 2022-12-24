map, path = open('input.txt').read().split('\n\n')
map = map.splitlines()
m = {(x, y): map[y][x] for y in range(len(map)) for x in range(len(map[y])) if map[y][x] != ' '}
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
p = []
num = ''
for i in path:
    if i in 'LR':
        p.append(int(num))
        p.append(i)
        num = ''
    else:
        num += i
if num != '':
    p.append(int(num))
def eval(part):
    d = 0
    x = 50
    y = 0
    for c in p:
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4
        else:
            for i in range(c):
                dx, dy = dirs[d]
                np = (x + dx, y + dy)
                nd = d
                if np not in m:
                    if part == 1:
                        odx, ody = dirs[(d + 2) % 4]
                        for i in range(1000):
                            if (x + i * odx, y + i * ody) not in m:
                                np = (x + (i - 1) * odx, y + (i - 1) * ody)
                                break
                    else:
                        lx = x % 50
                        ly = y % 50
                        np, nd = {(1, 2): ((0, 149 - ly), 0), (1, 3): ((0, 150 + lx), 0),
                              (2, 3): ((lx, 199), 3), (2, 0): ((99, 149 - ly), 2), (2, 1): ((99, 50 + lx), 2),
                              (4, 2): ((0 + ly, 100), 1), (4, 0): ((100 + ly, 49), 3),
                              (6, 2): ((50, 49 - ly), 0), (6, 3): ((50, 50 + lx), 0),
                              (7, 0): ((149, 49 - ly), 2), (7, 1): ((49, 150 + lx), 2),
                              (9, 2): ((50 + ly, 0), 1), (9, 1): ((100 + lx, 0), 1), (9, 0): ((50 + ly, 149), 3)
                              }[(y // 50 * 3 + x // 50, d)]
                if m[np] != '.':
                    break
                x, y = np
                d = nd
    return 1000 * (y + 1) + 4 * (x + 1) + d
print("Part 1:", eval(1))
print("Part 2:", eval(2))
