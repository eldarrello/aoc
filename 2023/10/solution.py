s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
x, y = [(x, y) for x, y in m.keys() if m[(x, y)] == 'S'][0]
gg = [(dx, dy) for (dx, dy), v in {(1, 0): '-7J', (-1, 0): '-FL', (0, 1): '|LJ', (0, -1): '|F7'}.items() if m[(x + dx, y + dy)] in v]
dx, dy = gg[0]
m[(x, y)] = {(-1,0,0,1):'7', (0,-1,0,1):'|', (1,0,0,1):'F', (-1,0,0,-1):'J', (-1,0,1,0):'-', (0,-1,1,0):'L'}[gg[0] + gg[1]]
loop = set()
while (x, y) not in loop:
    loop.add((x, y))
    x, y = x + dx, y + dy
    dx, dy = {'F': (-dy, -dx), 'J': (-dy, -dx), 'L': (dy, dx), '7': (dy, dx), '-': (dx, dy), '|': (dx, dy)}[m[(x, y)]]
print("Part 1:", len(loop) // 2)
print("Part 2:", sum([1 for (x, y) in m.keys() if (x, y) not in loop and ''.join([m[(i, y)] for i in range(x) if (i, y) in loop and m[(i, y)] != '-']).replace('L7', '|').replace('FJ', '|').count('|') % 2]))


