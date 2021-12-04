s = open('input.txt').read().replace(' ', '').split(',')
x = 0
y = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
map = {}
find_2 = True
for i in s:
    if i[:1] == 'L':
        dir += 1
    else:
        dir -= 1
    if dir < 0:
        dir = 3
    if dir == 4:
        dir = 0
    for k in range(int(i[1:])):
        if dirs[dir][0]:
            x += dirs[dir][0]
        else:
            y += dirs[dir][1]
        if (x, y) in map and find_2:
            find_2 = False
            print('Part 2:', abs(x) + abs(y))
        map[(x,y)] = 1
print('Part 1:', abs(x) + abs(y))