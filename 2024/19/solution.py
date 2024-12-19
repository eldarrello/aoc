def comb(p):
    c = 0
    for k in range(1, 9):
        if p[:k] in gs:
            if k == len(p):
                c += 1
            if p[k:] not in cache:
                cache[p[k:]] = comb(p[k:])
            c += cache[p[k:]]
    return c
a, b = open('input.txt').read().split('\n\n')
gs = set(a.split(', '))
cache = {}
cc = [comb(p) for p in b.splitlines()]
print("Part 1:", len(cc) - cc.count(0))
print("Part 2:", sum(cc))
