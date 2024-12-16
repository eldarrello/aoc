s, b = open('input.txt').read().split('\n\n')
s = s.splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
b = b.replace('\n', '')
x, y = [(x, y) for x, y in m.keys() if m[(x, y)] == '@'][0]
m[(x, y)] = '.'
for i in b:
    dx, dy = [(-1, 0), (1, 0), (0, -1), (0, 1)]['<>^v'.index(i)]
    for k in range(1, 50):
        p = (x + k * dx, y + k * dy)
        if m[p] == '.':
            for j in range(k, 0, -1):
                m[(x + j * dx, y + j * dy)] = m[(x + j * dx - dx, y + j * dy - dy)]
            x += dx
            y += dy
            break
        if m[p] == '#':
            break
acc = 0
for x, y in [(x, y) for x, y in m.keys() if m[(x, y)] == 'O']:
    acc += 100 * y + x
print("Part 1:", acc)

for y, line in enumerate(s):
    for x, v in enumerate(line.replace('O', '[]').replace('.', '..').replace('#', '##').replace('@', '@.')):
        m[(x, y)] = v
x, y = [(x, y) for x, y in m.keys() if m[(x, y)] == '@'][0]
m[(x, y)] = '.'
tt = 0
for i in b:
    dx, dy = [(-1, 0), (1, 0), (0, -1), (0, 1)]['<>^v'.index(i)]
    if dx:
        for k in range(1, 100):
            p = (x + k * dx, y + k * dy)
            if m[p] == '.':
                for j in range(k, 0, -1):
                    m[(x + j * dx, y + j * dy)] = m[(x + j * dx - dx, y + j * dy - dy)]
                x += dx
                y += dy
                break
            if m[p] == '#':
                break
    else:
        moves = []
        nodes = [(x, y)]
        while nodes:
            px, py = nodes.pop(0)
            nx = px + dx
            ny = py + dy
            if (px, py, nx, ny) not in moves:
                moves.append((px, py, nx, ny))
                if m[(nx, ny)] == '#':
                    moves.clear()
                    break
                if m[(nx, ny)] == '[':
                    nodes.append((nx, ny))
                    nodes.append((nx + 1, ny))
                if m[(nx, ny)] == ']':
                    nodes.append((nx, ny))
                    nodes.append((nx - 1, ny))
        if moves:
            while moves:
                sx, sy, nx, ny = moves.pop()
                m[(nx, ny)] = m[(sx, sy)]
                m[(sx, sy)] = '.'
            x += dx
            y += dy
acc = 0
for x, y in [(x, y) for x, y in m.keys() if m[(x, y)] == '[']:
    acc += 100 * y + x
print("Part 2:", acc)

