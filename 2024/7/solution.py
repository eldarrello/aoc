def eval(part):
    acc = 0
    for ss in [list(map(int, ss.replace(':', '').split())) for ss in open('input.txt').read().splitlines()]:
        nodes = [(ss[1], ss[2:])]
        while nodes:
            v, vs = nodes.pop()
            if len(vs):
                nodes.append((v * vs[0], vs[1:]))
                nodes.append((v + vs[0], vs[1:]))
                if part:
                    nodes.append((int(str(v) + str(vs[0])), vs[1:]))
            else:
                if v == ss[0]:
                    acc += ss[0]
                    break
    return acc
print("Part 1:", eval(False))
print("Part 2:", eval(True))

