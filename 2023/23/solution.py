s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s)) if s[y][x] != '#'}
end_y = len(s) - 1
max_p = 0
nodes = [((1, 0), {(1, 0)}, (1, 0))]
keys = {(1, 0): []}
dist = {}
while nodes:
    (x, y), path, last = nodes.pop()            # full path isn't really needed, just previous tile
    for i in range(1 if len(dist) else 0, end_y * end_y):
        moves = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        if m[(x, y)] != '.':
            moves = [moves['v^><'.index(m[(x, y)])]]
        valid_moves = [xy for xy in moves if xy in m and xy not in path]
        if len(valid_moves) > 1 or y == end_y:
            if len(path) > max_p:
                max_p = len(path)
            keys[(x, y)] = [last]
            keys[last].append((x, y))
            dist[(last, (x, y))] = i
            dist[((x, y), last)] = i
            for xy in valid_moves:
                nodes.append((xy, path | {xy}, (x, y)))
            break
        if valid_moves:
            (x, y) = valid_moves[0]
            if (x, y) in keys:
                keys[last].append((x, y))
                keys[(x, y)].append(last)
                dist[((x, y), last)] = i + 1
                dist[(last, (x, y))] = i + 1
                break                           # comment out for example input
            path |= {(x, y)}
        else:
            break
print("Part 1:", max_p - 1)

for key, item in keys.items():
    item.sort(key=lambda x: dist[(key, x)])     # With DFS longest dists are evaluated first, which enables to use bailout counter
max_p = 0
nodes = [((1, 0), {(1, 0)}, 0)]
c = 0
while nodes and c < 10000:
    xy, path, d = nodes.pop()
    for key in keys[xy]:
        nd = d + dist[(xy, key)]
        if key not in path:
            if key[1] == end_y:
                c += 1
                if nd > max_p:
                    max_p = nd
                continue
            nodes.append((key, path | {key}, nd))
print("Part 2:", max_p)
'''
Insight for pruning optimisation: junctions form 3x3 grid in example and 6x6 grid in full input.
So junctions with 3 choices are from the borders of the grid and in the middle, all junctions have 4 choices.
When you reach the border then only valid choice is towards exit, other choice is dead end.
'''
