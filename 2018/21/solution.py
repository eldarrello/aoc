a3 = 0
v = []
while v.count(a3) < 2:
    a1 = a3 | 0x10000
    a3 = 10373714
    while a1:
        a3 += a1 & 255
        a3 &= 0xffffff
        a3 *= 65899
        a3 &= 0xffffff
        if a1 < 256:
            v.append(a3)
        a1 = a1 // 256
print("Part 1:", v[0])
print("Part 2:", v[-2])


