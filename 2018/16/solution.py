def calc(op, a, b, c, r):
    r[c] = {0: r[a] + r[b], 1: r[a] + b, 2: r[a] * r[b], 3: r[a] * b, 4: r[a] & r[b],
            5: r[a] & b, 6: r[a] | r[b], 7: r[a] | b, 8: r[a], 9: a,
            10: 1 if a > r[b] else 0, 11: 1 if r[a] > b else 0, 12: 1 if r[a] > r[b] else 0,
            13: 1 if a == r[b] else 0, 14: 1 if r[a] == b else 0, 15: 1 if r[a] == r[b] else 0}[op]

s = open('input.txt').read().split('\n\n\n\n')
cases = s[0].split('\n\n')
m = {}
acc = 0
for i in cases:
    before, op, after = i.splitlines()
    ks = []
    for k in range(16):
        r = eval(before.split(':')[-1])
        h = [k] + [int(i) for i in op.split()[1:]]
        calc(*h, r)
        if r == eval(after.split(':')[-1]):
            ks.append(k)
    if len(ks) >= 3:
        acc += 1
    op = op.split()[0]
    if op in m:
        m[op] = set(ks).intersection(m[op])
    m[op] = set(ks)
print("Part 1:", acc)
f = {}
while len(m):
    for k, v in m.items():
        if len(v) == 1:
            f[k] = list(v)[0]
            for k1, v1 in m.items():
                if f[k] in v1:
                    m[k1].remove(f[k])
    for k in f.keys():
        if k in m:
            del m[k]
r = [0, 0, 0, 0]
for op in s[1].splitlines():
    op = op.split()
    op_code = f[op[0]]
    op = [int(i) for i in op]
    op[0] = op_code
    calc(*op, r)
print("Part 2:", r[0])

