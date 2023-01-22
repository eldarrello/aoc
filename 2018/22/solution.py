s = open('input.txt').read().splitlines()
depth = int(s[0].split()[1])
tx, ty = map(int, s[1].split()[1].split(','))
def get_erosion_map(w, h):
    el = {}
    for y in range(h + 1):
        for x in range(w + 1):
            if x == tx and y == ty:
                gi = 0
            elif y == 0:
                gi = x * 16807
            elif x == 0:
                gi = y * 48271
            else:
                gi = el[(x - 1, y)] * el[(x, y - 1)]
            el[(x, y)] = (gi + depth) % 20183
    return el
print("Part 1:", sum([v % 3 for v in get_erosion_map(tx, ty).values()]))
m = get_erosion_map(tx + 50, ty + 30)
nodes = [(0, 0, 0, 2)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
m = {k: (v % 3, [3 * (k[0] + k[1]), 3 * (k[0] + k[1]), 3 * (k[0] + k[1])]) for k, v in m.items()}
best_time = (tx + ty) * 3
while nodes:
    x, y, t, gear = nodes.pop(0)
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx == tx and ny == ty:
            end_time = t + 1
            if gear != 2:
                end_time += 7
            if end_time < best_time:
                best_time = end_time
            continue
        if abs(tx - nx) + abs(ty - ny) + t >= best_time:
            continue
        if (nx, ny) in m:
            type, visited = m[(nx, ny)]
            needed_gears = [[1, 2], [1, 0], [2, 0]][type]
            if gear in needed_gears:
                if t + 1 < visited[gear] and t + 1 < min(visited) + 7:
                    nodes.append((nx, ny, t + 1, gear))
                    visited[gear] = t + 1
                    m[(nx, ny)] = (type, visited)
            else:
                for g in needed_gears:
                    if g in [[1, 2], [1, 0], [2, 0]][m[(x, y)][0]]:
                        if t + 8 < visited[g]:
                            nodes.append((nx, ny, t + 8, g))
                            visited[g] = t + 8
                            m[(nx, ny)] = (type, visited)
print("Part 2:", best_time)
