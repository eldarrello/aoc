def get(x, y, n):
    v = ((x + 10) * y + n) * (x + 10)
    v //= 100
    v %= 10
    v -= 5
    return v

def find_max(max_size):
    max_sum = 0
    r = None
    for y in range(1, 300):
        for x in range(1, 300):
            sum = 0
            for i in range(1, min(300 - max(x, y), max_size + 1)):
                for j in range(i):
                    sum += m[(x + j, y + i - 1)]
                for j in range(i - 1):
                    sum += m[(x + i - 1, y + j)]
                if sum > max_sum:
                    max_sum = sum
                    r = x, y, i
    return r

m = {}
for y in range(1, 301):
    for x in range(1, 301):
        m[(x, y)] = get(x, y, 5034)
part_1 = find_max(3)
print("Part 1:", '{},{}'.format(part_1[0], part_1[1]))
print("Part 2:", ','.join([str(i) for i in find_max(30)]))
#todo::full search for part 2 is too slow, so it has limited to 30x30
