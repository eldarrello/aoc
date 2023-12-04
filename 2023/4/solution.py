acc1 = 0
acc2 = 0
s = open('input.txt').read().splitlines()
copies = [1 for i in s]
for y, l in enumerate(s):
  a, b = l.split(': ')[1].split(' | ')
  w = [int(i) for i in a.split(' ') if i.isnumeric()]
  q = [int(i) for i in b.split(' ') if i.isnumeric()]
  n = sum([1 for i in w if i in q])
  acc1 += int(2 ** (n - 1))
  acc2 += copies[y]
  for i in range(y, y + n):
    copies[i + 1] += copies[y]
print("Part 1:", acc1)
print("Part 2:", acc2)
