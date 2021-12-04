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
        print(''.join([map[(x, y)] if (x, y) in map else ' ' for x in range(min_x, max_x + 1)]))

class Maze:
    def __init__(self, map):
        self.map = map
        self.input = []
        self.code = load()
        if len(map) > 0:
            self.code[0] = 2
            self.input = self.get_commands()
        self.cpu = CPU(Memory(self.code))
        self.cros = {}
        self.xy = (0,0)

    def run(self):
        self.cpu.run(self.input_handler, self.output_handler)
        draw(self.map)
        if self.code[0] == 2: return
        c = 0
        for i in self.cros:
            c += self.cros[i]
        print('crosses:', c)
        return self.map

    def input_handler(self):
        if len(self.input):
            return self.input.pop(0)
        return 0

    def output_handler(self, s):
        if s > 120:
            print('Colleted dust:', s)
            return
        if s == 10:
            self.xy = (0, self.xy[1] + 1)
            return
        self.xy = (self.xy[0] + 1, self.xy[1])
        self.map[self.xy] = chr(s)
        x = self.xy[0]
        y = self.xy[1]
        if self.code[0] == 2: return
        if s == 35 and x > 3 and y > 1 and self.map[(x - 1,y)] == '#' and self.map[(x - 2, y)] == '#' and self.map[(x - 1, y - 1)] == '#':
            self.cros[x - 2, y] = (x - 2) * y

    def get_move(self, xy, dir):
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        return (xy[0] + moves[dir][0], xy[1] + moves[dir][1])

    def has_path(self, xy):
        return xy in self.map and self.map[xy] != '.'

    def get_count_in_direction(self, xy, dir):
        c = 0
        for i in range(100):
            t_xy = self.get_move(xy, dir)
            if self.has_path(t_xy):
                c += 1
                xy = t_xy
            else:
                break
        old_dir = dir
        n_moves=[(2, 3), (2, 3), (0, 1), (0, 1)]
        if self.has_path(self.get_move(xy, n_moves[dir][0])):
            dir = n_moves[dir][0]
        elif self.has_path(self.get_move(xy, n_moves[dir][1])):
            dir = n_moves[dir][1]
        else:
            dir = -1
        r_turns = [(0,3),(1,2),(2,0),(3,1)]
        l_turns = [(0,2),(1,3),(2,1),(3,0)]
        if (old_dir, dir) in r_turns:
            turn = ord('R')
        elif (old_dir, dir) in l_turns:
            turn = ord('L')
        else:
            turn = ''
        return (xy, c, dir, turn)

    def get_commands(self):
        id = ['^', 'v', '<', '>']
        a = []
        for xy, v in self.map.items():
            if v in id:
                dock = xy
                dir = id.index(v)
                #todo::initial turn
                a += [ord('L')]
                dir = 2
        xy = dock

        while dir >= 0:
            [xy, c, dir, turn] = self.get_count_in_direction(xy, dir)
            a += [c]
            a += [turn]
        a.pop()
        print(a)
        sub_count = 0
        subs = [[], [], []]
        main = []
        base = 0
        while base < len(a):
            found = []
            breakout = False
            for i in range(sub_count):
                k = len(subs[i])
                if subs[i] == a[base:base + k]:
                    base += k
                    main += [65 + i]
                    breakout = True
                    break
            if breakout: continue
            for k in range(6, 9, 2):        #todo::9 is probably cheating here, instead search existing subs in base chunk to stop earlier
                for i in range(base + k + 1, len(a) - k):
                    if a[base:base + k] == a[i:i + k]:
                        found.append((k,i))
            if len(found):
                [k, i] = found.pop()
            else:
                f = 1
            subs[sub_count] = a[base:base + k]
            main += [65 + sub_count]
            sub_count += 1
            base += k
        c = []
        for i in main:
            c += [i]
            c += [ord(',')]
        c.pop()
        c += [10]
        for i in range(3):
            for j in range(len(subs[i])):
                v = subs[i][j]
                if v < 76:
                    [p, q] = divmod(v, 10)
                    if p > 0:
                        c += [ord('0') + p]
                    c += [ord('0') + q]
                else:
                    c += [v]
                c += [ord(',')]
            #print ('sub', subs[i])
            c.pop()
            c += [10]
        print('commands', ''.join([chr(x) for x in c]))
        print(c)
        c += [ord('n')]
        c += [10]
        return c

m = Maze({}).run()
Maze(m).run()
