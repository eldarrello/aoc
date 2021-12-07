s = open('input.txt').read().splitlines()
n = [int(x) for x in s[0].split(',')]
print("Part 1:", min([sum([abs(t - i) for i in n]) for t in range(max(n))]))
print("Part 2:", min([sum([abs(t - i) * (abs(t - i) + 1) // 2 for i in n]) for t in range(max(n))]))
