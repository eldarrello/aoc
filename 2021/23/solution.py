def get_moves(m, yx):
    ms = []
    y, x = yx
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = (x + dx), (y + dy)
        if (ny, nx) in m and m[(ny, nx)] not in [' ', '#']:
            ms.append((ny, nx))
    return ms

def get_moves_with_path(m, yx):
    moves = []
    nodes = [(yx, [yx])]
    while nodes:
        move, path = nodes.pop(0)
        next_moves = get_moves(m, move)
        for i in next_moves:
            if i not in path:
                nodes.append((i, path + [i]))
                if i not in [(1, 3), (1, 5), (1, 7), (1, 9)]:
                    if yx[0] != 1 or i[0] != 1:
                        moves.append((i, path))
    return moves

def get_all_moves(m):
    ms = {}
    for yx, v in m.items():
        if v in [' ', '#']:
            continue
        ms[yx] = get_moves_with_path(m, yx)
    return ms

def get_valid_moves(ms, ps):
    vm = []
    for yx, v in ps.items():
        moves = ms[yx]
        for m, path in moves:
            if m in ps.keys():
                continue
            for i in path[1:]:
                if i in ps:
                    break
            else:
                y, x = m
                if y > 1:
                    if x != dest_x[v]:
                        continue
                    if (y - 1) != list(ps.values()).count(v):   #check if bottom is settled
                        continue
                    if (y + 1, x) in ps:                        #any wrong ones still in?
                        continue
                    return [(yx, (y, x), len(path) * w[v])]     #take only the settling move as it is the best
                vm.append((yx, (y, x), len(path) * w[v]))
    return vm

def eval(file):
    s = open(file).read().splitlines()
    m = {(y, x): s[y][x] for y in range(len(s)) for x in range(len(s[y]))}
    ms = get_all_moves(m)
    n = list(m.values()).count('A')
    ps = {}
    for yx, v in m.items():
        if v in 'ABCD':
            if yx[1] == dest_x[v]:
                for y in range(yx[0] + 1, n + 2):
                    if m[(y, yx[1])] != v:
                        break
                else:
                    continue
            ps[yx] = v
    nodes = []
    vm = get_valid_moves(ms, ps)
    seen = set()
    c = 0
    for s, d, score in vm:
        pss = ps.copy()
        pss[d] = pss[s]
        del pss[s]
        heapq.heappush(nodes, (score, c, pss))
        c += 1
    while nodes:
            score, _, ps = heapq.heappop(nodes)
            if len(ps) == 0:
                return score
            vm = get_valid_moves(ms, ps)
            for next_s, next_d, next_score in vm:
                next_ps = ps.copy()
                if next_d[0] == 1:
                    next_ps[next_d] = next_ps[next_s]
                del next_ps[next_s]
                if tuple(next_ps.items()) not in seen or not next_ps.items():
                    seen.add(tuple(next_ps.items()))
                    heapq.heappush(nodes, (score + next_score, c, next_ps))
                    c += 1
import heapq
#import time
w = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
dest_x = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
#start = time.perf_counter()
print("Part 1:", eval('input_1.txt'))
print("Part 2:", eval('input_2.txt'))
#print(time.perf_counter() - start)              #todo::too slow (~80sec), One optimisation idea is to detect moves, which block solving. Also it seems that emptying a pocket moves need to come in a row!