s = open('input.txt').read().splitlines()
mm = []
acc = 0
for l in s:
    vs = l.split()
    if vs[0] in "*+":
        for i in range(len(vs)):
            if vs[i] == '*':
                ac = 1
                for k in range(len(mm)):
                  ac *= mm[k][i]
                acc += ac
            else:
                ac = 0
                for k in range(len(mm)):
                  ac += mm[k][i]
                acc += ac
    else:
        mm.append(list(map(int, vs)))
print("Part 1:", acc)
mm = []
acc = 0
maxl = 0
for l in s:
    maxl = max(maxl, len(l))
    if l[0] in "*+":
        for i in range(len(mm)):
            mm[i] = mm[i].ljust(maxl + 1, ' ')
        vs = list(l.ljust(maxl + 1, ' '))

        for i in range(len(vs)):
            if vs[i] == ' ' and i < len(vs) - 1 and vs[i + 1] == ' ':
                vs[i] = vs[i - 1]
        ac = 0
        for i in range(len(vs)):
            op = vs[i]
            if op == ' ':
                acc += ac
                ac = 0
            vv = ''
            for k in range(len(mm)):
              vv += mm[k][i]
            if ac == 0:
                if not vv.isspace():
                    ac = int(vv)
            else:
                ac = eval('ac' + op + vv)
        acc += ac
    else:
        mm.append(l)
print("Part 2:", acc)

