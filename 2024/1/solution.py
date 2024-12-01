s = open('input.txt').read().splitlines()
aa = []
bb = []
for i in s:
    a, b = i.split('   ')
    aa.append(int(a))
    bb.append(int(b))
aa = sorted(aa)
bb = sorted(bb)
acc = 0
acc2 = 0
for i in range(len(aa)):
    acc += abs(aa[i] - bb[i])
    acc2 += aa[i] * bb.count(aa[i])
print("Part 1:", acc)
print("Part 2:", acc2)