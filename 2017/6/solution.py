s = open('input.txt').read()
s = [int(x) for x in s.split('\t')]
ss = set()
count = 0
n = len(s)
f = None
part_1 = None
while True:
    h = ''.join([str(x) for x in s])
    if f == h:
        break
    if part_1 == None and h in ss:
        part_1 = count
        f = h
    ss.add(h)
    m = max(s)
    c = s.index(m)
    s[c] = 0
    d = m // n
    s = [x + d for x in s]
    r = m - d * n
    for i in range(r):
        k = (c + i + 1) % n
        s[k] += 1
    count += 1
print("Part 1:", part_1)
print("Part 2:", count - part_1)