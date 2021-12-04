s = open('input.txt').read().splitlines()
ack = 0
for i in s:
    d = i.split('x')
    d = [int(x) for x in d]
    a = [d[0] * d[1], d[1] * d[2], d[2] * d[0]]
    m = min(a)
    q = 2 * sum(a) + m
    ack += q
print('Part 1:', ack)
ack = 0
for i in s:
    d = i.split('x')
    d = [int(x) for x in d]
    d.sort()
    ack += 2 * d[0] + 2 * d[1]
    ack += d[0] * d[1] * d[2]
print('Part 2:', ack)