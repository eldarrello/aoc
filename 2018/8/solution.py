s = open('input.txt').read().split()
def parse(part, i):
    acc = 0
    n = int(s[i])
    m = int(s[i + 1])
    i += 2
    ts = []
    for k in range(n):
        i, t = parse(part, i)
        ts.append(t)
    for k in range(m):
        v = int(s[i + k])
        if part == 1:
            acc += v
        else:
            if v - 1 < len(ts):
                acc += ts[v - 1]
            elif not ts:
                acc += v
    if part == 1:
        acc += sum(ts)
    return i + m, acc
print("Part 1:", parse(1, 0)[1])
print("Part 2:", parse(2, 0)[1])
