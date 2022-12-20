def eval(n, key):
    v = [int(i) * key for i in open('input.txt').read().splitlines()]
    k = [i for i in range(len(v))]
    for j in range(n):
        for i in range(len(v)):
            si = k.index(i)
            q = k.pop(si)
            di = (si + v[i]) % len(k)
            if di < 0:
                di -= 1
            k.insert(di, q)
    vv = [v[i] for i in k]
    return sum([vv[(vv.index(0) + i) % len(v)] for i in [1000, 2000, 3000]])
print("Part 1:", eval(1, 1))
print("Part 2:", eval(10, 811589153))