def shunting_yard(s, p):
    ops = []
    rpn = []
    for c in s:
        if c in '+*':
            while ops and ops[-1] != '(' and p[ops[-1]] >= p[c]:
                rpn.append(ops.pop())
            ops.append(c)
        elif c == '(':
            ops.append(c)
        elif c == ')':
            while ops[-1] != '(':
                rpn.append(ops.pop())
            ops.pop()
        else:
            rpn.append(int(c))
    while ops:
        rpn.append(ops.pop())
    while rpn:
        c = rpn.pop(0)
        if c == '*':
            ops.append(ops.pop() * ops.pop())
        elif c == '+':
            ops.append(ops.pop() + ops.pop())
        else:
            ops.append(c)
    return ops[0]
ss = open('input.txt').read().splitlines()
acc = 0
acc2 = 0
for s in ss:
    s = s.replace(' ', '')
    acc += shunting_yard(s, {'+': 0, '*': 0})
    acc2 += shunting_yard(s, {'+': 1, '*': 0})
print("Part 1:", acc)
print("Part 2:", acc2)
