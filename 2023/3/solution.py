m = {}
for y, l in enumerate(open('input.txt').read().splitlines()):
  for x, c in enumerate('.' + l + '.'):
    m[(x, y)] = c
acc1 = 0
stars = {}
num = []
q = 0

for (x, y), c in m.items():
  if c.isdigit():
    num.append(c)
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
      if (x + dx, y + dy) in m:
        c = m[(x + dx, y + dy)]
        if c not in '1234567890.':
          q = (x + dx, y + dy, c)
  elif len(num):
    v = int(''.join(num))
    if (q):
      acc1 += v
      if q[2] == '*':
        x, y, _ = q
        if (x, y) not in stars:
          stars[(x, y)] = []
        stars[(x, y)].append(v)
    q = 0
    num = []

print("Part 1:", acc1)
acc2 = 0
for x in stars.values():
  if len(x) == 2:
    acc2 += x[0] * x[1]
print("Part 2:", acc2)
