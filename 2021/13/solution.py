s = open('input.txt').read().splitlines()
m = {}
folds = []
for i in s:
    if (',') in i:
        x, y = i.split(',')
        m[(int(x), int(y))] = 1
    elif '=' in i:
        _, _, t = i.split(' ')
        folds.append(t)
for fold in range(len(folds)):
    a, b = folds[fold].split('=')
    b = int(b)
    for x, y in list(m.keys()):
        del m[(x, y)]
        m[(2 * b - x if a == 'x' and x > b else x, 2 * b - y if a == 'y' and y > b else y)] = 1
    if fold == 0:
        print("Part 1:", len(m.keys()))
for y in range(10):
    print(''.join(['x ' if (x, y) in m else '  ' for x in range(100)]))



