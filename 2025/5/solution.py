a, b = open('input.txt').read().split("\n\n")
rs = sorted([tuple(map(int, l.split('-'))) for l in a.splitlines()])
mrs = [rs[0]]
for s1, s2 in rs[1:]:
    if s1 <= mrs[-1][1]:
        if s2 > mrs[-1][1]:
            mrs[-1] = (mrs[-1][0], s2)
    else:
        mrs.append((s1, s2))
acc = 0
for l in b.splitlines():
    v = int(l)
    for s1, s2 in mrs:
        if s1 <= v <= s2:
            acc += 1
            break
print("Part 1:", acc)
print("Part 2:", sum([s2 - s1 + 1 for s1, s2 in mrs]))

