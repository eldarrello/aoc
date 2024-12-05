a, b = open('input.txt').read().split("\n\n")
m = {}
for c, d in [i.split('|') for i in a.splitlines()]:
    m[c] = [d] if c not in m else m[c] + [d]
acc = 0
acc2 = 0
for vs in [i.split(',') for i in b.splitlines()]:
    q = list(vs)
    for j in [j for i in range(len(q) - 1) for j in range(len(q) - i - 1)]:
        if q[j + 1] in m and q[j] in m[q[j + 1]]:
            q[j], q[j + 1] = q[j + 1], q[j]
    acc += int(q[len(q) // 2]) if vs == q else 0
    acc2 += int(q[len(q) // 2]) if vs != q else 0
print("Part 1:", acc)
print("Part 2:", acc2)

