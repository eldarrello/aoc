d = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]
tiles = {}
for i in open('input.txt').read().splitlines():
    p = 0, 0
    for j in i.replace('se','a').replace('sw','b').replace('nw','c').replace('ne','d'):
        ind = ['e','a','b','w','c','d'].index(j)
        p = p[0] + d[ind][0], p[1] + d[ind][1]
    tiles[p] = 1 if p not in tiles else tiles[p] + 1
print("Part 1:", sum(i % 2 for i in tiles.values()))
def get_n(col, row):
   return [(col + i[0], row + i[1]) for i in d ]
for _ in range(100):
    to_flip = set()
    for k, v in tiles.items():
        b = 0
        for i in get_n(k[0], k[1]):
            if i not in tiles:
                if sum(t in tiles and tiles[t] % 2 for t in get_n(i[0],i[1])) == 2:
                    to_flip.add(i)
            elif tiles[i] % 2:
                b += 1
        if v % 2 and (b == 0 or b > 2) or not v % 2 and b == 2:
            to_flip.add(k)
    for i in to_flip:
        tiles[i] = 1 if i not in tiles else tiles[i] + 1
print("Part 2:", sum(i % 2 for i in tiles.values()))