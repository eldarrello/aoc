'''
s = sorted([int(i) for i in open('input.txt').read().splitlines()]) + [0]
t = [-1] + [i for i in range(1, len(s)) if s[i] - s[i - 1] != 1]
v = [(t[i] - t[i - 1] - 1) for i in range(1, len(t))]
print("Part", z := 1,":", sum(v) * (len(s) - sum(v)),'\nPart 2:', [z := z * [1, 1, 2, 4, 7][i] for i in v][-1])
'''
s = sorted([int(i) for i in open('input.txt').read().splitlines()]) + [0]
c_1 = 0
k = 0
acc = 1
for i in range(1, len(s)):
    if s[i] - s[i - 1] != 1:
        acc *= [1, 1, 2, 4, 7][i - k]
        c_1 += i - k
        k = i + 1
print("Part 1:", c_1 * (len(s) - c_1))
print("Part 2:", acc)