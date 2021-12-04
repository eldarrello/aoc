s = open('input.txt').read().splitlines()
s = [[int(k) for k in list(i)] for i in s]
b = s[0]
for i in range(1, len(s)):
    b = [sum(x) for x in zip(b, s[i])]
r = int(''.join(['1' if i > len(s) - i else '0' for i in b]), 2)
h = int(''.join(['0' if i > len(s) - i else '1' for i in b]), 2)
print("Part 1:",  r * h)

def filter(c):
    w = s
    for b in range(len(w[0])):
        w = [w[i] for i in range(len(w)) if w[i][b] != (0 if len(w) - 2 * sum([w[i][b] for i in range(len(w))]) > 0 else 1) ^ c]
        if len(w) == 1:
            break
    return int(''.join([str(i) for i in w[0]]), 2)

print("Part 2:", filter(0) * filter(1))

