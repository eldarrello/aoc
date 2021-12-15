def eval(n):
    i = open('input.txt').read().splitlines()
    w = len(i[0])
    map = {(y, x): (int(i[y % w][x % w]) + y // w + x // w - 1) % 9 + 1 for y in range(n * w) for x in range(n * w)}
    s = {(y, x): (y + x) * 9 for y in range(n * w) for x in range(n * w)}
    for k in range(1000):
        changed = False
        for y in range(0, n * w):
            for x in range(0, n * w):
                yx = (y, x)
                t = [s[move] + map[yx] for move in
                 [(yx[0] + m[0], yx[1] + m[1]) for m in [(0, 1), (1, 0), (-1, 0), (0, -1)]] if move in map and s[move] + map[yx] < s[yx]]
                if t:
                    s[yx] = min(t)
                    changed = True
        if changed == False:
            return s[(n * w - 1, n * w - 1)]
print("Part 1:", eval(1))
print("Part 2:", eval(5))   #todo: too slow