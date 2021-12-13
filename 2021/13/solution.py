m = {(map(int, i.split(','))) for i in open('input.txt').read().splitlines() if ',' in i}
folds = []
for a, b in [i.split(' ')[2].split('=') for i in open('input.txt').read().splitlines() if '=' in i]:
    m = {(2 * int(b) - x if a == 'x' and x > int(b) else x, 2 * int(b) - y if a == 'y' and y > int(b) else y) for x, y in m}
    folds.append(len(m))
print("Part 1:", folds[0])
[print("Part 2:", ''.join(['x ' if (x, y) in m else '  ' for x in range(100)])) for y in range(6)]