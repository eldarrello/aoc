map = {}
done_moves = set()
for y in range(40):
    row = []
    for x in range(40):
        v = x*x + 3*x + 2*x*y + y + y*y + 1362
        map[(y, x)] = 'X' if bin(v).count("1") % 2 == 1 else '.'

def get_moves(y, x):
    try_moves = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    moves = []
    for i in try_moves:
        if i in map and map[i] == '.' and i not in done_moves:
            moves.append(i)
            done_moves.add(i)
    return moves

p = (1, 1)
moves = get_moves(p[0], p[1])
level = 1
while moves:
    next_moves = []
    while moves:
        p = moves.pop()
        if p == (39, 31):
            print("Part 1:", level)
        next_moves += get_moves(p[0], p[1])
    moves = next_moves
    level += 1
    if level == 50:
        print("Part 2:", len(done_moves))



