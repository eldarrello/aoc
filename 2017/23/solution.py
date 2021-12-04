s = open('input.txt').read().splitlines()
r = {chr(c):0 for c in range(ord('a'), ord('h') + 1)}
i = 0
count = 0
while True:
    if i >= len(s):
        break
    c, a, b = s[i].split()
    if b in r:
        b = r[b]
    else:
        b = int(b)
    if c == 'set':
        r[a] = b
    if c == 'sub':
        r[a] -= b
    if c == 'mul':
        count += 1
        r[a] *= b
    if a in r:
        a = r[a]
    else:
        a = int(a)
    if c == 'jnz' and a != 0:
        i += b
    else:
        i += 1
print("Part 1:", count)
acc = 0
for b in range(109900, 126900 + 17, 17):
    for d in range(2, b + 1):
        if b % d == 0 and b // d >= 2:
            break
    else:
        continue
    acc += 1
print("Part 2:", acc)
