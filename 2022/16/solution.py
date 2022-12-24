# assumptions: 1. no dead ends
s = open('input.txt').read().splitlines()
v = {}
ks = ['AA']
for line in s:
    ds = line.replace('valves', 'valve').split('valve ')[1].split(', ')
    ws = line.replace('=', ' ').replace(';', '').split()
    v[ws[1]] = (int(ws[5]), ds)
    if v[ws[1]][0] > 0:
        ks.append(ws[1])

def get_path(a, b):
    nodes = [(a, [a])]
    visited = set()
    while nodes:
        next_nodes = []
        while nodes:
            node, path = nodes.pop(0)
            if node == b:
                return path
            visited.add(node)
            #next_nodes += [(i, path + [i]) for i in v[node][1] if (i not in visited) and (i == b or (v[i][0] == 0 and i != 'AA'))]
            next_nodes += [(i, path + [i]) for i in v[node][1] if (i not in visited)]
        nodes = next_nodes
    return []

paths = {}
for i in ks:
    for j in ks:
        if i == j:
            continue
        path = get_path(i, j)
        if path:
            if i not in paths:
                paths[i] = []
            paths[i].append((j, len(path)))
def eval(n):
    best_score = 0
    best_path = []
    nodes = [('AA', [], [], 0)]
    cc = 0
    while nodes:
        node, opened, times, time = nodes.pop()
        new_nodes = []
        for next_node, dt in paths[node]:
            if next_node in opened:
                continue
            time_to_open = time + dt
            if time_to_open <= n:
                new_nodes.append((next_node, opened + [next_node], times + [time_to_open], time_to_open))
        if new_nodes:
            nodes += new_nodes
        else:
            cc += 1
            score = 0
            delta = 0
            path = []
            for i in range(n + 1):
                score += delta
                if times and times[0] == i:
                    delta += v[opened[0]][0]
                    times.pop(0)
                    path.append(opened.pop(0))
            if score > best_score:
                best_score = score
                #best_path = path
    return best_score

def get_next_nodes(node, opened, time, n):
    nodes = [(next_node, time + dt) for next_node, dt in paths[node] if next_node not in opened and time + dt <= n - 3]
    if not nodes:
       return [(node, time)], False
    return nodes, True

def eval2(n):
    best_score = 0
    best_path = []
    nodes = [('AA', 'AA', [], [], 0, 0)]
    cc = 0
    while nodes:
        nodeA, nodeB, opened, times, timeA, timeB = nodes.pop()
        new_nodes = []
        next_nodeAs, hA = get_next_nodes(nodeA, opened, timeA, n)
        next_nodeBs, hB = get_next_nodes(nodeB, opened, timeB, n)
        if not hA and not hB:
            next_nodeAs = []
        for next_nodeA, next_timeA in next_nodeAs:
            for next_nodeB, next_timeB in next_nodeBs:
                if next_nodeA == next_nodeB:
                    continue
                new_opened = []
                new_times = []
                if next_nodeA not in opened:
                    new_opened.append(next_nodeA)
                    new_times.append(next_timeA)
                if next_nodeB not in opened and next_nodeB not in new_opened:
                    new_opened.append(next_nodeB)
                    new_times.append(next_timeB)
                if len(new_times) == 2 and new_times[1] < new_times[0]:
                    new_times.append(new_times.pop(0))
                    new_opened.append(new_opened.pop(0))
                new_node = (next_nodeA, next_nodeB, opened + new_opened, times + new_times, next_timeA, next_timeB)
                if new_node not in new_nodes:
                    new_nodes.append(new_node)
        if new_nodes:
            nodes += new_nodes
        else:
            cc += 1
            score = 0
            delta = 0
            path = []
            for i in range(n + 1):
                score += delta
                while times and times[0] == i:
                    delta += v[opened[0]][0]
                    times.pop(0)
                    path.append(opened.pop(0))
            if score > best_score:
                best_score = score
                #best_path = path
                #print(score, best_path)
    return best_score
print("Part 1:", eval(30))
#todo::brute force is too slow (~5 min).
print("Part 2:", eval2(26))

