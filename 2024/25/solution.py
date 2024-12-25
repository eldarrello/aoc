import itertools
acc = 0
for a, b in [(a.splitlines(), b.splitlines()) for a, b in itertools.combinations(open('input.txt').read().split('\n\n'), 2)]:
    if not sum([1 for y in range(len(a)) for x in range(len(a[0])) if a[y][x] == '#' and b[y][x] == '#']):
        acc += 1
print("Part 1:", acc)


