s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s))}
end_y = len(s) - 1

max_p = 0
nodes = [((1, 0), [(1, 0)])]
while nodes:
    (x, y), path = nodes.pop(0)
    if y == len(s) - 1:
        if len(path) > max_p:
            max_p = len(path)
    moves = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    if m[(x, y)] in 'v^><':
        moves = [moves['v^><'.index(m[(x, y)])]]
        if m[moves[0]] == '#':
            moves = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    for xy in moves:
        if xy in m and m[(xy[0], xy[1])] != '#' and xy not in path:
            nodes.append((xy, path + [xy]))
print("Part 1:", max_p - 1)

def run():
    keys = {(1, 0):[]}
    dist = {}
    nodes = [((1, 0), [(1, 0)])]
    while nodes:
        (x, y), path = nodes.pop()
        moves = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        '''
        if m[(x, y)] in 'v^><':
            moves = [moves['v^><'.index(m[(x, y)])]]
            if m[moves[0]] == '#':
                moves = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        '''
        cnt = 0
        for i, xy in enumerate(moves):
            if xy in m and m[(xy[0], xy[1])] != '#' and xy not in path:
                if xy in keys:
                    d = 1
                    for last_node in reversed(path):
                        if last_node in keys:
                            break
                        d += 1
                    #last_node = list(keys.keys())[-1]
                    keys[last_node].append(xy)
                    keys[xy].append(last_node)
                    #d = len(path) - path.index(last_node)
                    dist[((xy), last_node)] = d
                    dist[(last_node, (xy))] = d
                    continue
                nodes.append((xy, path + [xy]))
                cnt += 1
        if cnt > 1 or y == end_y:
            d = 0
            for last_node in reversed(path):
                if last_node in keys:
                    break
                d += 1
            dist[((x, y), last_node)] = d
            dist[(last_node, (x, y))] = d
            keys[last_node].append((x, y))
            keys[(x, y)] = [last_node]

    max_d = 0
    nodes = [((1, 0), [(1, 0)], 0)]
    while nodes:
        xy, path, d = nodes.pop()
        for key in keys[xy]:
            nd = d + dist[(xy, key)]
            if key not in path:
                if key[1] == end_y:
                    if nd > max_d:
                        max_d = nd
                    continue
                nodes.append((key, path + [key], nd))
    return max_d
#print("Part 1:", run())
#m = {xy: c if c in '.#' else '.' for xy, c in m.items()}
print("Part 2:", run())
#todo::optimize and merge part1 and part2