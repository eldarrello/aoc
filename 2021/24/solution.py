def eval(z, d, v):
    x = z % 26 + v[1]
    z //= v[0]
    if x != d:
        z *= 26
        z += d + v[2]
    return z
s = list(map(lambda x: x.splitlines(), open('input.txt').read().split('inp w\n')))
s.pop(0)
states = {}
good = {0}
for i in range(13, -1, -1):
    coef = [int(s[i][k].split(' ')[2]) for k in [3, 4, 14]]
    next_good = set()
    states[i] = []
    digits = set()
    for k in range(9, 0, -1):
        for n in range(400000):             #400000 - was enough for the input to complete in 20sec, todo:: smarter logic to determine the range based on coef or implement reverse of eval()
            z = eval(n, k + 1, coef)
            if z in good:
                next_good.add(n)
                states[i].append((k, z, n))
    good = next_good
nodes = [(states[0][0][1], 1, str(states[0][0][0]))]
codes = []
while nodes:
    z, n, d = nodes.pop()
    dd = states[n]
    for i in dd:
        if i[2] == z:
            if n == 13:
                codes.append(d + str(i[0]))
            else:
                nodes.append((i[1], n + 1, d + str(i[0])))
results = list(map(int, codes))
print("Part 1:", max(codes))
print("Part 2:", min(codes))
