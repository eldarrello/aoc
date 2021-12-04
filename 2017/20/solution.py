s = open('input.txt').read().splitlines()
def get(w):
    return [int(x) for x in w[3:-1].split(',')]
def add(l1, l2):
    return [x + y for x, y in zip(l1, l2)]
ps = []
for i in s:
    ps.append([get(x) for x in i.split(', ')])

min_i = 0
while True:
    min_d = 10000000
    k = 0
    for i, p in enumerate(ps):
        p[1] = add(p[1], p[2])
        p[0] = add(p[0], p[1])
        d = abs(p[0][0]) + abs(p[0][1]) + abs(p[0][2])
        if d < min_d:
            min_d = d
            k += 1
            min_i = i
    if k == 1:
        break
print("Part 1:", min_i)

ps = []
for i in s:
    ps.append([get(x) for x in i.split(', ')])
t = 0
while True:
    hashes = {}
    for i, p in enumerate(ps):
        p[1] = add(p[1], p[2])
        p[0] = add(p[0], p[1])

        hash = str(p[0][0]) +','+ str(p[0][1]) + ',' + str(p[0][2])
        if hash in hashes:
            hashes[hash].append(p)
        else:
            hashes[hash] = [p]
    for _, v in hashes.items():
        if len(v) > 1:
            for p in v:
                ps.remove(p)
    t += 1
    if t > 1000:
        break
print("Part 2:", len(ps))
