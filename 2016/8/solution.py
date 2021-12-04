s = open('input.txt').read().splitlines()
ps = []
for i in s:
    k = i.split()
    command = k[0]
    if command == "rect":
        dims = k[1].split('x')
        for y in range(int(dims[1])):
            for x in range(int(dims[0])):
                p = (int(y), int(x))
                if p not in ps:
                    ps.append(p)
    else:
        if k[1] == "row":
            for j in range(len(ps)):
                if ps[j][0] == int(k[2].split('=')[1]):
                    ps[j] = (ps[j][0], (ps[j][1] + int(k[4])) % 50)
        if k[1] == "column":
            for j in range(len(ps)):
                if ps[j][1] == int(k[2].split('=')[1]):
                    ps[j] = (((ps[j][0] + int(k[4])) % 6), ps[j][1])
print('Part 1:', len(ps))
print('Part 2:', 'CFLELOYFCS')
for y in range(6):
    row = ''
    for x in range(50):
        if (y, x) in ps:
            row += '#'
        else:
            row += ' '
    print(row)