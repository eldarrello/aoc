def eval(m, ep = None):
    p = [(x, y) for y in range(len(s)) for x in range(len(s[0])) if m[(x, y)] == '^'][0]
    d = 0
    visited = set()
    while True:
        if ep:
            if (p, d) in visited:
                return 0
            visited.add((p, d))
        else:
            visited.add(p)
        np = [(p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] - 1, p[1])][d]
        if np not in m:
            return len(visited)
        if m[np] == '#' or np == ep:
            d = (d + 1) % 4
            continue
        p = np
s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
print("Part 1:", eval(m))
print("Part 2:", sum([1 for y in range(len(s)) for x in range(len(s[0])) if m[(x, y)] == '.' and eval(m, (x, y)) == 0]))

