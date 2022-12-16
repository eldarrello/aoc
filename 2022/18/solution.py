d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
m = {tuple(map(int,(i.split(',')))) for i in open('input.txt').read().splitlines()}
s = [(x + dx, y + dy, z + dz) for x, y, z in m for (dx, dy, dz) in d if (x + dx, y + dy, z + dz) not in m]
print("Part 1:", len(s))
acc = 0
outer = set()
for i in s:
    visited = set()
    nodes = [i]
    depth = 0
    while nodes:
        next_nodes = []
        while nodes:
            x, y, z = nodes.pop(0)
            visited.add((x, y, z))
            next_nodes += [(x + dx, y + dy, z + dz) for dx, dy, dz in d]
        nodes = [node for node in set(next_nodes) if node not in visited and node not in m]
        depth += 1
        if (x, y, z) in outer or depth > 40:
            acc += 1
            outer.update(visited)
            break
print("Part 2:", acc)

