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

s = open('input.txt').read()
lengths = [int(x) for x in s.split(',')]
print("Part 1:", KnotHash().get_l2(lengths))
print("Part 2:", KnotHash().get_hash(s))
