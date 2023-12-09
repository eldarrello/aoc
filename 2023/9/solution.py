s = open('input.txt').read().splitlines()
acc1 = 0
acc2 = 0
for i in s:
    d = [list(map(int, i.split()))]
    while d[-1].count(0) < len(d[-1]):
        d.append([])
        for j, _ in enumerate(d[-2][:-1]):
            d[-1].append(d[-2][j + 1] - d[-2][j])
    acc1 += sum([d[i][-1] for i in range(len(d))])
    acc2 += sum([d[k][0] if k % 2 == 0 else -d[k][0] for k in range(len(d) - 2, -1, -1)])
print("Part 1:", acc1)
print("Part 2:", acc2)
