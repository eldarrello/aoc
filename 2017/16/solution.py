s = open('input.txt').read()
s = s.split(',')
base = [chr(x) for x in range(ord('a'), ord('p') + 1)]
p = [chr(x) for x in range(ord('a'), ord('p') + 1)]
def dance():
    global p
    for i in s:
        if 's' in i:
            n = int(i[1:])
            p = p[-n:] + p[:-n]
        elif 'x' in i:
            ws = i[1:].split('/')
            a = int(ws[0])
            b = int(ws[1])
            p[a], p[b] = p[b], p[a]
        else:
            ws = i[1:].split('/')
            a = p.index(ws[0])
            b = p.index(ws[1])
            p[a], p[b] = p[b], p[a]
dance()
print("Part 1:", ''.join(p))
for i in range(1, 1000000000):
    if p == base:
        n = 1000000000 % i
        for i in range(n):
            dance()
        print("Part 2:", ''.join(p))
        exit()
    dance()
