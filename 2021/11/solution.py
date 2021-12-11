s = open('input.txt').read().splitlines()
map = {(y, x):int(s[y][x]) for y in range(len(s)) for x in range(len(s[y]))}
flashes = 0
for step in range(1, 1000):
    map = {yx: map[yx] + 1 for yx in map.keys()}
    f = set()
    while(True):
        g = len(f)
        for yx in map.keys():
            if map[yx] > 9 and yx not in f:
                f.add(yx)
                for move in [move for move in [(yx[0] + m[0], yx[1] + m[1]) for m in[(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]] if move in map]:
                    map[move] += 1
        if len(f) == g:
            break
    flashes += len(f)

    for i in f:
        map[i] = 0
    if step == 100:
        print("Part 1:", flashes)
    if len(f) == len(map):
        print("Part 2:", step)
        break



