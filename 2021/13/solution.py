m = {(int(i.split(',')[0]), int(i.split(',')[1])) for i in open('input.txt').read().splitlines() if ',' in i}
folds = []
for i in open('input.txt').read().splitlines():
    if '=' in i:
        a, b = i.split(' ')[2].split('=')
        for x, y in list(m):
            m.remove((x, y))
            m.add((2 * int(b) - x if a == 'x' and x > int(b) else x, 2 * int(b) - y if a == 'y' and y > int(b) else y))
        folds.append(len(m))
print("Part 1:", folds[0])
for y in range(6):
    print("Part 2:", ''.join(['x ' if (x, y) in m else '  ' for x in range(100)]))



