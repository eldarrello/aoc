map = []
cols = 0
def p(y, x):
    return y * cols + x
    
def yx(p):
    return divmod(p, cols)
    
def distance(y, x):
    return x * x + y * y
    
def set(d, k, dy, dx):
    if k in d:
        if distance(dy, dx) >= distance(d[k][0], d[k][1]): return
    d[k] = [dy, dx]

def evaluate(y0, x0):
    d0 = {}
    d1 = {}
    d2 = {}
    d3 = {}
    for i in range(len(map)):
        if map[i] and i != p(y0, x0):
            [y1, x1] = yx(i)
            dx = x1 - x0
            dy = y1 - y0
                        
            if dx == 0:
                k = 9999999
            else:
                k = float(dy) / dx
            
            if dx == 0 and dy < 0:
                set(d0, -k, dy, dx)
            elif dx > 0 and dy < 0:    
                set(d0, k, dy, dx)
            elif dx > 0 and dy >= 0:
                set(d1, k, dy, dx)
            elif dy > 0:
                set(d2, k, dy, dx)
            else:
                set(d3, k, dy, dx)
                
    return [d0, d1, d2, d3]
        
with open("input.txt") as fp:
    for cols, line in enumerate(fp):    
        line = line.replace('.','0').replace('#','1').strip()
        line = line.replace('#','1')  
        [map.append(int(a)) for a in line]
cols += 1
print(cols)
max_n = 0
c = 0
station = 0
for i in range(len(map)):
    if map[i] != 1: continue
    [y, x] = yx(i)
    if (map[i]):
        c += 1
    [dy_pos, dy_neg, dx_pos, dx_neg] = evaluate(y, x)
    n = len(dy_pos) + len(dy_neg) + len(dx_pos) + len(dx_neg)
    if n > max_n:
        max_n = n
        station = i
print(max_n)
print(c)
[y, x] = yx(station)
print(y, x)
[d0, d1, d2, d3] = evaluate(y, x)
print(len(d0), len(d1), len(d2), len(d3))
#print(dy_pos)
d_s = sorted(d3)
n = len(d0) + len(d1) + len(d2)
for i in range(len(d_s)):
    if n + i + 1 == 200:
        print(d_s[i], d3[d_s[i]])
        f_y = y + d3[d_s[i]][0]
        f_x = x + d3[d_s[i]][1]
        print(f_y, f_x)


#y=29 x=26