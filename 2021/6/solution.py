s = open('input.txt').read().splitlines()
n = [[int(x) for x in s[0].split(',')].count(i) for i in range(9)]
for i in range(256):
    n[(i + 7) % 9] += n[i % 9]
    if i == 79:
        print("Part 1:", sum(n))
print("Part 2:", sum(n))

