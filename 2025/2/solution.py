s = open('input.txt').read().split(',')
acc1 = 0
acc2 = 0
for r in s:
    a, b = map(int, r.split('-'))
    for i in range(a, b + 1):
        si = str(i)
        l = len(si)
        invalid = False
        for c in range(1, l // 2 + 1):
            k = l // c
            if l / c == k:
                for j in range(1, k):
                    if si[j * c:j * c + c] != si[:c]:
                        break
                else:
                    invalid = True
                    if c == l // 2 and l // 2 == l / 2:
                        acc1 += i
        if invalid:
            acc2 += i
print("Part 1:", acc1)
print("Part 2:", acc2)

