s = open('input.txt').read().splitlines()
map = {}
for i in s:
    i = i.split(' ')
    if len(i) > 2:
        if i[0] in map:
            map[i[0]].append(i[2])
        else:
            map[i[0]] = [i[2]]
    elif len(i) == 1:
        m = i[0]

combs = set()
for k, v in map.items():
    ps = [n for n in range(len(m)) if m.find(k, n) == n]
    for j in v:
        for i in ps:
            combs.add(m[:i] + j + m[i + len(k):])
print('Part 1:', len(combs))

#reddit insight: You can generalize to X => X(X,X) by noting that each , reduces the length by two (,X).
# The new formula is count(tokens) - count("(" or ")") - 2*count(",") - 1.
y = m.count('Y')
ar = m.count('Ar')
tokens = 0
for i in m:
    if i.isupper():
        tokens += 1

print('Part 2:', tokens - 2 * ar - 2 * y - 1)
