class KnotHash:
    n = 256

    def __init__(self):
        self.pos = 0
        self.skip = 0
        self.l = [x for x in range(self.n)]

    def get_hash(self, str):
        lengths = [ord(x) for x in str] + [17, 31, 73, 47, 23]
        for i in range(64):
            self.__apply(lengths)
        hex = ''
        for i in range(16):
            acc = 0
            for k in range(16):
                acc ^= self.l[i * 16 + k]
            hex += '{:02x}'.format(acc)
        return hex

    def get_l2(self, lengths):
        self.__apply(lengths)
        return self.l[0] * self.l[1]

    def __reverse(self, lst, start, end):
        tmp = lst + lst
        tmp[start:end] = tmp[start:end][::-1]
        extra = end - self.n
        if extra > 0:
            return tmp[self.n: self.n + extra] + tmp[extra:self.n]
        return tmp[:self.n]

    def __apply(self, lengths):
        for i in lengths:
            self.l = self.__reverse(self.l, self.pos, self.pos + i)
            self.pos = (self.pos + i + self.skip) % self.n
            self.skip += 1

map = set()
for y in range(128):
    s = 'oundnydw-' + str(y)
    hash = KnotHash().get_hash(s)
    t = str(bin(int(hash, 16))[2:].zfill(128))
    for x, v in enumerate(t):
        if v == '1':
            map.add((x, y))
print("Part 1:", len(map))

def get_moves(xy):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = []
    for i in d:
        x = xy[0] + i[0]
        y = xy[1] + i[1]
        if (x, y) in map:
            map.remove((x, y))
            moves.append((x, y))
    return moves

groups = 0
while len(map):
    xy = map.pop()
    groups += 1
    moves = get_moves(xy)
    while moves:
        move = moves.pop(0)
        moves += get_moves(move)
print("Part 2:", groups)
