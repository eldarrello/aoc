import math
bits = ''.join([bin(int(i, 16))[2:].zfill(4) for i in open('input.txt').read()])
p = 0
total = 0

def read(n):
    global p
    p += n
    return bits[p - n: p]

def read_packet():
    global total
    total += int(read(3), 2)
    type = int(read(3), 2)
    if type == 4:
        v = ''
        while read(1) == '1':
            v += read(4)
        return int(v + read(4), 2)
    else:
        if read(1) == '0':
            bits_in_sub = int(read(15), 2)
            vs = [read_packet() for i in range(p, p + bits_in_sub) if p < i]
        else:
            vs = [read_packet() for _ in range(int(read(11), 2))]
        return [sum(vs), math.prod(vs), min(vs), max(vs), 0, vs[0] > vs[-1], vs[0] < vs[-1], vs[0] == vs[-1]][type]
print("Part 2:", read_packet())
print("Part 1:", total)