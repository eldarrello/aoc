import copy

s = open('input.txt').read().splitlines()
values_map = {}
parents = {}
childs = {}
for i in s:
    ws = i.split(' ')
    parent = ws[0]
    if '->' in ws:
        leafs = i.split(' -> ')[1].split(', ')
        childs[parent] = leafs
        for leaf in leafs:
            parents[leaf] = parent
    values_map[parent] = int(ws[1][1:-1])
for key, value in values_map.items():
    if key not in parents:
        root = key
        print("Part 1:", key)

values_map_ori = copy.deepcopy(values_map)
while len(childs):
    deleted = []
    for key, child_list in childs.items():
        values = []
        tags = []
        for child in child_list:
            if child not in childs:
                values.append(values_map[child])
                tags.append(child)
        if len(values) == len(child_list):
            if values.count(values[0]) == len(values):
                values_map[key] += len(values) * values[0]
            else:
                counts = {}
                target = None
                for i in values:
                    if i not in counts:
                        counts[i] = 1
                    else:
                        target = i
                        counts[i] += 1
                for key, i in counts.items():
                    if i == 1:
                        tag = tags[values.index(key)]
                        dif = target - key
                        print("Part 2:", values_map_ori[tag] + dif)
                deleted.clear()
                childs.clear()
                break
            deleted.append(key)
    for i in deleted:
        del childs[i]
