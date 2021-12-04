s = open('input.txt').read().splitlines()

def prepare():
    map = {}
    ops = []
    for i in s:
        a, b = i.split('->')
        a = a.strip()
        a = a.split(' ')
        b = b.strip()
        if len(a) == 1:
            map[b] = int(a[0]) if a[0].isdigit() else a[0]
        elif len(a) == 2:
            ops.append(("not", a[1], b))
        else:
            if a[0].isdigit():
                a[0] = int(a[0])
            ops.append((a[1], a[0], a[2], b))
    return map, ops

def wire():
    while len(ops):
        #reduce ops
        for i in ops:
            if isinstance(i[1], int):
                a = i[1]
            elif i[1] not in map: continue
            else:
                a = map[i[1]]
            if not isinstance(a, int): continue
            if len(i) == 3:
                map[i[2]] = ~a
                if map[i[2]] < 0:
                    map[i[2]] += 65536
                ops.remove(i)
                break
            else:
                if i[0] == "RSHIFT":
                    result = a >> int(i[2])
                    map[i[3]] = result
                    ops.remove(i)
                    break

                elif i[0] == "LSHIFT":
                    result = a << int(i[2])
                    map[i[3]] = result
                    ops.remove(i)
                    break

                if i[2] not in map: continue
                b = map[i[2]]
                if not isinstance(b, int):continue
                if i[0] == "AND":
                    result = a & b
                elif i[0] == "OR":
                    result = a | b
                map[i[3]] = result
                ops.remove(i)
                break
        #reduce map
        for k, v in map.items():
            if not isinstance(v, int):
                if v in map:
                    if isinstance(map[v], int):
                        map[k] = map[v]

map, ops = prepare()
wire()
part_1 = map['a']
print('Part 1:', part_1 )
map, ops = prepare()
map['b'] = part_1
wire()
print('Part 2:', map['a'])