s = open('input.txt').read().splitlines()
c1 = 0
c2 = 0
for i in s:
    ws = i.split()
    r0, r1 = [int(x) for x in ws[0].split('-')]
    c = ws[1][0:1]
    n = ws[2].count(c)
    c1 += 1 if n >= r0 and n <= r1 else 0
    c2 += 1 if (ws[2][r0 - 1] == c) ^ (ws[2][r1 - 1] == c) else 0
print("Part 1:", c1)
print("Part 2:", c2)