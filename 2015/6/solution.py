s = open('input.txt').read().splitlines()
map1 = [0 for x in range(1000 * 1000)]
map2 = [0 for x in range(1000 * 1000)]
for i in s:
    i = i.replace("turn on", "turnon")
    i = i.replace("turn off", "turnoff")
    p = i.split(' ')
    com = p[0]
    c1 = p[1].split(',')
    c2 = p[3].split(',')
    for x in range(int(c1[0]), int(c2[0]) + 1):
        for y in range(int(c1[1]), int(c2[1]) + 1):
            if com == "turnon":
                map1[y * 1000 + x] = 1
                map2[y * 1000 + x] += 1
            elif com == "turnoff":
                map1[y * 1000 + x] = 0
                if map2[y * 1000 + x] > 0:
                    map2[y * 1000 + x] -= 1
            elif com == "toggle":
                map1[y * 1000 + x] ^= 1
                map2[y * 1000 + x] += 2
print('Part 1:', map1.count(1))
print('Part 2:', sum(map2))