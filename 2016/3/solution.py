s = open('input.txt').read().splitlines()

def is_triangle(sides):
    return not (sides[0] >= sides[1] + sides[2] or sides[1] >= sides[0] + sides[2] or sides[2] >= sides[0] + sides[1])

triangles = 0
c0 = []
c1 = []
c2 = []
for i in s:
    sides = list(map(int, i.split()))
    c0.append(sides[0])
    c1.append(sides[1])
    c2.append(sides[2])
    if is_triangle(sides):
        triangles += 1
print('Part 1:', triangles)
c = c0 + c1 + c2
triangles = 0
for i in range(0, len(c), 3):
    sides = c[i:i + 3]
    if is_triangle(sides):
        triangles += 1
print('Part 2:', triangles)
