m = sum([sum([5 ** i * {'0': 0, '1': 1, '2': 2, '-': -1, '=': -2}[l[::-1][i]] for i in range(len(l))]) for l in open('input.txt').read().splitlines()])
v = []
while m:
    m, k = divmod(m, 5)
    v.insert(0, ['0', '1', '2', '=', '-'][k])
    m += 1 if k > 2 else 0
print("Part 1:", ''.join(v))
