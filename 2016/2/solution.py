s = open('input.txt').read().splitlines()

map1 = {(0, 0):'1', (1, 0):'2', (2, 0):'3', (0, 1):'4', (1, 1):'5', (2, 1):'6', (0, 2):'7', (1, 2):'8', (2, 2):'9'}
map2 = {(2, 0):'1', (1, 1):'2', (2, 1):'3', (3, 1):'4', (0, 2):'5', (1, 2):'6', (2, 2):'7', (3, 2):'8', (4, 2):'9', (1, 3):'A', (2, 3):'B', (3, 3):'C', (2, 4):'D'}

def find(x, y, map):
    codes = []
    for k in s:
        for m in k:
            dy = 0
            dx = 0
            if m == 'U':
                dy = -1
            if m == 'L':
                dx = -1
            if m == 'R':
                dx = 1
            if m == 'D':
                dy = 1
            if (x + dx, y + dy) in map:
                y += dy
                x += dx
        codes.append(map[(x, y)])
    return "".join(codes)
print('Part 1:', find(1, 1, map1))
print('Part 2:', find(0, 2, map2))
