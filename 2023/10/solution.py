s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
x, y = [(x, y) for x, y in m.keys() if m[(x, y)] == 'S'][0]
dx, dy = 0, 1           #hack for specific input.txt
loop = set([(x, y)])
while True:
    x, y = x + dx, y + dy
    loop.add((x, y))
    v = m[(x, y)]
    if v == 'S':
        m[x, y] = '7'   #hack for specific input.txt
        break
    if v in 'FJ':
        dx, dy = -dy, -dx
    elif v in 'L7':
        dx, dy = dy, dx

def is_inside(x, y):
    acc = 0
    s = 0
    for i in range(x):
        if (i, y) in loop and m[(i, y)] != '-':
            p, s = {'|':(1, 0), 'L':(0, 'L'), 'F':(0, 'F'), '7':(1 if s == 'L' else 0, 0), 'J':(1 if s == 'F' else 0, 0)}[m[(i, y)]]
            acc += p
    return acc % 2 == 1

print("Part 1:", len(loop) // 2)
print("Part 2:", sum([1 for x, y in m.keys() if (x, y) not in loop and is_inside(x, y)]))


