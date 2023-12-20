import math
m = {}
for i in open('input.txt').read().splitlines():
    k, ds = i.split(' -> ')
    m[k[1:]] = (k[:1], ds.split(', '))
ss = {key: {k: 0 for k, v in m.items() if key in v[1]} for key, d in m.items() if d[0] == '&'}
ff = {key: 0 for key, d in m.items() if d[0] == '%'}
low = 0
high = 0
w = {}
x = set()
q = set()
for i in range(1, 5000):
    inputs = [('roadcaster', '', 0)]
    low += 1
    while inputs:
        k, s, input = inputs.pop(0)
        if k in ff:
            if input != 0:
                continue
            ff[k] = 1 - ff[k]
            pulse = ff[k]
        elif k in ss:
            ss[k][s] = input
            pulse = 0 if sum(list(ss[k].values())) == len(ss[k]) else 1
        else:
            pulse = 0
        for d in m[k][1] if k in m else []:
            inputs.append((d, k, pulse))
            high += pulse
            low += 1 - pulse
    if i == 1000:
        print("Part 1:", high * low)
    for k, v in ss.items():
        for a, b in v.items():
            if b == 1 and a not in w:
                w[a] = i
            if b == 0 and a in w:
                if a not in x:
                    x.add(a)
                    if w[a] != i - w[a]:
                        q.add(i)
print("Part 2:", math.prod(list(q)))


