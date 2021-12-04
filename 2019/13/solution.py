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

class Part_1:
    def __init__(self):
        self.output = []
        self.cpu = CPU(Memory(load()))
        self.blocks = 0
    
    def output_handler(self, value):
        self.init_color = 0       
        self.output.append(value)
        if len(self.output) == 3:
            if self.output[2] == 2:
                self.blocks += 1
            self.output.clear()
            
    def run(self):
        self.cpu.run(None, self.output_handler)
        print('Block count:', self.blocks)
        
class Part_2:
    def __init__(self):
        self.output = []
        code = load()
        code[0] = 2
        self.cpu = CPU(Memory(code))
        self.paddle_x = 0
        self.ball_x = 0
        
    def input_handler(self):
        if self.ball_x == self.paddle_x: return 0
        return 1 if self.ball_x > self.paddle_x else -1

    
    def output_handler(self, value):      
        self.output.append(value)
        if len(self.output) == 3:
            if self.output[0] == -1 and self.output[1] == 0:
                self.score = self.output[2]
            elif self.output[2] == 4:
                self.ball_x = self.output[0]
            elif self.output[2] == 3:
                self.paddle_x = self.output[0]
            self.output.clear()
            
    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
        print('Score:', self.score)

Part_1().run()    
Part_2().run()