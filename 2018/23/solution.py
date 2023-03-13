s = open('input.txt').read().splitlines()
max_r = 0
ps = []
for i in s:
    p, r = i.replace('r=', '').replace('pos=<', '').split('>, ')
    x, y, z = map(int, p. split(','))
    r = int(r)
    if r > max_r:
        max_r = r
        base = (x, y, z)
    ps.append(((x, y, z), r))
c = 0
for p, r in ps:
    d = abs(p[0] - base[0]) + abs(p[1] - base[1]) + abs(p[2] - base[2])
    if d <= max_r:
        c += 1
print("Part 1:", c)
q = []
for p, r in ps:
  d = abs(p[0]) + abs(p[1]) + abs(p[2])
  q.append((max(0, d - r), 1))              # the range starts
  q.append((d + r + 1, -1))                 # the range ends
q = sorted(q, key=lambda x: x[0])
in_range = 0                                # number of overlapping ranges
max_c = 0
for d, starts_ends in q:
  in_range += starts_ends
  if in_range > max_c:
    part2 = d
    max_c = in_range
print("Part 2:", part2) # Based on a hint, which enabled reducing 3 coordinates to a single distance.