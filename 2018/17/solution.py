s = open('input.txt').read().splitlines()
m = {}
for i in s:
    a, b, _, d, e = i.replace(',', '').replace('=', ' ').replace('..', ' ').split()
    b = int(b)
    d = int(d)
    e = int(e)
    if a == 'y':
        y = b
        for x in range(d, e + 1):
           m[(x, y)] = '#'
    else:
        x = b
        for y in range(d, e + 1):
           m[(x, y)] = '#'
min_y = 10000
max_y = 0
for k, v in m.items():
    min_y = min(k[1], min_y)
    max_y = max(k[1], max_y)

def debug():
    for y in range(0, max_y):
        row = []
        for x in range(0, 2000):
            if (x, y) in m:
                if (x, y) in stuck:
                    row.append('~')
                else:
                    row.append(m[(x, y)])
            else:
                row.append('.')
        print(''.join(row))
def flood(x, y):
    right_side = False
    for rx in range(x, 2000):
        if (rx, y) not in m or m[(rx, y)] != '#':
            m[(rx, y)] = '|'
            if (rx, y + 1) not in m:
                if m[(rx - 1, y + 1)] == '|':
                    m[(rx, y)] = '.'
                    break
                if land_water(rx, y) == y:
                    continue
                break
        else:
            right_side = True
            break
    left_side = False
    for lx in range(x, 0, -1):
        if (lx, y) not in m or m[(lx, y)] != '#':
            m[(lx, y)] = '|'
            if (lx, y + 1) not in m:
                if m[(lx + 1, y + 1)] == '|':
                    m[(lx, y)] = '.'
                    break
                if land_water(lx, y) == y:
                    continue
                break
        else:
            left_side = True
            break
    if left_side and right_side:
        for x in range(lx + 1, rx):
            stuck.add((x, y))
        return True
    return False
def land_water(x, y):
    while y < max_y:
        ny = y + 1
        if (x, ny) in m and m[(x, ny)] == '#':
            while flood(x, y):
                y -= 1
            return y
        else:
            y = ny
            if y >= min_y:
                m[(x, y)] = '|'
    return -1
stuck = set()
land_water(500, 0)
#debug()
print("Part 1:", len([1 for v in m.values() if v == '|']))
print("Part 2:", len(stuck))
