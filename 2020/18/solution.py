ss = open('input.txt').read().splitlines()
ss = ['((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2']
#ss = ['2 + (4 * 9)']
def eval(i):
    op = None
    while i < len(s):
        k = s[i]
        i += 1
        if k == '(':
            k, i = eval(i)
        if k == ')':
            return r, i
        elif k in ['+', '*']:
            op = k
        else:
            print(k)
            k = int(k)
            if op:
                if op == '+':
                    r += k
                else:
                    r *= k
            else:
                r = k
    return r, i
acc = 0
for s in ss:
    s = s.replace(' ', '')
    acc += eval(0)[0]
print("Part 1:", acc)
print("Part 2:", 'todo') #was done by using external code:
