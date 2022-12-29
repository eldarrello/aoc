def get_path_to_closest_target(p, v):
    nodes = [[p]]
    best_path = []
    visited = set()
    while nodes and not best_path:
        next_nodes = []
        for path in nodes:
            x, y = path[-1]
            for dx, dy in dirs:
                np = x + dx, y + dy
                if np not in visited and np in m:
                    if m[np][0] == {'G': 'E', 'E': 'G'}[v]:
                        if not best_path:
                            best_path = path
                        elif path[-1][1] < best_path[-1][1] or (path[-1][1] == best_path[-1][1] and path[-1][0] < best_path[-1][0]):
                            best_path = path
                    elif m[np][0] == '.':
                        visited.add(np)
                        next_nodes.append(path + [np])
        nodes = next_nodes
    return best_path[1:]
s = open('input.txt').read().splitlines()
w = len(s[0])
h = len(s)
dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
damage_points = {'G': 3, 'E': 3}
m = {}
def attack(p, v):
    target = None
    for dx, dy in dirs:
        tp = p[0] + dx, p[1] + dy
        if tp in m and m[tp][0] == {'G': 'E', 'E': 'G'}[v]:
            if target:
                if m[tp][1] < m[target][1]:
                    target = tp
            else:
                target = tp
    if target:
        hit_points = m[target][1]
        if hit_points > damage_points[v]:
            m[target] = (m[target][0], hit_points - damage_points[v])
        else:
            m[target] = '.'
def round():
    pvs = list(m.items())
    for p, item in pvs:
        v = item[0]
        if v in 'GE' and m[p][0] in 'GE':
            path = get_path_to_closest_target(p, v)
            if path:
                m[path[0]], m[p] = m[p], ('.', 200)
                attack(path[0], v)
            else:
                target_count = len([1 for k, w in m.items() if w[0] == {'G': 'E', 'E': 'G'}[v]])
                if target_count == 0:
                    return True
                attack(p, v)
    return False
def eval(part):
    for y in range(h):
        for x in range(w):
            if s[y][x] != '#':
                m[(x, y)] = (s[y][x], 200)
    initial_e_count = len([1 for k, w in m.items() if w[0] == 'E'])
    for r in range(50000):
        ended = round()
        e_count = len([1 for k, w in m.items() if w[0] == 'E'])
        if part == 2 and e_count < initial_e_count:
            return 0
        hits = [v[1] for k, v in m.items() if v[0] in 'GE']
        if ended:
            break
    return r * sum(hits)
print("Part 1:", eval(1))
for i in range(4, 500):
    damage_points['E'] = i
    result = eval(2)
    if result:
        break
print("Part 2:", result)
