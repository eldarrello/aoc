def get_path(a, b):
    nodes = [(a, [a])]
    visited = set()
    while nodes:
        next_nodes = []
        for node, path in nodes:
            if node == b:
                return path
            visited.add(node)
            next_nodes += [(i, path + [i]) for i in v[node][1] if (i not in visited)]
        nodes = next_nodes
    return []
def get_next_nodes(node, opened, time_left):
    return [(next_node, dt) for next_node, dt in paths[node] if next_node not in opened and dt < time_left - 2]
def eval(n):
    best_score = 0
    nodes = [('AA', 'AA', [], 0, n, n)]
    while nodes:
            node_a, node_b, opened, score, time_left_a, time_left_b = nodes.pop()
            best_score = max(best_score, score)
            next_node_as = get_next_nodes(node_a, opened, time_left_a)
            next_node_bs = get_next_nodes(node_b, opened, time_left_b) if n == 26 else [(node_b, 1)]
            for next_node_a, dt_a in next_node_as:
                for next_node_b, dt_b in next_node_bs:
                    if next_node_a != next_node_b:
                        new_opened = [next_node_a]
                        dscore = v[next_node_a][0] * (time_left_a - dt_a)
                        if next_node_b != node_b:
                            dscore += v[next_node_b][0] * (time_left_b - dt_b)
                            new_opened.append(next_node_b)
                        nodes.append((next_node_a, next_node_b, opened + new_opened, score + dscore, time_left_a - dt_a, time_left_b - dt_b))
    return best_score
v = {}
ks = ['AA']
for line in open('input.txt').read().splitlines():
    ds = line.replace('valves', 'valve').split('valve ')[1].split(', ')
    ws = line.replace('=', ' ').replace(';', '').split()
    v[ws[1]] = (int(ws[5]), ds)
    if v[ws[1]][0] > 0:
        ks.append(ws[1])
paths = {}
for i in ks:
    for j in ks:
        if i == j or j == 'AA':
            continue
        path = get_path(i, j)
        if path:
            if i not in paths:
                paths[i] = []
            paths[i].append((j, len(path)))
print("Part 1:", eval(30))
print("Part 2:", eval(26))

