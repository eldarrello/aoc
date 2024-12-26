a, b = open('input.txt').read().split('\n\n')
w = {i.split(': ')[0]: int(i.split(': ')[1]) for i in a.splitlines()}
gs = [i.replace(' ->', '').split() for i in b.splitlines()]
q = {c: (a, op, b) for a, op, b, c in gs}
qq = {a: op for a, op, b, c in gs} | {b: op for a, op, b, c in gs}
bad = set()
while len(w) < 312:
    for i, (a, op, b, c) in enumerate(gs):
        if a in w and b in w:
            av = w[a]
            bv = w[b]
            if op == 'AND':
                if c not in qq or qq[c] != 'OR' and '00' not in a + b:
                    bad.add(c)
                w[c] = av & bv
            elif op == 'OR':
                if c not in qq and c != 'z45':  # last bit comes from OR
                    bad.add(c)
                w[c] = av | bv
            elif op == 'XOR':
                if c in qq and qq[c] == 'OR':
                    bad.add(c)
                if a in q and b in q and q[a][1] == 'XOR' and q[b][1] == 'XOR':
                    if q[a][0] in q:
                        bad.add(a)
                    if q[b][0] in q:
                        bad.add(b)
                w[c] = av ^ bv
print("Part 1:", sum([2 << (i - 1) for i in range(0, 46) if w[f'z{i:02}']]))
print("Part 2:", ','.join(sorted(bad)))



