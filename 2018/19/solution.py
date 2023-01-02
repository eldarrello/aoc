s = open('input.txt').read().splitlines()
ip_reg = int(s[0].split('#ip ')[1])
def calc(op, a, b, c, r):
    r[c] = {'addr': r[a] + r[b], 'addi': r[a] + b, 'mulr': r[a] * r[b], 'muli': r[a] * b,
            'setr': r[a], 'seti': a,
    'gtir': 1 if a > r[b] else 0, 'gtri': 1 if r[a] > b else 0, 'gtrr': 1 if r[a] > r[b] else 0,
    'eqir': 1 if a == r[b] else 0, 'eqri': 1 if r[a] == b else 0, 'eqrr': 1 if r[a] == r[b] else 0}[op]
m = []
for i in s[1:]:
    op, a, b, c = i.split()
    m.append((op, int(a), int(b), int(c)))
r = [0 for i in range(20)]
while True:
    ip = r[ip_reg]
    if ip >= len(m):
        break
    op, a, b, c = m[ip]
    pre = str(r[:6]) + str(m[ip])
    calc(op, a, b, c, r)
    r[ip_reg] += 1
print("Part 1:", r[0])
# There is double loop in ips 2 - 15, which transforms to the following code:
print("Part 2:", sum([x for x in range(1, 10551275 + 1) for y in range(1, 10551275 // x + 1) if x * y == 10551275]))

