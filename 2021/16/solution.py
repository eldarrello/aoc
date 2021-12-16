import math
s = open('input.txt').read()
bits = ''.join([bin(int(i, 16))[2:].zfill(4) for i in s])
p = 0
total = 0

def read(n):
    global p
    v = bits[p: p + n]
    p += n
    return v

def read_packet():
    global total
    total += int(read(3), 2)
    type = int(read(3), 2)
    if type == 4:
        v = ''
        while(True):
            bs = read(5)
            v += (bs[1:])
            if bs[0] == '0':
                break
        return int(v, 2)
    else:
        values = []
        ind = read(1)
        if ind == '0':
            bits_in_sub = int(read(15), 2)
            start = p
            while p < start + bits_in_sub:
                values.append(read_packet())
        else:
            number_of_subs = int(read(11), 2)
            for i in range(number_of_subs):
                values.append(read_packet())
        if type == 0:
            return sum(values)
        elif type == 1:
            return math.prod(values)
        elif type == 2:
            return min(values)
        elif type == 3:
            return max(values)
        elif type == 5:
            return 1 if values[0] > values[1] else 0
        elif type == 6:
            return 1 if values[0] < values[1] else 0
        elif type == 7:
            return 1 if values[0] == values[1] else 0

print("Part 2:", read_packet())
print("Part 1:", total)