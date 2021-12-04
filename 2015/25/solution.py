s = open('input.txt').read().splitlines()

b = 20151125
k = 252533
m = 33554393

def get_index(row, col):
    s = sum([x for x in range(1, row)]) + 1
    s += sum([x for x in range(row + 1, row + col)])
    return s

for i in range(1, get_index(3010, 3019)):
    b = b * k % m
print('Part 1:', b)
