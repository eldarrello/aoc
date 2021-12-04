m = {}
all = []
for i in open('input.txt').read().splitlines():
    l, a = i.split(' (contains ')
    l = l.split()
    all += l
    for k in a.strip(')').split(', '):
        if k not in m:
            m[k] = [l]
        else:
            m[k].append(l)
found = {}
for t in range(2):
    for k, v in m.items():
        r = [i for i in list(set.intersection(*map(set, v))) if i not in found]
        if len(r) == 1:
            found[r[0]] = k
print("Part 1:", sum(1 for i in all if i not in found))
print("Part 2:", ','.join([i[0] for i in sorted(list(found.items()), key=lambda x: x[1])]))
