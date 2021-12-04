s = open('input.txt').read().splitlines()

def toggle(i):
    if i >= len(s): return
    c = s[i].split(' ')
    map = {'dec':'inc','inc':'dec','tgl':'inc','jnz':'cpy','cpy':'jnz'}
    s[i] = s[i].replace(c[0], map[c[0]])
    return

def get_value(arg):
    if arg in r:
        v = r[arg]
    else:
        v = int(arg)
    return v

def eval(r):
    out = []
    i = 0
    while True:
        #print(i, s[i], r)
        c = s[i].split(' ')
        if c[0] == 'cpy':
            if c[2] in r:
                r[c[2]] = get_value(c[1])
        elif c[0] == 'inc':
            r[c[1]] = r[c[1]] + 1
        elif c[0] == 'dec':
            r[c[1]] = r[c[1]] - 1
        elif c[0] == 'jnz':
            if get_value(c[1]) != 0:
                i += get_value(c[2]) - 1
        elif c[0] == 'tgl':
            v = i + get_value(c[1])
            if v < len(s):
                toggle(v)
        elif c[0] == 'out':
            v = get_value(c[1])
            out.append(v)
            if len(out) > 9:
                return out
        i += 1
        if i >= (len(s)): break

r = {'a':7,'b':0,'c':0,'d':0}
t = [0,1,0,1,0,1,0,1,0,1]
for i in range(10000):
    r['a'] = i
    k = eval(r)
    if k == t:
        print("Part 1:", i)
        break
