import itertools
bs = [list(map(int,i.replace(' @', ',').split(', '))) for i in open('input.txt').read().splitlines()]
acc = 0
for (x, y, _, dx, dy, _), (x2, y2, _, dx2, dy2, _) in itertools.combinations(bs, 2):
    d = dy * dx2 - dx * dy2
    if d != 0:
        t2 = (dx * (y2 - y) - dy * (x2 - x)) / d
        t1 = ((y2 - y) + t2 * dy2) / dy
        min_v = 200000000000000
        max_v = 400000000000000
        if min_v <= x + t1 * dx <= max_v and min_v <= y + t1 * dy <= max_v and t1 >= 0 and t2 >= 0:
            acc += 1
print("Part 1:", acc)

import collections
Vec3 = collections.namedtuple("Vec3", "x,y,z", defaults = (0, 0, 0))

def cross(a, b):
    return Vec3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z

def sub(a, b):
    return Vec3(a.x - b.x, a.y - b.y, a.z - b.z)

def mul(a, b):
    return Vec3(a.x * b, a.y * b, a.z * b)

def add(a, b):
    return Vec3(a.x + b.x, a.y + b.y, a.z + b.z)

'''Make h0 as a base, find plane n using h1, find intersection points p2, p3 of h2 and h3 with the plane n.'''
a = bs[0]
h0 = Vec3(*a[:3])
b = list(map(int.__sub__, bs[1], a))
v1 = Vec3(*b[3:])
h1 = Vec3(*b[:3])
c = list(map(int.__sub__, bs[2], a))
v2 = Vec3(*c[3:])
h2 = Vec3(*c[:3])
d = list(map(int.__sub__, bs[3], a))
v3 = Vec3(*d[3:])
h3 = Vec3(*d[:3])

n = cross(h1, add(h1, v1))

t2 = dot(h2, n) / -dot(v2, n)
p2 = add(h2, mul(v2, t2))

t3 = dot(h3, n) / -dot(v3, n)
p3 = add(h3, mul(v3, t3))

r = add(add(p2, mul(sub(p2, p3), t2 / (t3 - t2))), h0)

print("Part 2:", int(r.x + r.y + r.z))
