ds = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]  # y, x
def get(s, w, p, part):
    c = 0
    ty, tx = divmod(p, w)
    for d in ds:
        y = ty
        x = tx
        while True:
            y += d[0]
            x += d[1]
            if y >= 0 and (y * w + x) < len(s) and x >= 0 and x < w:
                if s[y * w + x] == '#':
                    c += 1
                if s[y * w + x] == '.' and part != 1:
                    continue
            break
    return c

def run(part):
    k = open('input.txt').read().splitlines()
    w = len(k[0])
    s = []
    for i in k:
        s += list(i)
    n = len(s)
    while True:
        t = ['#' if s[p] == 'L' and get(s, w, p, part) == 0 else s[p] for p in range(n)]
        s = ['L' if t[p] == '#' and get(t, w, p, part) >= (4 if part == 1 else 5) else t[p] for p in range(n)]
        if t == s:
            break
    return sum(i.count('#') for i in s)
print("Part 1:", run(1))
print("Part 2:", run(2))