s = open('input.txt').read().splitlines()
map = ''
w = 0
for i in s:
    if len(i) > w:
        w = len(i)
for i in s:
    map +=i.ljust(w)
x = map.index('|')
y = 1
d = (0, 1)
path = []
count = 1
while True:
    c = map[w * y + x]
    if c == '+':
        if d == (0, 1) or d == (0, -1):
            if map[w * y + x + 1] != ' ':
                d = (1, 0)
            elif map[w * y + x - 1] != ' ':
                d = (-1, 0)
            else:
                print('x')
                break
        elif d == (1, 0) or d == (-1, 0):
            if y + 1 < 200 and map[w * (y + 1) + x] != ' ':
                d = (0, 1)
            elif map[w * (y - 1) + x] != ' ':
                d = (0, -1)
            else:
                print('y')
                break
    if c.isalpha():
        path.append(c)
    if c == ' ':
        break
    x += d[0]
    y += d[1]
    count += 1
    if y < 1 or x < 1:
        break

print("Part 2:", ''.join(path))
print("Part 2:", count)
