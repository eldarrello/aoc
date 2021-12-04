lines = open('input.txt').read().splitlines()
def run(r, i, input, output):
    while True:
        if i < 0 or i >= len(lines):
            return i
        line = lines[i]
        ws = line.split(' ')
        c = ws[0]
        d = ws[1]
        if d.isalpha():
            dv = r[d]
        else:
            dv = int(d)
        if len(ws) > 2:
            s = ws[2]
            if s.isalpha():
                sv = r[s]
            else:
                sv = int(s)
        if c == 'set':
            r[d] = sv
        elif c == 'add':
            r[d] += sv
        elif c == 'mul':
            r[d] *= sv
        elif c == 'mod':
            r[d] %= sv
        elif c == 'snd':
            output.append(dv)
        elif c == 'rcv':
            if len(input):
                r[d] = input.pop(0)
            else:
                return i
        if c == 'jgz' and dv > 0:
            i += sv
        else:
            i += 1
def get_regs():
    r = {}
    for i in range(ord('a'), ord('z') + 1):
        r[chr(i)] = 0
    return r
input = []
output = []
run(get_regs(), 0, input, output)
print("Part 1:", output.pop())
r0 = get_regs()
r1 = get_regs()
r0['p'] = 0
r1['p'] = 1
i0 = 0
i1 = 0
q0 = []
q1 = []
count = 0
while True:
    i0 = run(r0, i0, q0, q1)
    b = len(q0)
    i1 = run(r1, i1, q1, q0)
    d = len(q0) - b
    count += d
    if d == 0:
        break
print("Part 2:", count)
