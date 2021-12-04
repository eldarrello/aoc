input = 289326

def spin(part_2):
    k = 1
    n = 1
    x = 0
    y = 0
    map = {(0, 0):1}
    while True:
        for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            for i in range(n):
                x += d[0]
                y += d[1]
                if part_2:
                    k = 0
                    ps = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
                    for p in ps:
                        if p in map:
                            k += map[p]
                    map[x, y] = k
                    if k > input:
                        print("Part 2:", k)
                        return
                else:
                    k += 1
                    if k == input:
                        print("Part 1:", abs(x) + abs(y))
                        return
            if d[0] == 0:
                n += 1
spin(False)
spin(True)