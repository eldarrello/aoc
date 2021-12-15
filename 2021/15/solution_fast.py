import heapq
def dijkstra(n):
    s = open('input.txt').read().splitlines()
    map = {(y, x): (int(s[y % 100][x % 100]) + y // 100 + x // 100 - 1) % 9 + 1 for y in range(n) for x in range(n)}
    s = {yx: (yx[0] + yx[1]) * 9 for yx in map.keys()}
    nodes = [(0, (0, 0))]
    while len(nodes):
        score, yx = heapq.heappop(nodes)
        for move, s[move] in [(move, score + map[move]) for move in [(yx[0] + m[0], yx[1] + m[1]) for m in [(0, 1), (1, 0), (-1, 0), (0, -1)]] if move in map and score + map[move] < s[move]]:
            heapq.heappush(nodes, (s[move], move))
    return s[(n - 1, n - 1)]
print("Part 1", dijkstra(100))
print("Part 2", dijkstra(500))