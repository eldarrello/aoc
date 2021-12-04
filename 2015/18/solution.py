s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)

def eval(s, x, y):
    d = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    c = 0
    for i in d:
        kx = x + i[0]
        ky = y + i[1]
        if ky < 0 or ky >= h or kx < 0 or kx >= w:
            continue
        if s[ky][kx] == '#':
            c += 1
    if s[y][x] == '#':
        return c >= 2 and c <= 3
    else:
        return c == 3

def iter(s):
    t = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append('#' if eval(s, x, y) else '.')
        t.append(row)
    return t

def count(s, part_2):
    for i in range(100):
        s = iter(s)
        if part_2:
            set_corners(s)
    cnt = 0
    for i in s:
        cnt += i.count('#')
    return cnt

def set_corners(s):
    s[0][0] = '#'
    s[0][w - 1] = '#'
    s[h - 1][0] = '#'
    s[h - 1][w - 1] = '#'

print('Part 1:', count(s, False))
s = open('input.txt').read().splitlines()
for i in range(len(s)):
    s[i] = list(s[i])
set_corners(s)
print('Part 2:', count(s, True))


