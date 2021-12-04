s = open('input.txt').read().splitlines()
m = {'N':(-1,0), 'E':(0,1), 'S':(1,0), 'W':(0,-1)}

def run(part, dx, dy):
    x = 0
    y = 0
    for i in s:
        c = i[:1]
        v = int(i[1:])
        if c == 'F':
            x += dx * v
            y += dy * v
        elif c in m:
            if part == 1:
                y += m[c][0] * v
                x += m[c][1] * v
            else:
                dy += m[c][0] * v
                dx += m[c][1] * v
        else:
            if c == 'L':
                v = 360 - v
            for j in range(v // 90):
                dy, dx = dx, -dy
    print("Part {}:".format(part), abs(x) + abs(y))
run(1, 1, 0)
run(2, 10, -1)