def eval(n):
    s = open('input.txt').read().splitlines()
    map = {(y, x): (int(s[y % 100][x % 100]) + y // 100 + x // 100 - 1) % 9 + 1 for y in range(n) for x in range(n)}
    s = {yx: (yx[0] + yx[1]) * 9 for yx in map.keys()}
    for _ in range(10):     #10 - alternative is to break out of the loop if no changes
        for yx in map.keys():
            t = [s[move] + map[yx] for move in [(yx[0] + m[0], yx[1] + m[1]) for m in [(0, 1), (1, 0), (-1, 0), (0, -1)]] if move in map and s[move] + map[yx] < s[yx]]
            if t:
                s[yx] = min(t)
    return s[(n - 1, n - 1)]
print("Part 1:", eval(100))
print("Part 2:", eval(500))