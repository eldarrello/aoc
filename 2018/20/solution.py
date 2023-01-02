s = open('input.txt').read()[1:-1]
m = {}
def get_paths(i, ox, oy):
    paths = []
    x, y = ox, oy
    while i < len(s):
        d = s[i]
        if d == '(':
            ps, i = get_paths(i + 1, x, y)
            paths += ps
        elif d == ')':
            paths.append((x, y))
            return paths, i
        elif d == '|':
            x, y = ox, oy
            paths.append((x, y))
        else:
            dx, dy = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}[d]
            m[(x + dx, y + dy)] = '.'
            x += 2 * dx
            y += 2 * dy
            m[(x, y)] = '.'
        i += 1
get_paths(0, 0, 0)
nodes = [(0, 0)]
visited = set()
depth = 0
cc = 0
while nodes:
    next_nodes = []
    for x, y in nodes:
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and (nx, ny) in m:
                if depth >= 2 * (1000 - 1):
                    cc += 1
                next_nodes.append((nx, ny))
                visited.add((nx, ny))
    nodes = next_nodes
    depth += 1 if next_nodes else 0
print("Part 1:", depth // 2)
print("Part 2:", cc // 2)
