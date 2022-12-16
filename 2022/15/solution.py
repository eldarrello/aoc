s = open('input.txt').read().splitlines()
m = {}
bs = {}
for i in s:
    r = i.replace('=', ' ').replace(',', '').replace(':', '').split()
    sx = int(r[3])
    sy = int(r[5])
    bx = int(r[11])
    by = int(r[13])
    d = abs(sx - bx) + abs(sy - by)
    m[(sx, sy)] = d
    if by not in bs:
        bs[by] = set()
    bs[by].add(bx)

def eval(y):
    rs = []
    for key, d in m.items():
        sx, sy = key
        dy = abs(y - sy)
        if dy <= d:
            min_x = sx - (d - dy)
            max_x = sx + d - dy
            rs.append((min_x, max_x))
    rs.sort(key = lambda x: x[0])
    max_x = rs[0][1]
    for i in range(1, len(rs)):
        if rs[i][0] > max_x + 1:
            x = rs[i][0] - 1
            print("Part 2:", x * 4000000 + y)
            return None
        max_x = max(max_x, rs[i][1])
    return rs[-1][1] - rs[0][0] + 1 - (len(bs[y]) if y in bs else 0)
print("Part 1:", eval(2000000))
for i in range(0, 4000000):
    if not eval(i):
        break


