import math

z = (0, 0, 0)

with open("input.txt") as f:
    p = f.read().splitlines()
for i in range(len(p)):
    p[i] = p[i].replace('<','').replace('>', '').replace('x=', '').replace('y=', '').replace('z=', '').split(', ')
    p[i] = [int(a) for a in p[i]]

def add(p, v):
    for i in range(4):
        p[i] = (p[i][0] + v[i][0], p[i][1] + v[i][1], p[i][2] + v[i][2])
    return p

def get_gravity():
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    g = [z, z, z, z]
    for pair in range(len(pairs)):
        p1 = pairs[pair][0]
        p2 = pairs[pair][1]
        d1 = [0,0,0]
        d2 = [0,0,0]
        for c in range(3):
            if p[p1][c] > p[p2][c]:
                d1[c] = -1
                d2[c] = 1
            elif p[p1][c] < p[p2][c]:
                d1[c] = 1
                d2[c] = -1
        g[p1] = (g[p1][0] + d1[0], g[p1][1] + d1[1], g[p1][2] + d1[2])
        g[p2] = (g[p2][0] + d2[0], g[p2][1] + d2[1], g[p2][2] + d2[2])
    return g
      
def get_energy():
    e = 0
    for i in range(len(p)):
        pot = 0
        kin = 0
        for c in range(3):
            pot += abs(p[i][c])
            kin += abs(v[i][c])
        e += pot * kin
    return e 

v = [z,z,z,z]  
d = [{},{},{}]
cnt = 0
for i in range(10000000):
    if i == 1000:
        print('Total energy:', get_energy(), '@t =', i)    
    v = add(v, get_gravity())
    p = add(p, v)
    
    for k in range(len(d)):
        key = []
        for j in range(4):
            key.append(p[j][k])
            key.append(v[j][k])
        key = str(key)
        if key not in d[k]:   
            d[k][key] = i
            cnt += 1
    if i > cnt + 1:
        break
#print(i, cnt)
t = 1
for i in range(len(d)):
    t = int(t * len(d[i]) / math.gcd(t, len(d[i])))

print('Number of steps:', t)