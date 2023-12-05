s = open('input.txt').read().splitlines()
maps = []

for y, l in enumerate(s + ['']):
  if ':' in l:
    m = []
    if 'seeds' in l:
      seeds = list(map(int, l.split(': ')[1].split()))
    continue
  if l == '':
    if len(m):
      maps.append(m)
  else:
    m.append(list(map(int, l.split())))

def eval(s):
  for mm in maps:
    for m in mm:
      if s >= m[1] and s <= m[1] + m[2]:
        s = m[0] + s - m[1]
        break
  return s

print("Part 1:", min([eval(i) for i in seeds]))

pairs = []
for i in range(len(seeds) // 2):
  pairs.append((seeds[i * 2], seeds[i * 2 + 1]))

best = 999999999999
for j, (start, n) in enumerate(pairs):
  prev = -1
  step = 1000
  for k in range(0, n, step):     # coarse search
    v = eval(start + k)
    if v != prev + step and v != prev + 2 * step:
      for i in range(step):       # fine search
        best = min(best, eval(start + k - step + i))
    prev = v
print("Part 2:", best)


