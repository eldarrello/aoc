s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
def eval(part):
    acc = 0
    for (x, y), v in m.items():
        if v == '0':
            ends = []
            nodes = [(x, y, int(v))]
            while nodes:
                x, y, v = nodes.pop()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (nx, ny) in m and m[(nx, ny)].isdigit() and int(m[(nx, ny)]) == v + 1:
                        if m[(nx, ny)] == '9':
                            ends.append((nx, ny))
                        nodes.append((nx, ny, v + 1))
            acc += len(ends) if part else len(set(ends))
    return acc
print("Part 1:", eval(0))
print("Part 2:", eval(1))

