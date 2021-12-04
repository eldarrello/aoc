file = "input.txt"
s = open(file).read().splitlines()
s = ''.join(s)

def bugx(l, x, y):
    s = levels[l] if l in levels else ['.' for x in range(25)]
    return 1 if s[5 * y + x] == '#' else 0

def bug(l, x, dx, y, dy):
    x += dx
    y += dy
    if x < 0:
        return bugx(l - 1, 1, 2)
    if x > 4:
        return bugx(l - 1, 3, 2)
    if y < 0:
        return bugx(l - 1, 2, 1)
    if y > 4:
        return bugx(l - 1, 2, 3)
    bugs = bugx(l, x, y)
    if x == 2 and y == 2:
        if dx == 1:
            for y in range(5):
                bugs += bugx(l + 1, 0, y)
        if dx == -1:
            for y in range(5):
                bugs += bugx(l + 1, 4, y)
        if dy == 1:
            for x in range(5):
                bugs += bugx(l + 1, x, 0)
        if dy == -1:
            for x in range(5):
                bugs += bugx(l + 1, x, 4)
    return bugs

def run(l, part_2):
    s1 = []
    for y in range(5):
        for x in range(5):
            bugs = bug(l, x, -1, y, 0)
            bugs += bug(l, x, 1, y, 0)
            bugs += bug(l, x, 0, y, -1)
            bugs += bug(l, x, 0, y, 1)
            v = '#' if bug(l, x, 0, y, 0) else '.'
            if v == '#':
                if bugs != 1:
                    v = '.'
            else:
                if bugs == 1 or bugs == 2:
                    v = '#'
            if part_2:
                if x == 2 and y == 2:
                    v = '.'
            s1.append(v)
    return s1

def get_bio(s):
    b = 0
    for i in range(len(s)):
        if s[i] == '#':
            b += 2 ** i
    return b

#part_1
levels = {}
levels[0] = s
map = {}
while True:
    levels[0] = run(0, False)
    #print(levels[0])
    bio = get_bio(levels[0])
    if bio in map:
        print('Part 1:', bio)
        break
    else:
        map[bio] = 1
#part_2
levels = {}
next_levels = {}
n = 100
for l in range(-n, n + 2):
    levels[l] = ['.' for x in range(25)]

levels[0] = s
for k in range(200):
    for l in range(-n, n + 1):
        next_levels[l] = run(l, True)
    levels = next_levels.copy()
count = 0
for l in range(-n, n + 1):
    count += levels[l].count('#')
    #print(l, levels[l])
print('Part 2:', count)

#1983 too high