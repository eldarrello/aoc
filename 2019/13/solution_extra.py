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
    
def draw(map, score):
    print("\033[0;0HScore:", score, ' ')
    min_x = sorted(map)[0][0]
    max_x = sorted(map, reverse = True)[0][0]
    min_y = sorted(map, key=lambda i: i[1])[0][1]
    max_y = sorted(map, key=lambda i: i[1], reverse = True)[0][1]
    chart = [' ', '\u2588', '\u2591', '\u2501', 'O'] #1-wall, 2-block, 3-paddle, 4-ball'\u26AB'
    for y in range(min_y, max_y + 1):
        print(''.join([chart[map[(x, y)]] for x in range(min_x, max_x + 1)]))

from time import sleep
import terminal
 
class Breakout:
    def __init__(self):
        self.map = {}
        self.output = []
        self.control = 0
        self.ball = (0, 0)
        self.paddle = (0, 0)
        self.score = 0
        self.map_complete = False
        code = load()
        code[0] = 2
        self.cpu = CPU(Memory(code))
        self.kb = terminal.KBHit()
        
    def input_handler(self):
        self.map_complete = True
        for i in range(10):
          if self.kb.kbhit():
            key = self.kb.getarrow()      
            if key == 1:
                return 1
            if key == 3:
                return -1
          sleep(0.1)
        return 0#self.control
        
    def output_handler(self, value):      
        self.output.append(value)
        if len(self.output) == 3:
            p = (self.output[0], self.output[1])
            t = self.output[2]
            self.output.clear()
            if p == (-1, 0):
                print('score:', t, ' ')
                self.score = t
                return
            self.map[p] = t
            if t == 3:
                self.paddle = p
            if t == 4:
                self.ball = p
                if self.ball[0] == self.paddle[0]:
                    self.control = 0
                else:
                    self.control = 1 if self.ball[0] > self.paddle[0] else -1
            if self.map_complete:
                draw(self.map, self.score)
            
    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
   
Breakout().run()
'''
moves = [(-1,-1),(-1,1),(1,1),(-1,1)]
move_index = 2
print('blocks', blocks)
while True:
    map[p] = ' '
    next_pos = (p[0] + moves[move_index][0], p[1] + moves[move_index][1])
    if next_pos not in map:
        break    
    if map[next_pos] in ['#', 'P']:
        move_index = (move_index + 1) % 5
        next_pos = (p[0] + moves[move_index][0], p[1] + moves[move_index][1])
    p = next_pos
    if p not in map:
        break
    if map[p] == 'B':
        map[p] = ' '
        move_index = (move_index + 1) % 5
    map[p] = 'O'
    draw(map)
cnt = 0
for i in map.values():
    if i == 'B':
        cnt += 1
print(cnt)
'''


