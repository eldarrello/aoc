s = open('input.txt').read().splitlines()
fs = [int(x) for x in s[0].split(',')]
n = [fs.count(i) for i in range(9)]

for day in range(256):
    t = n[0]
    n = [n[i + 1] for i in range(8)]
    n.append(t)
    n[6] += t
    if day == 79:
        print("Part 1:", sum(n))
print("Part 2:", sum(n))

