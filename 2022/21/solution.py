def calc(node):
    return eval("calc('{}') {} calc('{}')".format(*q[node])) if type(q[node]) is tuple else q[node]
q = {k: tuple(v.split()) if ' ' in v else int(v) for k, v in [i.split(': ') for i in open('input.txt').read().splitlines()]}
print("Part 1:", int(calc('root')))
def calc2(node, e):
    if node == 'humn':
        return int(e)
    a, op, b = q[node]
    has_a = type(q[b]) is tuple
    if op == '+':
        c = e - q[a if has_a else b]
    elif op == '-':
        c = q[a] - e if has_a else e + q[b]
    elif op == '*':
        c = e / q[a if has_a else b]
    elif op == '/':
        c = q[a] / e if has_a else e * q[b]
    return calc2(b if has_a else a, c)
q['humn'] = float('nan')
q.update({i: v for i, v in {k: calc(k) for k in q.keys()}.items() if v == v})
del q['humn']
a, _, b = q['root']
print("Part 2:", calc2(b, q[a]) if type(q[b]) is tuple else calc2(a, q[b]))