min_x, max_x, min_y, max_y = map(int, open('input.txt').read()[15:].replace('..', ',').replace(' y=', '').split(','))
print("Part 1:", min_y * (min_y + 1) // 2)
def eval(dx, dy):
    x, y = 0, 0
    while x <= max_x and y >= min_y:
        x, y = x + dx, y + dy
        dx, dy = dx - (dx > 0), dy - 1
        if min_x <= x <= max_x and min_y <= y <= max_y:
            return 1
print("Part 2:", sum([eval(dx, dy) != None for dx in range(0, max_x + 1) for dy in range(min_y, abs(min_y))]))