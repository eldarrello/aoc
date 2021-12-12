s = open('input.txt').read().splitlines()
ps = {}
for i in s:
    p = i.split('-')
    if p[0] in ps:
        ps[p[0]] = ps[p[0]] + [p[1]]
    else:
        ps[p[0]] = [p[1]]
    if p[1] in ps:
        ps[p[1]] = ps[p[1]] + [p[0]]
    else:
        ps[p[1]] = [p[0]]
caves = [i for i in ps.keys() if i[0].islower()]

def eval(part):
    count = 0
    nodes = [i for i in ps['start']]
    path = ['start']
    while nodes:
        node = nodes.pop()
        if node == 'back':
            path.pop()
            continue
        path.append(node)
        if node == 'end':
            count += 1
            path.pop()
            continue
        nodes.append('back')
        for next in ps[node]:
            if next[0].islower():
                if path.count(next) > 0:
                    if next in ['start', 'end'] or [1 for cave in caves if path.count(cave) > part]:
                        continue
            nodes.append(next)
    return count
print("Part 1:", eval(0))
print("Part 2:", eval(1))



