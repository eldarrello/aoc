import itertools
d = {}
for i in open('input.txt').read().splitlines():
    a, b = i.split('-')
    d[a] = d[a] + [b] if a in d else [b]
    d[b] = d[b] + [a] if b in d else [a]
triples = set()
max_cs = 0
for k, vs in d.items():
    abs = [tuple(sorted([k, a, b])) for a, b in list(itertools.combinations(vs, 2)) if b in d[a]]
    triples.update(abs)
    if len(abs) > max_cs:
        max_cs = len(abs)
        acc2 = ','.join(sorted(list(set([x for xs in abs for x in xs]))))
print("Part 1:", sum([1 for t in triples if 't' in ''.join([t[0][0], t[1][0], t[2][0]])]))
print("Part 2:", acc2)
