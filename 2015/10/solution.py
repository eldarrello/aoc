s = open('input.txt').read().splitlines()
s = s[0]
def do():
    prev = '?'
    c = 1
    t = []
    for i in range(len(s)):
        v = s[i]
        if v == prev:
            c += 1
        elif i > 0:
            t.append(str(c))
            t.append(prev)
            c = 1
        prev = v
    t.append(str(c))
    t.append(prev)
    return t
for k in range(40):
    s = do()
print('Part 1:', len(s))
for k in range(10):
    s = do()
print('Part 2:', len(s))
