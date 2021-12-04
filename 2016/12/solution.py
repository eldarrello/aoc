s = open('input.txt').read().splitlines()

def eval(r):
    i = 0
    while True:
        c = s[i].split(' ')
        if c[0] == 'cpy':
            if c[1] in r:
                v = r[c[1]]
            else:
                v = int(c[1])
            r[c[2]] = v
        elif c[0] == 'inc':
            r[c[1]] = r[c[1]] + 1
        elif c[0] == 'dec':
            r[c[1]] = r[c[1]] - 1
        elif c[0] == 'jnz':
            if c[1] in r:
                v = r[c[1]]
            else:
                v = int(c[1])
            if v != 0:
                i += int(c[2]) - 1
        i += 1
        if i >= (len(s)): break

r = {'a':0,'b':0,'c':0,'d':0}
eval(r)
print("Part 1:", r['a'])
r = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
eval(r)
print("Part 2:", r['a'])