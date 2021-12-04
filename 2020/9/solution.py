import itertools
s = [int(i) for i in open('input.txt').read().splitlines()]
v = next(s[i] for i in range(25, len(s)) if s[i] not in [sum(x) for x in itertools.combinations(s[i - 25: i], 2)])
print("Part 1:", v)
for i in range(len(s)):
    acc = 0
    for k in range(i, len(s)):
        acc += int(s[k])
        if acc == v:
            f = s[i:k]
            f = [int(x) for x in f]
            print("Part 2:", min(f) + max(f))
            exit()
        if acc > v:
            break



