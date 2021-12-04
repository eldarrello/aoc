s = open('input.txt').read().splitlines()
total = 0
for i in s:
    dm = -2
    x = 0
    while x < len(i):
        v = i[x]
        if v == '\\':
            if i[x + 1] == 'x':
                dm -= 2
            x += 1
        dm += 1
        x += 1
    total += len(i) - dm
print('Part 1:', total)
ss = ''.join(s)
t1 = ss.count('\\')
t2 = ss.count('\"')
print('Part 2:', t1 + t2 + len(s) * 2)
