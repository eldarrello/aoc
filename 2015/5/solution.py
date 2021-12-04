s = open('input.txt').read().splitlines()
nice = 0
for i in s:
    v = "aeiou"
    bad = ["ab", "cd", "pq", "xy"]
    t = 0
    q = False
    z = True
    prev = '?'
    for k in i:
        if k in v:
            t += 1
        if k == prev:
            q = True
        if prev + k in bad:
            z = False
            break
        prev = k
    if t >= 3 and q == True and z == True:
        nice += 1
    else:
        g = 0
print('Part 1:', nice)
nice = 0
for i in s:
    pair = False
    sym = False
    prev = '?'
    pprev = '?'
    for k in range(len(i)):
        v = i[k]
        if i[k:].find(prev + v) > 0:
            pair = True
        if pprev == v:
            sym = True
        pprev = prev
        prev = v
    if pair == True and sym == True:
        nice += 1
    else:
        g = 0
print('Part 2:', nice)