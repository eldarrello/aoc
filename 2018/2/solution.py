s = open('input.txt').read().splitlines()
c2 = 0
c3 = 0
for i in s:
    h = {}
    for k in i:
        h[k] = h[k] + 1 if k in h else 1
    if 2 in h.values():
        c2 += 1
    if 3 in h.values():
        c3 += 1
print("Part 1:", c2 * c3)
for i in s:
    for j in s:
        if i != j:
            m = [c1 for c1, c2 in zip(i, j) if c1 == c2]
            if len(m) == len(i) - 1:
                print("Part 2:", ''.join(m))
                exit()
