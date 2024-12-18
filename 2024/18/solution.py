def run():
    nodes = [(0, 0, 0)]
    visited = {(0, 0): 0}
    while nodes:
        x, y, d = nodes.pop(0)
        if (x, y) == (70, 70):
            return d
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if (nx, ny) in m and (nx, ny) and ((nx, ny) not in visited or visited[(nx, ny)] > d):
                visited[(nx, ny)] = d
                nodes.append((nx, ny, d + 1))
    return 0
s = open('input.txt').read().splitlines()
m = {(x, y): '.' for y in range(70 + 1) for x in range(70 + 1)}
for i in range(1024):
    del m[tuple(map(int, s[i].split(',')))]
print("Part 1:", run())
for i in range(i + 1, len(s)):
    del m[tuple(map(int, s[i].split(',')))]
    if run() == 0:
        print("Part 2:", s[i])
        break