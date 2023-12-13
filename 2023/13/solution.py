def get(s, f):
    return [f * y for y in range(1, len(s)) if not sum([1 for i in range(min(y, len(s) - y)) if s[y + i] != s[y - 1 - i]])]

def get_p(s, exclude):
    ss = [[s[x][y] for x in range(len(s))] for y in range(len(s[0]))]
    ps = [i for i in get(s, 100) + get(ss, 1) if i != exclude]
    return ps[0] if ps else 0

fs = open('input.txt').read().split('\n\n')
acc = 0
acc2 = 0
for f in fs:
    s = [list(line) for line in f.splitlines()]
    po = get_p(s, 0)
    acc += po
    ps = set()
    for y in range(len(s)):
        for x in range(len(s[0])):
            s[y][x] = '.' if s[y][x] == '#' else '#'
            ps.add(get_p(s, po))
            s[y][x] = '.' if s[y][x] == '#' else '#'
    acc2 += max(list(ps))
print("Part 1:", acc)
print("Part 2:", acc2)
