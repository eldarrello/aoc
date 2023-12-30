def get_path(a, b):
    visited = set()
    nodes = [(a, [a])]
    while nodes:
        node, path = nodes.pop(0)
        if node not in visited:
            visited.add(node)
            for node in m[node]:
                if node == b:
                    return path + [b]
                nodes.append((node, path + [node]))
    return []

def get_visited(a):
    visited = set()
    nodes = [a]
    while nodes:
        node = nodes.pop(0)
        visited.add(node)
        for node in m[node]:
            if node not in visited:
                nodes.append(node)
    return len(visited)

m = {}
s = open('input.txt').read().splitlines()
for i in s:
    a, bs = i.split(': ')
    if a not in m:
        m[a] = []
    for b in bs.split():
        m[a].append(b)
        if b not in m:
            m[b] = []
        m[b].append(a)
ws = {}
n = 20      #20 is found experimentally to make it faster. Otherwise should go through all combinations. n = 20 takes ~20sec
for a in list(m.keys())[:n]:
    for b in [k for k in m.keys() if k != a]:
        p = get_path(a, b)
        for i in range(len(p) - 1):
            w1 = (p[i], p[i + 1])
            w2 = (p[i + 1], p[i])
            if w1 in ws:
                ws[w1] += 1
            elif w2 in ws:
                ws[w2] += 1
            else:
                ws[w1] = 1
ws = [(k, v) for k, v in ws.items()]
ws.sort(key=lambda x: x[1], reverse = True) # Idea here is to find 3 wires which were visited the most.
for (a, b), _ in ws[:3]:
    m[a].remove(b)
    m[b].remove(a)
a = get_visited(list(m.keys())[0])
print("Part 1:", a * (len(m.keys()) - a))