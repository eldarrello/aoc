def snake(cs):
  x = 0
  y = 0
  s = []
  for c in cs:
      d = int(c[1:])
      if c[:1] == 'D':
          for i in range(d):
              s.append(tuple([y, x]))
              y += 1
      elif c[:1] == 'U':
          for i in range(d):
              s.append(tuple([y, x]))
              y -= 1
      elif c[:1] == 'L':
          for i in range(d):
              s.append(tuple([y, x]))
              x -= 1
      elif c[:1] == 'R':
          for i in range(d):
              s.append(tuple([y, x]))
              x += 1
  return s
  
with open("input.txt") as fp:
   l1 = snake(fp.readline().split(','))
   l2 = snake(fp.readline().split(','))
   for i in l1:
       if l2.count(i) != 0:
           print(i, l1.index(i) + l2.index(i))
