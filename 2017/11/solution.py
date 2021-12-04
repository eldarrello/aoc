s = open('input.txt').read()
s = s.split(',')
map = {'n':(0,-2),'s':(0,2),'nw':(-1,-1),'ne':(1,-1),'sw':(-1,1),'se':(1,1)}
def get_doubleheight_distance(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return dx + max(0, (dy - dx) / 2)
col = 0
row = 0
max_d = 0
for i in s:
    p = map[i]
    col += p[0]
    row += p[1]
    d = int(get_doubleheight_distance((col,row), (0,0)))
    if d > max_d:
        max_d = d
print("Part 1:", d)
print("Part 2:", max_d)
