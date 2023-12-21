s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
visited = {}
nodes = [(1, [(x, y) for x, y in m.keys() if m[(x, y)] == 'S'][0])]
while nodes:
    d, (x, y) = nodes.pop(0)
    for xy in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if m[(xy[0] % len(s[0]), xy[1] % len(s))] != '#' and xy not in visited:
            visited[xy] = d
            if d < 500:
                nodes.append((d + 1, xy))
k = [0] + [sum([1 for v in visited.values() if v <= i and v & 1 == i & 1]) for i in range(1, 500)]  # This can be made faster with some more code. Runs 10s
print("Part 1:", k[64])
for n in range (1, 150):
    dk1 = k[-1] - k[-1 - n]
    dk2 = k[-1 - n] - k[-1 - 2 * n]
    dk3 = k[-1 - 2 * n] - k[-1 - 3 * n]
    if dk2 - dk1 == dk3 - dk2:
        periods, rem = divmod(26501365, n)
        print("Part 2:", k[rem] + periods * (k[rem + n] - k[rem] + abs(dk2 - dk1) * (periods - 1) // 2))
