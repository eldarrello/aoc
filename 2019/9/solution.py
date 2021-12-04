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
        else: return
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]

input = [2]
output = []
m = Memory(load())
c = CPU(m)
c.run(input, output)
print(output)