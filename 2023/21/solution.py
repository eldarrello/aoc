s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s))}
visited = {}
nodes = [(1, (len(s) // 2, len(s) // 2))]
n = len(s)
while nodes:
    d, (x, y) = nodes.pop(0)
    for xy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if m[(xy[0] % len(s), xy[1] % len(s))] != '#' and xy not in visited:
            visited[xy] = d
            if d < n * 3:
                nodes.append((d + 1, xy))
k = [0] + [sum([1 for v in visited.values() if v <= i and v & 1 == i & 1]) for i in range(1, n * 3)]
print("Part 1:", k[64])
periods, rem = divmod(26501365, n)
print("Part 2:", k[rem] + periods * (k[rem + n] - k[rem] + abs(2 * k[-1 - n] - k[-1 - 2 * n] - k[-1]) * (periods - 1) // 2))
