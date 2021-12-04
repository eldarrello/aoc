import copy
s = open('input.txt').read().splitlines()
map = {}
for i in s:
    i = i.split(' <-> ')
    map[int(i[0])] = [int(x) for x in i[1].split(', ')]
def eval(n):
    nodes = copy.deepcopy(map[n])
    all = set()
    while nodes:
        node = nodes.pop(0)
        all.add(node)
        for i in map[node]:
            if i in all or i in nodes:
                continue
            nodes.append(i)
    return all
print("Part 1:", len(eval(0)))
groups = set()
for i in range(len(s)):
    group = ','.join([str(x) for x in sorted(eval(i))])
    groups.add(group)
print("Part 2:", len(groups))
