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
            values = [read_packet() for i in range(p, p + bits_in_sub) if p < i]
        else:
            values = [read_packet() for _ in range(int(read(11), 2))]
        return [sum(values), math.prod(values), min(values), max(values), 0, 1 if values[0] > values[-1] else 0, 1 if values[0] < values[-1] else 0, 1 if values[0] == values[-1] else 0][type]
print("Part 2:", read_packet())
print("Part 1:", total)