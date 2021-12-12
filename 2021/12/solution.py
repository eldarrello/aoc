ps = {}
for i in open('input.txt').read().splitlines():
    s, d = i.split('-')
    ps[s] = ps[s] + [d] if s in ps else [d]
    ps[d] = ps[d] + [s] if d in ps else [s]

def eval(part):
    count = 0
    nodes = [('start', ['start'])]
    while nodes:
        node, path = nodes.pop()
        if node == 'end':
            count += 1
            continue
        nodes += [(i, list(path + ([i] if i[0].islower() else []))) for i in ps[node] if not i[0].islower() or path.count(i) == 0 or
                  (i not in ['start', 'end'] and part and len(path) == len(set(path)))]
    return count
print("Part 1:", eval(0))
print("Part 2:", eval(1))



