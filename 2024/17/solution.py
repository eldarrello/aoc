def run(a):
    regs = [a, 0, 0]
    out = []
    i = 0
    while i in range(len(code) - 1):
        op, v = code[i:i + 2]
        comb = regs[v - 4] if v >= 4 else v
        if op == 0:
            regs[0] = regs[0] // 2 ** comb
        elif op == 1:
            regs[1] ^= code[i + 1]
        elif op == 2:
            regs[1] = comb % 8
        elif op == 3:
            if regs[0]:
                i = code[i + 1] - 2
        elif op == 4:
            regs[1] ^= regs[2]
        elif op == 5:
            out.append(comb % 8)
        elif op == 6:
            regs[1] = regs[0] // 2 ** comb
        elif op == 7:
            regs[2] = regs[0] // 2 ** comb
        i += 2
    return out
s = open('input.txt').read().splitlines()
code = list(map(int, s[-1].split()[1].split(',')))
print("Part 1:", ','.join(map(str, run(int(s[0].split()[2])))))
n = len(code) * 3 - 2
b = n
nodes = [(2 ** b, b - 1)]
while nodes:
    a, b = nodes.pop(0)
    c = (n - b - 9)
    if c > 3:
        c //= 3
        if run(a)[-c:] != code[-c:]:
            continue
    if b > 0:
        nodes.append((a + 2 ** b, b - 1))
        nodes.append((a, b - 1))
    else:
        if run(a + 1) == code:
            print("Part 2:", a + 1)
