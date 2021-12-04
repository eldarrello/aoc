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

    def run(self, input=lambda: 0, output=lambda x: 0):
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
            else:
                break

        def terminate(self):
            self.terminate = True

def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    return [int(a) for a in s]

def draw(map):
    # print("\033[0;0H")
    min_x = sorted(map)[0][0]
    max_x = sorted(map, reverse=True)[0][0]
    min_y = sorted(map, key=lambda i: i[1])[0][1]
    max_y = sorted(map, key=lambda i: i[1], reverse=True)[0][1]
    for y in range(min_y, max_y + 1):
        print(''.join([map[(x,y)] if (x,y) in map else '?' for x in range(min_x, max_x + 1)]))

class Drone:
    def __init__(self):
        self.code = load()
        self.input = []
        self.output = []

    def run_1(self):
        for y in range(50):
            for x in range(50):
                self.input.append(y)
                self.input.append(x)
                self.cpu = CPU(Memory(self.code))
                self.cpu.run(self.input_handler, self.output_handler)
        print("Affected point count:", self.output.count(1))

    def run_2(self, n):
        x = 0
        for y in range(n, 10000):
            for i in range(10000):
                self.input.append(y)
                self.input.append(x + i)
                self.cpu = CPU(Memory(self.code))
                self.cpu.run(self.input_handler, self.output_handler)
                if self.output.pop() == 1:
                    break
            x += i
            self.input.append(y - n)
            self.input.append(x + n)
            self.cpu = CPU(Memory(self.code))
            self.cpu.run(self.input_handler, self.output_handler)
            if self.output.pop() == 1:
                print('Ship cordinates', x * 10000 + y - n)
                break

    def input_handler(self):
        return self.input.pop()

    def output_handler(self, s):
        self.output.append(s)

Drone().run_1()
Drone().run_2(99)
