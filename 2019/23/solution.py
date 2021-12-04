class Memory:
    def __init__(self, code):
        self.m = {}
        for i in range(len(code)):
            self.m[i] = code[i]

    def load(self, address):
        if address in self.m:  # print('load_s', address, self.m[address])
            return self.m[address]
        else:  # print('load_0', address, 0)
            return 0

    def store(self, address, value):  # print('store', address, value)
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

    def arg(self, value=None):
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

    def tick(self, input=lambda: 0, output=lambda x: 0):
        arg = self.arg
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
        else:
            return False
        return True

        def run(self, input=lambda: 0, output=lambda x: 0):
            while self.tick(input, output):
                pass

def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]

class Comp:
    def __init__(self, address, i, o):
        self.cpu = CPU(Memory(load()))
        self.output = []
        self.address = address
        self.i = i
        self.o = o

    def run(self):
        self.cpu.tick(self.input_handler, self.output_handler)

    def input_handler(self):
        return self.i(self.address)

    def output_handler(self, s):
        self.output.append(s)
        if len(self.output) == 3:
            self.o(self.output)
            self.output.clear()

class Net:
    def __init__(self):
        self.packets = {}
        self.comp = []
        self.xy = (-1, -1)
        self.prev_sent_xy = (-1, -1)
        self.data_in_queue = 0
        self.input_counter_since_last = 0
        self.done = False
        for i in range(50):
            self.comp.append(Comp(i, self.input_handler, self.output_handler))
            self.packets[i] = [i]
            self.data_in_queue += 1

    def add_packet(self, address, xy):
        self.data_in_queue += 2
        self.packets[address].append(xy[0])
        self.packets[address].append(xy[1])

    def input_handler(self, address):
        self.input_counter_since_last += 1
        if len(self.packets[address]):
            self.data_in_queue -= 1
            return self.packets[address].pop(0)
        else:
            if self.data_in_queue == 0:
                if self.xy != (-1, -1) and self.input_counter_since_last > 1000:
                    if self.prev_sent_xy == self.xy:
                        print('Part 2 Y', self.xy[1])
                        self.done = True
                    self.prev_sent_xy = self.xy
                    self.add_packet(0, self.xy)
                    self.input_counter_since_last = 0
            return -1

    def output_handler(self, s):
        if s[0] == 255:
            if self.xy == (-1, -1):
                print('Part 1 Y', s[2])
            self.xy = (s[1], s[2])
            return
        self.add_packet(s[0], (s[1], s[2]))

    def run(self):
        while not self.done:
            for i in range(len(self.comp)):
                self.comp[i].run()

Net().run()