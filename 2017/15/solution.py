s = open('input.txt').read().splitlines()
a = int(s[0].split(' ')[-1])
b = int(s[1].split(' ')[-1])
t = 0
c = 0
while True:
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a & 0xffff == b & 0xffff:
        c += 1
    t += 1
    if t > 40000000:
        break
print("Part 1:", c)
a = int(s[0].split(' ')[-1])
b = int(s[1].split(' ')[-1])
t = 0
c = 0
while True:
    while True:
        a = (a * 16807) % 2147483647
        if a & 3 == 0:
            break
    while True:
        b = (b * 48271) % 2147483647
        if b & 7 == 0:
            break
    if a & 0xffff == b & 0xffff:
        c += 1
    t += 1
    if t > 5000000:
        break
print("Part 2:", c)
