def eval(p, q):
    nodes = [(0, 0, 0, 1, 0), (0, 0, 0, 0, 1)]
    visited = set()
    while nodes:
        score, x, y, dx, dy = heapq.heappop(nodes)
        if x == w - 1 and y == h - 1:
            return score
        if (x, y, dx, dy) in visited:
            continue
        visited.add((x, y, dx, dy))
        for ndx, ndy in [(dy, dx), (-dy, -dx)]:
            nscore = score
            for i in range(1, q + 1):
                nx = x + i * ndx
                ny = y + i * ndy
                if (nx, ny) in m:
                    nscore += m[(nx, ny)]
                    if i >= p:
                        heapq.heappush(nodes, (nscore, nx, ny, ndx, ndy))
import heapq
s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
m = {(x, y): int(s[y][x]) for y in range(h) for x in range(w)}
print("Part 1:", eval(1, 3))
print("Part 2:", eval(4, 10))
