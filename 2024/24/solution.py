a, b = open('input.txt').read().split('\n\n')
w = {i.split(': ')[0]: int(i.split(': ')[1]) for i in a.splitlines()}
gs = [i.replace(' ->', '').split() for i in b.splitlines()]
q = {c: (a, op, b) for a, op, b, c in gs}
bads = []
if q['z00'] not in [('x00', 'XOR', 'y00'), ('y00', 'XOR', 'x00')]:
    bads.append('z00')
for i in range(1, 45):
    z = f'z{i:02}'
    a, op, b = q[z]
    if op != 'XOR':
        bads.append(z)
    elif q[a][1] not in ['XOR', 'OR'] and i > 1:
        bads.append(a)
    elif q[b][1] not in ['XOR', 'OR'] and i > 1:
        bads.append(b)
    elif q[a][1] == 'XOR' and q[b][1] == 'XOR':
        if q[a][0] not in [f'x{i:02}', f'y{i:02}']:
            bads.append(a)
        if q[b][0] not in [f'x{i:02}', f'y{i:02}']:
            bads.append(b)
for a, op, b, c in gs:
    if op == 'OR':
        if q[a][1] != 'AND':
            bads.append(a)
        if q[b][1] != 'AND':
            bads.append(b)
while gs:
    done = []
    for i, (a, op, b, c) in enumerate(gs):
        if a in w and b in w:
            a = w[a]
            b = w[b]
            if op == 'AND':
                w[c] = a & b
            elif op == 'OR':
                w[c] = a | b
            elif op == 'XOR':
                w[c] = a ^ b
            done.append(gs[i])
    for i in done:
        gs.remove(i)
zs = []
for i in w.keys():
    if i[0] == 'z':
        zs.append(i)
zs.sort(reverse=True)
out = []
for i in zs:
    out.append(str(w[i]))
ss = ''.join(out)
print("Part 1:", int(ss, 2))
print("Part 2:", ','.join(sorted(bads)))

