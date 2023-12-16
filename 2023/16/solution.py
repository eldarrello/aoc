def run(nodes):
    visited = set()
    while nodes:
        x, y, dx, dy = nodes.pop(0)
        visited.add((x, y, dx, dy))
        d = m[(x, y)]
        next = [(dx, dy)]
        if d == '/':
            next = [(-dy, -dx)]
        elif d == '\\':
            next = [(dy, dx)]
        elif d == '|' and dx:
            next = [(dy, dx), (dy, -dx)]
        elif d == '-' and dy:
            next = [(dy, dx), (-dy, dx)]
        for dx, dy in next:
            if (x + dx, y + dy) in m:
                key = (x + dx, y + dy, dx, dy)
                nodes.append(key) if key not in visited else 0
    return len({(x, y) for x, y, _, _ in list(visited)})

s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
m = {(x, y): s[y][x] for y in range(h) for x in range(w)}
print("Part 1:", run([(0, 0, 1, 0)]))
print("Part 2:", max([run([(x, 0, 0, 1)]) for x in range(w)] + [run([(w - 1, y, -1, 0)]) for y in range(h)] + [run([(x, h - 1, 0, -1)]) for x in range(w)] + [run([(0, y, 1, 0)]) for y in range(h)]))

