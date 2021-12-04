def part1():
    x = [x for x in range(3018458)]
    pos = 0
    count = 0
    while True:
        while x[pos] < 0:
            pos += 1
            if pos >= len(x):
                pos = 0
        pos += 1
        if pos >= len(x):
            pos = 0
        while x[pos] < 0:
            pos += 1
            if pos >= len(x):
                pos = 0
        count += 1
        if count == len(x):
            return x[pos] + 1
        x[pos] = -1
#Based on pattern: repeates every 3 multiple, then first chunck increments by one and second part by 2
def part2(x):
    y = 1
    while y < x:
        y *= 3
    if x == y:
        return x
    y //= 3
    x -= y
    if x <= y:
        return x
    return 2 * (x - y) + y


print("Part 1:", part1())
print("Part 2:", part2(3018458))
