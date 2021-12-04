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
    self.terminate = False
    
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
    while not self.terminate:
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

    def terminate(self):
        self.terminate = True
            
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]

class Maze:
    def __init__(self):
        self.cpu = CPU(Memory(load()))
        self.command = 0
        self.commands = [0, 1, 2, 3]
        self.path = []
        self.max = 0
        self.find_o = True

    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
       
    def input_handler(self):
        if len(self.commands) == 0:
            print('Time to fill', self.max)
            return 0
        self.command = self.commands.pop()
        return self.command + 1
    
    def output_handler(self, s):
        if s == 0: return
        if len(self.path) > 0 and len(self.commands) == 0:
            self.commands = self.path.pop()                  
        else:
            self.path.append(self.commands)
            self.max = max(self.max, len(self.path))    
            self.commands = [self.command ^ 1 + x for x in [0, 1, 2, -1]]
            if s == 2 and self.find_o:
                print('Path to oxygen', len(self.path), 'steps')
                self.path = []
                self.max = 0
                self.find_o = False

Maze().run()    
