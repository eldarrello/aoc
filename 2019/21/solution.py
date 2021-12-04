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

class Droid:
    def __init__(self):
        self.code = load()
        self.input = []
        self.output = []

    def send_command(self, cmd):
        for i in cmd:
            self.input.append(ord(i))
        self.input.append(10)

    def run(self, part_2):
        self.send_command('NOT A T')
        self.send_command('OR T J')
        self.send_command('NOT B T')
        self.send_command('OR T J')
        self.send_command('NOT C T')
        self.send_command('OR T J')
        self.send_command('AND D J')
        if part_2:
            #clear T
            self.send_command('NOT A T')
            self.send_command('AND A T')
            #look forward to postpone jump not to land in hole
            self.send_command('OR E T')
            self.send_command('OR H T')
            self.send_command('AND T J')
            self.send_command('RUN')
        else:
            self.send_command('WALK')
        CPU(Memory(self.code)).run(self.input_handler, self.output_handler)
        #print(''.join(self.output))

    def input_handler(self):
        return self.input.pop(0)

    def output_handler(self, s):
        if s > 200:
            print('Hull damage:', s)
        else:
            self.output.append(chr(s))

Droid().run(False)
Droid().run(True)
