s = open('input.txt').read().splitlines()
total_1 = 0
total_2 = 0
for i in s:
    v = i.split('\t')
    v = [int(x) for x in v]
    total_1 += max(v) - min(v)
    for k in v:
        for j in v:
            if k != j and j / k == j // k:
                total_2 += j // k
print("Part 1:", total_1)
print("Part 2:", total_2)