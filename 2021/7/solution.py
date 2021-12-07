s = open('input.txt').read().splitlines()
n = [int(x) for x in s[0].split(',')]
print("Part 1:", min([sum([abs(t - i) for i in n]) for t in range(max(n))]))
b = [sum(range(i)) for i in range(1, max(n) + 2)]
print("Part 2:", min([sum([b[abs(t - i)] for i in n]) for t in range(max(n))]))


