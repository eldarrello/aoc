def eval(n, key):
    v = [int(i) * key for i in open('input.txt').read().splitlines()]
    k = [i for i in range(len(v))]
    for j in range(n):
        for i in range(len(v)):
            si = k.index(i)
            k.insert((si + v[i]) % (len(k) - 1), k.pop(si))
    vv = [v[i] for i in k]
    return sum([vv[(vv.index(0) + i) % len(v)] for i in [1000, 2000, 3000]])
print("Part 1:", eval(1, 1))
print("Part 2:", eval(10, 811589153))