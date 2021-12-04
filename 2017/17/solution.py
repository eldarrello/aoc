n = 314
b = [0]
p = 0
for i in range(1, 2017 + 1):
    p += n % len(b)
    p %= len(b)
    p += 1
    b.insert(p, i)
print("Part 1:", b[p + 1])

s = 1
for i in range(1, 50000000):
    p += n % s
    p %= s
    if p == 0:
        pp = i
    p += 1
    s += 1
print("Part 2:", pp)
