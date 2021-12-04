s = open('input.txt').read().splitlines()
px = []
py = []
vx = []
vy = []
for i in s:
    z = i.replace('position=<', '').replace('> velocity=<', ',').rstrip('>').split(',')
    values = [int(k) for k in z]
    px.append(values[0])
    py.append(values[1])
    vx.append(values[2])
    vy.append(values[3])
n = len(px)
min_h = 1000000
t = 0
while(1):
    for i in range(n):
        px[i] += vx[i]
        py[i] += vy[i]
    h = max(py) - min(py)
    t += 1
    if h < min_h:
        min_h = h
        if h == 9:
            m = {}
            for i in range(n):
                m[(px[i] - min(px), py[i] - min(py))] = 'X'
            for y in range(10):
                row = []
                for x in range(62):
                    row.append('X' if (x, y) in m else ' ')
                print(' '.join(row))
            print("Part 2:", t)
            break

