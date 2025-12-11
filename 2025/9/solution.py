s = open('input.txt').read().splitlines()
ps = [list(map(int, l.split(','))) for l in s]
print("Part 1:", max((abs(ps[i][0] - ps[j][0]) + 1) * (abs(ps[i][1] - ps[j][1]) + 1) for i in range(len(ps)) for j in range(i + 1, len(ps))))
'''
import matplotlib.pyplot as plt
x, y = [p[0] for p in ps], [p[1] for p in ps]
plt.figure(figsize=(12, 10))
plt.plot(x + [x[0]], y + [y[0]], 'r-')
plt.fill(x, y, alpha=0.2)
plt.title(f'Polygon with {len(x)} vertices')
plt.grid(True)
plt.gca().set_aspect('equal')
plt.show()
'''
ps = ps[:len(ps) // 2 + 1]      # insight from the plot that the max rectangle can be either in the first half or in the second
x2, y2 = ps[-1]
max_area = 0
for i in range(len(ps)):
    x1, y1 = ps[i]
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    for i in range(len(ps)):
        x, y = ps[i]
        if min_x < x < max_x and min_y < y < max_y:
            break
    else:
        max_area = max(max_area, (max_x - min_x + 1) * (max_y - min_y + 1))
print("Part 2:", max_area)

