s = open('input.txt').read().splitlines()
x = 0
depth = 0
aim = 0
for i in s:
    c = i.split(' ')
    if c[0] == 'up':
        aim -= int(c[1])
    if c[0] == 'down':
        aim += int(c[1])
    if c[0] == 'forward':
        x += int(c[1])
        depth += aim * int(c[1])
print("Part 1:", x * aim)
print("Part 2:", x * depth)