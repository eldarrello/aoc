import math
bits = ''.join([bin(int(i, 16))[2:].zfill(4) for i in open('input.txt').read()])
p = 0
total = 0

def read(n):
    global p
    p += n
    return int(bits[p - n: p], 2)

def read_packet():
    global total
    total += read(3)
    type = read(3)
    if type == 4:
        v = 0
        while read(1) == 1:
            v = v * 16 + read(4)
        return v * 16 + read(4)
    else:
        if read(1) == 0:
            bits_in_sub = read(15)
            vs = [read_packet() for i in range(p, p + bits_in_sub) if p < i]
        else:
            vs = [read_packet() for _ in range(read(11))]
        return [sum(vs), math.prod(vs), min(vs), max(vs), 0, vs[0] > vs[-1], vs[0] < vs[-1], vs[0] == vs[-1]][type]
print("Part 2:", read_packet())
print("Part 1:", total)