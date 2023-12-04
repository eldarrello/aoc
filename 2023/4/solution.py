acc = 0
s = open('input.txt').read().splitlines()
copies = [1 for i in s]
for y, l in enumerate(s):
  a, b = l.split(': ')[1].split(' | ')
  w = [int(i) for i in a.split()]
  q = [int(i) for i in b.split()]
  n = sum([1 for i in w if i in q])
  acc += int(2 ** (n - 1))
  for i in range(y, y + n):
    copies[i + 1] += copies[y]
print("Part 1:", acc)
print("Part 2:", sum(copies))
