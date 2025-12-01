s = open('input.txt').read().splitlines()
p = 50
acc1 = 0
acc2 = 0
for i, l in enumerate(s):
    val = int(l[1:])
    if l[0] == "L":
        if val >= p and p > 0:
            acc2 += 1
        val = -val
    acc2 += abs(p + val) // 100
    p = (p + val) % 100
    if p == 0:
        acc1 += 1
print("Part 1:", acc1)
print("Part 2:", acc2)