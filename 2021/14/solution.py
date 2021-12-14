f, s = open('input.txt').read().split('\n\n')
m = {}
for i in s.splitlines():
    s, d = i.split(' -> ')
    m[s] = d

def eval(n):
    pairs = {}
    for i in range(len(f) - 1):
        i = f[i] + f[i + 1]
        pairs[i] = 1 if i not in pairs else pairs[i] + 1
    for t in range(1, n + 1):
        tt = {}
        for i in pairs.keys():
            p1 = i[0] + m[i]
            p2 = m[i] + i[1]
            tt[p1] = pairs[i] if p1 not in tt else (tt[p1] + pairs[i])
            tt[p2] = pairs[i] if p2 not in tt else (tt[p2] + pairs[i])
        pairs = tt
        n = {}
        for i in pairs.keys():
            a = i[0]
            b = i[1]
            n[a] = pairs[i] if a not in n else n[a] + pairs[i]
            n[b] = pairs[i] if b not in n else n[b] + pairs[i]
    mins = 1000000000000
    maxs = 0
    for i in n.keys():
        v = n[i] // 2 if n[i] % 2 == 0 else (n[i] - 1) // 2 + 1
        mins = min(mins, v)
        maxs = max(maxs, v)
    return maxs - mins
print("Part 1:", eval(10))
print("Part 2:", eval(40))