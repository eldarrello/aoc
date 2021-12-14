from collections import defaultdict
f, s = open('input.txt').read().split('\n\n')
m = {i.split(' -> ')[0]: i.split(' -> ')[1] for i in s.splitlines()}
def eval(n):
    pairs = defaultdict(lambda: 0)
    for i in [f[i] + f[i + 1] for i in range(len(f) - 1)]:
        pairs[i] += 1
    for t in range(1, n + 1):
        for k, v in list(pairs.items()):
            pairs[k] -= v
            pairs[k[0] + m[k]] += v
            pairs[m[k] + k[1]] += v
    g = {sum([v for k, v in pairs.items() if x == k[0]]) + (1 if x == f[-1] else 0) for x in set(f)}
    return max(g) - min(g)
print("Part 1:", eval(10))
print("Part 2:", eval(40))