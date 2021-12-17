tx, ty = map(lambda i: range(i[0], i[1] + 1), map(lambda i: list(map(int, i.split('..'))), map(lambda i: i.split('=')[1], open('input.txt').read().split(', '))))
tmax_y = 0
part_2 = 0
for svx in range(0, max(tx) + 1):
    for svy in range(min(ty), max(tx)):
        x = 0
        y = 0
        vx = svx
        vy = svy
        max_y = 0
        for step in range(1000):
            if vx != 0:
                x += vx
                vx += 1 if vx < 0 else -1
            elif x not in tx:
                break
            y += vy
            max_y = max(max_y, y)
            vy -= 1
            if x in tx and y in ty:
                part_2 += 1
                tmax_y = max(tmax_y, max_y)
                break
print("Part 1:", tmax_y)
print("Part 2:", part_2)