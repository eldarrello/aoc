def eval(n):
    acc = 0
    for l in s:
        vs = [-1] * (n + 1)
        for k in range(1, n + 1):
            vs[k] = vs[k - 1] + 1
            for i in range(vs[k], len(l) - n + k):
                if l[i] > l[vs[k]]:
                    vs[k] = i
        acc += int(''.join([l[vs[k + 1]] for k in range(n)]))
    return acc
s = open('input.txt').read().splitlines()
print("Part 1:", eval(2))
print("Part 2:", eval(12))

