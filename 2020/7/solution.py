s = open('input.txt').read().splitlines()
m = {}
for i in s:
    a, b = i.split(' bags contain ')
    bags = b.split(', ')
    m[a] = []
    for bag in bags:
        ws = bag.split(' ')
        if len(ws) < 4:
            continue
        m[a].append((int(ws[0]), ws[1] + ' ' + ws[2]))

def count_nodes(node):
    nodes = [node]
    count = 0
    has_gold = 0
    while nodes:
        n, id = nodes.pop(0)
        if id == 'shiny gold':
            has_gold |= 1
        count += n
        nodes += [(n * n_leaf, id_leaf) for n_leaf, id_leaf in m[id]]
    return has_gold, count

print("Part 1:", sum(count_nodes((1, k))[0] for k, v in m.items()) - 1)
print("Part 2:", count_nodes((1, 'shiny gold'))[1] - 1)
