def eval(n):
    s = open('input.txt').read().split()
    s = {i: s.count(i) for i in s}
    for i in range(n):
        ns = {}
        for k, v in s.items():
            if k == '0':
                ns['1'] = v if '1' not in ns else ns['1'] + v
            elif len(k) % 2 == 0:
                a = str(int(k[:len(k) // 2]))
                b = str(int(k[len(k) // 2:]))
                ns[a] = v if a not in ns else ns[a] + v
                ns[b] = v if b not in ns else ns[b] + v
            else:
                ns[str(int(k) * 2024)] = v
        s = ns
    return sum([v for k, v in s.items()])
print("Part 1:", eval(25))
print("Part 2:", eval(75))

