s = open('input.txt').read().splitlines()

def run():
    acc = 0
    t = set()
    i = 1
    while i < len(s):
        if i in t:
            return acc
        t.add(i)
        k = s[i]
        c, v = k.split()
        if c == 'acc':
            acc += int(v)
        if c == 'jmp':
            i += int(v)
        else:
            i += 1
    return -acc

print("Part 1:", run())
for i in range(len(s)):
    ori = s[i]
    c, v = s[i].split()
    if c == 'nop':
        s[i] = 'jmp ' + v
    elif c == 'jmp':
        s[i] = 'nop ' + v
    r = run()
    if r < 0:
        print("Part 2:", -r)
    s[i] = ori

