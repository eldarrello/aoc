def run(rounds):
    ms = []
    for i in open('input.txt').read().split('\n\n'):
        ls = i.splitlines()
        ms.append(([int(i) for i in ls[1].split(': ')[1].split(', ')], ls[2].split(': ')[1], int(ls[3].split()[-1]),
                   int(ls[4].split()[-1]), int(ls[5].split()[-1])))
    mod = 1
    mod = [mod := mod * i[2] for i in ms][-1]
    c = [0 for i in ms]
    for r in range(rounds):
        for i in range(len(ms)):
            m = ms[i]
            c[i] += len(m[0])
            for old in m[0]:
                new = eval(m[1].split('= ')[1])
                new = int(new / 3) if rounds == 20 else new % mod
                ms[m[3 + min(new % m[2], 1)]][0].append(new)
            ms[i][0].clear()
    c.sort()
    return c[-1] * c[-2]
print("Part 1:", run(20))
print("Part 2:", run(10000))
