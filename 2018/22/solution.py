s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def run():
    map = {}
    for y in range(h):
        for x in range(w):
            if s[y][x] == '#':
                map[(y, x)] = '#'
    y = h // 2
    x = w // 2
    d = 0
    c = 0
    for i in range(10000000):
        if (y, x) in map:
            if map[(y, x)] =='W':
                map[y, x] = '#'
                c += 1
            elif map[(y, x)] =='#':
                map[y, x] = 'F'
                d = (d + 1) % 4
            elif map[(y, x)] =='F':
                del map[y,x]
                d = (d + 2) % 4
        else:
            map[(y, x)] = 'W'
            d = (d - 1) % 4
        y += ds[d][0]
        x += ds[d][1]
    return c
print("Part 1:", run())
print("Part 2:", 2)