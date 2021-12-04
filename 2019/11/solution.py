class Memory:
    def __init__(self, code):
        self.m = {}
        for i in range(len(code)):
            self.m[i] = code[i]
        
    def load(self, address):
        if address in self.m: #print('load_s', address, self.m[address])
            return self.m[address]
        else: #print('load_0', address, 0)
            return 0
    
    def store(self, address, value): #print('store', address, value)
        self.m[address] = value
        
    def debug(self):
        s = []
        for i in range(len(self.m)):
            if i in self.m:
                s.append(self.m[i])
        print(s)
        
class CPU:
  def __init__(self, m):
    self.ip = 0
    self.modes = 0
    self.rel = 0
    self.m = m
    self.r = Memory([])
    
  def opcode(self):
     [self.modes, opcode] = divmod(m.load(self.ip), 100)
     self.ip += 1
     return opcode    
    
  def arg(self, value = None):
      [self.modes, mode] = divmod(self.modes, 10)
      p = self.m.load(self.ip)
      self.ip += 1
      x = self.r if mode == 3 else self.m
      if mode == 2:
         p += self.rel
      if (value == None):
         return p if mode == 1 else x.load(p)
      else:
         x.store(p, value)
                     
  def run(self, input, output):
    arg = self.arg
    while True:
        opcode = self.opcode()
        if opcode == 1:
           arg(arg() + arg())
        elif opcode == 2:
           arg(arg() * arg())
        elif opcode == 3:
           arg(input.pop(0))
        elif opcode == 4:
           output.append(arg())
           return True
        elif opcode == 5:
           self.ip = arg() if arg() != 0 else self.ip + 1
        elif opcode == 6:
           self.ip = arg() if arg() == 0 else self.ip + 1
        elif opcode == 7:
           arg(1 if arg() < arg() else 0)
        elif opcode == 8:
           arg(1 if arg() == arg() else 0)
        elif opcode == 9:
           self.rel += arg()
        else: return False
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]

map = {}
map[(0, 0)] = 1
input = []
output = []
x = 0
y = 0
dx = 0
dy = -1
m = Memory(load())
c = CPU(m)

while True:
    input.append(map[(x, y)])
    if c.run(input, output) == False: break
    if c.run(input, output) == False: break

    map[(x, y)] = output.pop(0)
    d = output.pop()
    if d == 0:
        if dy == -1 and dx == 0:
            dx = -1
            dy = 0
        elif dx == -1 and dy == 0:
            dy = 1
            dx = 0
        elif dy == 1 and dx == 0:
            dx = 1
            dy = 0
        else:
            dx = 0
            dy = -1
    else:
        if dy == -1 and dx == 0:
            dx = 1
            dy = 0
        elif dx == 1 and dy == 0:
            dy = 1
            dx = 0
        elif dy == 1 and dx == 0:
            dx = -1
            dy = 0
        else:
            dx = 0
            dy = -1
    x += dx
    y += dy
    if (x, y) not in map:
        map[(x, y)] = 0

print(len(map))
for y in range(6):
    s = []
    for x in range(41):
        if x == 40 and y == 5: break
        s.append('#' if map[(x + 1, y)] == 1 else ' ')
    print(''.join(s))
