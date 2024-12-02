def is_safe(vs):
    if vs == sorted(vs) or vs == sorted(vs, reverse=True):
        for k in range(1, len(vs)):
            d = abs(vs[k] - vs[k - 1])
            if d < 1 or d > 3:
                break
        else:
            return 1
    return 0
s = open('input.txt').read().splitlines()
acc = 0
acc2 = 0
for i in s:
    vs = list(map(int, i.split(' ')))
    acc += is_safe(vs)
    acc2 += 1 if sum([is_safe(vs[:j] + vs[j + 1:]) for j in range(len(vs))]) > 0 else 0
print("Part 1:", acc)
print("Part 2:", acc2)

