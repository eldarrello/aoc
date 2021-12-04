import hashlib

def get_moves(xy, path):
    open = 'bcdef'
    d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    l = ['U','D','L','R']
    result = hashlib.md5(('vwbaicqe' + path).encode())
    hash = str(result.hexdigest())
    moves = []
    for i in range(len(d)):
        if hash[i] not in open: continue
        m = (xy[0] + d[i][0], xy[1] + d[i][1])
        if m[0] < 0 or m[1] < 0: continue
        if m[0] > 3 or m[1] > 3: continue
        moves.append((m, path + l[i]))
    return moves

part1 = None
part2 = 0
moves = get_moves((0, 0), "")
while moves:
    next_moves = []
    while moves:
        move = moves.pop()
        if move[0] == (3, 3):
            if not part1:
                part1 = move[1]
            if len(move[1]) > part2:
                part2 = len(move[1])
            continue
        next_moves += get_moves(move[0], move[1])
    moves = next_moves
print("Part 1:", part1)
print("Part 2:", part2)

