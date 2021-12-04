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
            if i == 7:                      # Hack for part 2 speedup
                r['a'] += r['c']
            elif i == 9:                    # Hack for part 2 speedup
                r['a'] += (r['b'] * r['d'])
            else:
                if get_value(c[1]) != 0:
                    i += get_value(c[2]) - 1
        elif c[0] == 'tgl':
            v = i + get_value(c[1])
            if v < len(s):
                toggle(v)
        i += 1
        if i >= (len(s)): break

r = {'a':7,'b':0,'c':0,'d':0}
eval(r)
print("Part 1:", r['a'])
s = open('input.txt').read().splitlines()
r = {'a':12,'b':0,'c':0,'d':0}
eval(r)
print("Part 2:", r['a']) #43961674 - too low