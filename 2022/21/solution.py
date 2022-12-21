def calc2(node, e):
    if node == 'humn':
        return int(e)
    a, op, b = q[node]
    if op == '+':
        c = e - v[a if a in v else b]
    elif op == '-':
        c = v[a] - e if a in v else e + v[b]
    elif op == '*':
        c = e / v[a if a in v else b]
    elif op == '/':
        c = v[a] / e if a in v else e * v[b]
    return calc2(b if a in v else a, c)

def calc(node):
    global depends
    if node in v:
        if node == 'humn':
            depends += 1
        return v[node]
    return eval("calc('{}') {} calc('{}')".format(*q[node]))
q = {}
v = {}
for i in open('input.txt').read().splitlines():
    d, s = i.split(': ')
    ss = s.split()
    if len(ss) == 1:
        v[d] = int(ss[0])
    else:
        q[d] = tuple(ss)
depends = 0
print("Part 1:", int(calc('root')))

for k, _ in q.items():
    depends = 0
    value = calc(k)
    if depends == 0:
        v[k] = value
del v['humn']
print("Part 2:", calc2('pqpw', calc('vqmv')))