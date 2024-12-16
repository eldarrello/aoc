s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
scores = {}
visited = {}
nodes = [(0, (1, len(s) - 2, 1, []))]
while nodes:
    score, (x, y, d, path) = nodes.pop(0)
    if (x, y) == (len(s[0]) - 2, 1):
        scores[score] = scores[score] | set(path) if score in scores else set(path)
    for nd, (nx, ny) in enumerate([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]):
        nscore = score + 1 + (1000 if nd != d else 0)
        if m[(nx, ny)] != '#' and (nx, ny) not in path and ((nx, ny) not in visited or nscore <= visited[(nx, ny)] + 1000):
            visited[(nx, ny)] = nscore
            nodes.append((nscore, (nx, ny, nd, path + [(x, y)])))
print("Part 1:", min(scores.keys()))
print("Part 2:", len(scores[min(scores.keys())]) + 1)

