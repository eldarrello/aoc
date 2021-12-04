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
    
import random

def draw(map):
    #print("\033[0;0H")
    min_x = sorted(map)[0][0]
    max_x = sorted(map, reverse = True)[0][0]
    min_y = sorted(map, key=lambda i: i[1])[0][1]
    max_y = sorted(map, key=lambda i: i[1], reverse = True)[0][1]
    map[(0, 0)] = 'X'
    for y in range(min_y, max_y + 1):
        print(''.join([map[(x, y)] if (x, y) in map else ' ' for x in range(min_x, max_x + 1)]))

class Maze:
    def __init__(self):
        self.output = []
        self.cpu = CPU(Memory(load()))
        self.map = {}
        self.xy = (0, 0)
        self.command = 0
        self.commands = self.get_commands()
        self.path = []
        self.max = 0
        self.find_o = True

    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
       
    def input_handler(self):
        if len(self.commands) == 0:
            print('Time to fill', self.max)
            return 0
        self.command = self.commands.pop(0)
        return self.command + 1
    
    def output_handler(self, s):
        xy = self.get_move()
        if s == 0:
            self.map[xy] = '#'            
        else:
            self.xy = xy
            self.map[xy] = 'O' if s == 2 else ' '
            if len(self.path) > 1 and self.path[-2][0] == xy:
                self.commands = self.path.pop()[1]                   
            else:
                self.path.append((xy, self.commands))
                if len(self.path) > self.max:
                    self.max = len(self.path)
                self.commands = self.get_commands()
                if s == 2 and self.find_o:
                    print('Path to oxygen', len(self.path), 'steps')
                    self.path = []
                    self.max = 0
                    self.find_o = False
                
    def get_move(self):
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        return (self.xy[0] + moves[self.command][0], self.xy[1] + moves[self.command][1])
        
    def get_commands(self):
        m = [0,1,2,3]
        o = [1,0,3,2]
        last = o[self.command]
        m.remove(o[self.command])
        m.append(last)
        return m

Maze().run()    
