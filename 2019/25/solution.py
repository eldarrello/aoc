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

import random

class Droid:
    def __init__(self):
        self.cpu = CPU(Memory(load()))
        self.output = []
        self.input = []
        self.path = []
        self.coms = []
        self.direction = None
        self.map = {}
        self.xy = (0, 0)
        self.output_id = 0
        self.items = []
        self.combs = []
        self.all_items_collected = False

    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
        out = ''.join(self.output)
        print(out)

    def input_handler(self):
        if len(self.input) == 0:
            #print('miss')
            return 0
        return self.input.pop(0)

    def output_handler(self, s):
        self.output.append(chr(s))
        #print(''.join(self.output))
        if chr(s) == '?':
            print('output', self.output_id)
            self.output_id += 1
            out = ''.join(self.output)
            kt = out.splitlines()
            if kt[-1] != 'Command?':
                return
            if "Navigation" in out:
                r = 0
            new_spot = False
            print(out)
            #made move successfully?
            if "==" in out:
                if self.direction != None and "ejected" not in out:
                    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
                    self.xy = (self.xy[0] + moves[self.direction][0], self.xy[1] + moves[self.direction][1])
                new_spot = not (self.xy in self.map)
                self.map[self.xy] = out
                print('pos:', self.xy, new_spot)
            else:
                self.output.clear()
                return
            have_items = out.split('Items here:\n- ')
            if len(have_items) > 1:
                item = have_items[1].split('\n')[0]
                #nope = ["mug", "giant electromagnet", "escape pod", "photons", "molten lava", "infinite loop"]
                nope = ["giant electromagnet", "escape pod", "photons", "molten lava", "infinite loop"]
                if item not in nope:
                    self.take(item)
                    self.inv()
            if "Security Checkpoint" in out and self.all_items_collected:
                if len(self.combs) == 0:
                    self.prepare_combs()
                self.set_comb()
            coms = []
            dirs = ["north", "south", "east", "west"]

            if 'password' in out:
                print('--------------PASSWORD--------------')
            for i in dirs:
                if i in out:
                    coms.append(dirs.index(i))
            if new_spot:
                self.path.append(self.coms)
                if self.direction != None:
                    opposite = self.direction ^ 1
                    if opposite in coms:
                        coms.remove(opposite)
                        coms.append(opposite)
                self.coms = coms
            if len(self.coms) == 0:
                if len(self.path) > 0:
                    self.coms = self.path.pop()
                    if len(self.coms) == 0:
                        self.all_items_collected = True
                        print('All maze done, go to second round')
                        self.coms = coms
                        self.map = {}
            if len(self.coms):
                while True:
                    if len(self.combs):
                        self.direction = self.coms[0]      #lock it to checkpoint until can go through
                    else:
                        self.direction = self.coms.pop(0)
                    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
                    xy = (self.xy[0] + moves[self.direction][0], self.xy[1] + moves[self.direction][1])
                    if xy in self.map and len(self.coms) > 0:
                        print('loop')
                        #continue
                        del self.map[xy]
                    self.make_move()
                    break
            self.output.clear()

    def make_move(self):
        dirs = ["north", "south", "east", "west"]
        for i in dirs[self.direction]:
            self.input.append(ord(i))
        print('attemting to move', dirs[self.direction])
        self.input.append(10)

    def take(self, item):
        for i in "take ":
            self.input.append(ord(i))
        for i in item:
            self.input.append(ord(i))
        print('attemting to take', item)
        self.items.append(item)
        self.input.append(10)

    def drop(self, item):
        for i in "drop ":
            self.input.append(ord(i))
        for i in item:
            self.input.append(ord(i))
        self.items.remove(item)
        self.input.append(10)

    def inv(self):
        for i in "inv\n":
            self.input.append(ord(i))

    def prepare_combs(self):
        self.combs = []
        for l in range(1, len(self.items) + 1):
            for subset in itertools.combinations(self.items, l):
                self.combs.append(subset)

    def set_comb(self):
        if len(self.combs):
            comb = self.combs.pop(0)
            items = self.items.copy()
            for i in items:
                self.drop(i)
            for i in comb:
                self.take(i)
        else:
            print('done with comb')
import itertools

Droid().run()
