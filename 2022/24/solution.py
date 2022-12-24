s = open('input.txt').read().splitlines()
m = {(x - 1, y - 1): s[y][x] for y in range(len(s)) for x in range(len(s[0])) if s[y][x] != '#'}
h = len(s) - 2
w = len(s[0]) - 2
def eval(start, end, minute):
    nodes = [start]
    for minute in range(minute, minute + 1000):
        next_nodes = set()
        for x, y in nodes:
            for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1), (x, y)]:
                if (nx, ny) == end:
                    return minute
                if (nx, ny) in m:
                    vx = (nx - minute) % w
                    if vx < 0:
                        vx += w
                    vy = (ny - minute) % h
                    if vy < 0:
                        vy += h
                    if (((nx + minute) % w, ny) not in m or m[((nx + minute) % w, ny)] != '<')\
                            and ((vx, ny) not in m or m[(vx, ny)] != '>')\
                            and ((nx, (ny + minute) % h) not in m or m[(nx, (ny + minute) % h)] != '^')\
                            and ((nx, vy) not in m or m[(nx, vy)] != 'v'):
                        next_nodes.add((nx, ny))
        nodes = list(next_nodes)
start = (0, -1)
end = (99, 35)
minute = eval(start, end, 1)
print("Part 1:", minute)
print("Part 2:", eval(start, end, eval(end, start, minute)))
