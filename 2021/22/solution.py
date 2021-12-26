def cc(a):
    d = 1
    for i in range(3):
        d *= a[i][1] - a[i][0] + 1
    return d

def overlaps(a, b):
    c = 0
    for i in range(3):
        if b[i][0] <= a[i][0] <= b[i][1] or b[i][0] <= a[i][1] <= b[i][1] or a[i][0] <= b[i][0] <= a[i][1] or a[i][0] <= b[i][1] <= a[i][1]:
            c += 1
    return c == 3

#subtract b from a and return fractions
def sub(a, b):
    result = []
    for i in range(3):
        w = list(a)
        if b[i][0] <= a[i][0]:
            if b[i][1] >= a[i][1]:
                rem = a[i]
            else:
                v = [b[i][1] + 1, a[i][1]]
                rem = a[i][0], b[i][1]
                w[i] = v
                result.append(w)
        else:
            v = [a[i][0], b[i][0] - 1]
            rem = b[i][0], a[i][1]
            if a[i][1] > b[i][1]:
                w[i] = v
                result.append(w)
                v = b[i][1] + 1, a[i][1]
                w = list(a)
                rem = b[i][0], b[i][1]
            w[i] = v
            result.append(w)
        a[i] = rem
    return result

s = open('input.txt').read().splitlines()
cs = []
for i in s:
    on, i = i.split(' ')
    i = [list(map(int, k.split('=')[1].split('..'))) for k in i.split(',')]
    cs.append((on, i))
on = []
for i in range(len(cs)):
    s, a = cs[i]
    cp = list(on)
    for j in range(len(cp)):
        b = cp[j]
        if overlaps(a, b):
            on.remove(b)
            r = sub(b, a)
            on += r
    if s == 'on':
        on.append(a)
total = 0
for i in on:
    total += cc(i)
print("Part 2:", total)

m = 10000000
f = [(-m, m), (-m, m), (-m, m)]
m = 50
outer = sub(f, [(-m, m), (-m, m), (-m, m)])

for a in outer:
    cp = list(on)
    for j in range(len(cp)):
        b = cp[j]
        if overlaps(a, b):
            on.remove(b)
            r = sub(b, a)
            on += r
total = 0
for i in on:
    total += cc(i)
print("Part 1:", total)