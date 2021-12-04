s = open('input.txt').read().splitlines()
g = [int(i) for i in s[0].split(',')]
scores = []
totals = []
for i in range(1, len(s), 6):
    p = [int(x) for j in range(1, 6) for x in s[i + j].split(' ') if x != '']
    scores.append(min([min(max([g.index(p[x * 5 + y]) for x in range(5)]), max([g.index(p[y * 5 + x]) for x in range(5)])) for y in range(5)]))
    totals.append(sum([x for x in p if x not in g[:scores[-1] + 1]]))
print("Part 1:", totals[scores.index(min(scores))] * g[min(scores)])
print("Part 2:", totals[scores.index(max(scores))] * g[max(scores)])

