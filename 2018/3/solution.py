s = open('input.txt').read().splitlines()
map = {}
def run(part):
    for i in s:
        pos, size = i.split(' @ ')[1].split(': ')
        x, y = [int(i) for i in pos.split(',')]
        w, h = [int(i) for i in size.split('x')]
        found = True
        for yi in range(y, y + h):
            for xi in range(x, x + w):
                p = (xi, yi)
                map[p] = map[p] + 1 if p in map else 1
                if map[p] != 2:
                    found = False
        if part == 2 and found:
            print("Part 2:", i.split(' @ ')[0].strip('#'))
run(1)
print("Part 1:", sum(i >= 2 for i in map.values()))
run(2)

