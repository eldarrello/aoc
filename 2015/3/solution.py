s = open('input.txt').read()

def do(mod):
    map = {}
    map[(0, 0)] = 1
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for k in range(len(s)):
        i = s[k]
        dx = 0
        dy = 0
        if i == '>':
            dx = 1
        elif i == '<':
            dx = -1
        elif i == '^':
            dy = -1
        elif i == 'v':
            dy = 1
        if k % mod == 0:
            x1 += dx
            y1 += dy
            map[(x1, y1)] = 1
        else:
            x2 += dx
            y2 += dy
            map[(x2, y2)] = 1
    return len(map)

print('Part 1:', do(1))
print('Part 2:', do(2))