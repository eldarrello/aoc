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
     [self.modes, opcode] = divmod(self.m.load(self.ip), 100)
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
                     
  def run(self, input = lambda: 0, output = lambda x: 0):
    arg = self.arg
    while True:
        opcode = self.opcode()
        if opcode == 1:
           arg(arg() + arg())
        elif opcode == 2:
           arg(arg() * arg())
        elif opcode == 3:
           arg(input())
        elif opcode == 4:
           output(arg())
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
        else: break
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]
    
def draw(map):
    min_x = sorted(map)[0][0]
    max_x = sorted(map, reverse = True)[0][0]
    min_y = sorted(map, key=lambda i: i[1])[0][1]
    max_y = sorted(map, key=lambda i: i[1], reverse = True)[0][1]
    for y in range(min_y, max_y + 1):
        print(''.join(['#' if (x, y) in map and map[(x, y)] == 1 else ' ' for x in range(min_x, max_x + 1)]))
    
class Robot:
    def __init__(self):
        self.xy = (0, 0)
        self.init_color = 0      #0 for part_1
        self.output = []
        self.moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.d = 0               #direction pointer into 'moves'
        self.cpu = CPU(Memory(load()))

    def input_handler(self):
        return self.map[self.xy] if self.xy in self.map else self.init_color
    
    def output_handler(self, value):
        self.init_color = 0       
        self.output.append(value)
        if len(self.output) == 2:
            self.map[self.xy] = self.output.pop(0)
            self.d = (self.d - 1 if self.output.pop() == 1 else self.d + 1) % 4
            self.xy = (self.xy[0] + self.moves[self.d][0], self.xy[1] + self.moves[self.d][1])
    def run(self, m):
        self.map = m
        self.cpu.run(self.input_handler, self.output_handler)
        print('Number of painted panels:', len(self.map))

map = {}       
Robot().run(map)
draw(map)
