s = open('input.txt').read().splitlines()
m = {(x - 1, y - 1): s[y][x] for y in range(len(s)) for x in range(len(s[0])) if s[y][x] != '#'}
h = len(s) - 2
w = len(s[0]) - 2
def eval(start, end, minute):
    nodes = [start]
    while nodes:
        next_nodes = set()
        while nodes:
            x, y = nodes.pop(0)
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
                nx, ny = x + dx, y + dy
                p = (nx, ny)
                if p in m:
                    vx = (nx - minute) % w
                    if vx < 0:
                        vx += w
                    vy = (ny - minute) % h
                    if vy < 0:
                        vy += h
                    if (((nx + minute) % w, ny) in m and m[((nx + minute) % w, ny)] == '<')\
                            or ((vx, ny) in m and m[(vx, ny)] == '>')\
                            or ((nx, (ny + minute) % h) in m and m[(nx, (ny + minute) % h)] == '^')\
                            or ((nx, vy) in m and m[(nx, vy)] == 'v'):
                        continue
                    next_nodes.add(p)
        nodes = list(next_nodes)
        if end in nodes:
            return minute
        minute += 1
start = (0, -1)
end = (99, 35)
minute = eval(start, end, 1)
print("Part 1:", minute)
print("Part 2:", eval(start, end, eval(end, start, minute)))
