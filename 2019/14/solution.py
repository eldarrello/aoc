m = {}
   
for line in open("input.txt").readlines():
        cs = {}
        t = line.split(', ')
        for k in range(len(t) - 1):
            p = t[k].split(' ')
            cs[p[1]] = int(p[0])
        last = t[len(t) - 1].split(' => ')
        p = last[0].split(' ')
        cs[p[1]] = int(p[0])
        p = last[1].split(' ')
        m[p[1].strip()] = (int(p[0]), cs)

def depends(k, keys):
    for key in keys:
        if key not in m: continue
        leafs = m[key][1]
        if k in leafs:
            return True
        for leaf in leafs:
            if depends(k, leafs) == True:
                return True
    return False
    
def produce(c, n):
    cs = m[c][1].copy()
    for c in cs:
        cs[c] *= n
    while len(cs) > 1:
        for c in cs:
            if depends(c, cs): continue
            #print('reducing', c, cs[c], m[c][0])
            leafs = m[c][1]
            q = (cs[c] + m[c][0] - 1) // m[c][0]
            for leaf in leafs:
                if leaf in cs:
                    cs[leaf] += leafs[leaf] * q
                else:
                    cs[leaf] = leafs[leaf] * q
            del cs[c]
            #print(cs)
            break
    return cs
cs = produce('FUEL', 1)
print('ORE per 1 FUEL:', cs['ORE'])

min = 0
max = 1e9
while True:
    n = (min + max) / 2
    cs = produce('FUEL', n)
    #print(cs, min, max)
    d = cs['ORE'] - 1e12
    if (max - min) < 2:
        break
    if d > 0:
        max = n
    else:
        min = n
print('FUEL per 1e12 ORE:', n, cs['ORE'])