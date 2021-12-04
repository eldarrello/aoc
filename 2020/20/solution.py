def get(p):
    return sum([[p:=list(zip(*p[::-1])), [i[::-1] for i in p]] for i in range(4)], [])
def column(p, i):
    return [row[i] for row in p]
ts = {int(i[0].split()[1].strip(':')):get(i[1:]) for i in [i.splitlines() for i in open('input.txt').read().split('\n\n')]}
edge_to_ids = {}
for k, v in ts.items():
    for edge in [i[0] for i in v]:
        if edge in edge_to_ids:
            edge_to_ids[edge].append(k)
        else:
            edge_to_ids[edge] = [k]
acc = 1
for k, v in ts.items():
    for t in v:
        if len(edge_to_ids[tuple(column(t, 0))]) < 2 and len(edge_to_ids[t[0]]) < 2:
            acc *= k
            corner = (k, t)
            break
print("Part 1:", acc) # Alternative part 1: map[0, 0][0] * map[11, 11][0] * map[0, 11][0] * map[11, 0][0])
map = {(0, 0):corner}
nodes = [(0, 0)]
while len(map) < len(ts):       #Arrange tiles.
    x, y = nodes.pop()
    t = map[(x, y)][1]
    for i, d in enumerate([(-1, 0), (0, -1), (1, 0), (0, 1)]):
        p = (x + d[0], y + d[1])
        if p not in map:
            edge = [column(t, 0), t[0], column(t, 9), t[9]][i]
            for k in [i for i in edge_to_ids[tuple(edge)] if i != map[(x, y)][0]]:
                for tt in ts[k]:
                    if edge == [column(tt, 9), tt[9], column(tt, 0), tt[0]][i]:
                        map[p] = (k, tt)
                        nodes.append(p)
tile = []
for y in range(12):             #Merge tiles.
    cols = ['' for i in range(8)]
    for x in range(12):
        t = map[(x,y)][1]
        for i in range(1, 9):
            cols[i - 1] += ''.join(t[i][1:-1])
    tile += cols
p = ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
for tile in get(tile):          #Find monsters.
    acc = 0
    for y in range(96 - len(p)):
        for x in range(96 - len(p[0])):
            for dy in range(len(p)):
                for dx in range(len(p[0])):
                    if p[dy][dx] == '#' and tile[y + dy][x + dx] != '#':
                        break
                else:
                    continue
                break
            else:
                acc += 1
    if acc:
        print("Part 2:", sum(''.join(list(i)).count('#') for i in tile) - acc * 15)
