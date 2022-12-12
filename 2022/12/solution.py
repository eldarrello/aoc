s = open('input.txt').read().splitlines()
z = {(y, x): ord(s[y][x]) for y in range(len(s)) for x in range(len(s[0]))}
start = [k for k, v in z.items() if v == ord('S')][0]
end = [k for k, v in z.items() if v == ord('E')][0]
z[start] = ord('a')
z[end] = ord('z')
def eval(start):
    nodes = [start]
    visited = set()
    depth = 0
    while nodes and str(end) not in visited:
        next_nodes = []
        for y, x in nodes:
            moves = [m for m in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)] if m in z and z[m] - z[(y, x)] <= 1 and str(m) not in visited]
            visited.update([str(m) for m in moves])
            next_nodes += moves
        nodes = next_nodes
        depth += 1
    return depth if str(end) in visited else len(s) * len(s[0])
print("Part 1:", eval(start))
print("Part 2:", min([eval(m) for m in z if z[m] == ord('a')]))
