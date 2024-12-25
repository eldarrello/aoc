s = open('input.txt').read().splitlines()
kbd = {'7': (0, 0), '8': (1, 0), '9': (2, 0),'4': (0, 1),'5': (1, 1),'6': (2, 1),'1': (0, 2),'2': (1, 2),'3': (2, 2),'0': (1, 3),'A': (2, 3)}
ctrl = {'<': (0, 1), '>': (2, 1), '^': (1, 0),'v': (1, 1), 'A':(2, 0)}

def transform(input):
    sequence = ''
    x, y = (2, 0)
    for c in input:
        nx, ny = ctrl[c]
        dx = nx - x
        dy = ny - y
        if (x, y) == (1, 0) and (dx, dy) == (-1, 1):
            sequence += 'v<'
        elif (x, y) == (0, 1) and (dx, dy) == (1, -1):
            sequence += '>^'
        else:
            sequence += {(0, 0): '', (-1,0):'<', (1,0):'>', (0,-1):'^', (0, 1):'v', (-1, -1):'<^', (1, 1):'v>', (-1, 1):'<v', (1, -1):'^>', (-2, 1):'v<<', (2, -1):'>>^'}[(dx, dy)]
        sequence += 'A'
        x = nx
        y = ny
    return sequence

def split_transform(sequence, depth):
    acc = 0
    sss = sequence.split('A')
    q = {}
    for ss in sss[:-1]:
        if ss not in q:
            q[ss] = 1
        else:
            q[ss] += 1
    for ss in q.keys():
        sq = ss + 'A'
        for i in range(depth):
            sq = transform(sq)
        acc += len(sq) * q[ss]
    return acc

def run(depth):
    acc = 0
    x = 2
    y = 3

    for i in s:
        sequences = [[]]
        for c in i:
            nx, ny = kbd[c]
            dx = nx - x
            dy = ny - y
            hor = '<' if dx < 0 else '>'
            ver = '^' if dy < 0 else 'v'
            if (x + dx, y) == (0, 3) or dx == 0 or dy == 0:
                for sequence in sequences:
                    sequence += [ver for i in range(abs(dy))] + [hor for i in range(abs(dx))]
            elif (x, y + dy) == (0, 3):
                for sequence in sequences:
                    sequence += [hor for i in range(abs(dx))] + [ver for i in range(abs(dy))]
            else:
                nsequences = []
                for sequence in sequences:
                    nsequences.append(sequence + [hor for i in range(abs(dx))] + [ver for i in range(abs(dy))])
                    nsequences.append(sequence + [ver for i in range(abs(dy))] + [hor for i in range(abs(dx))])
                sequences = nsequences
            x = nx
            y = ny
            for sequence in sequences:
                sequence.append('A')
        sequences = [''.join(i) for i in sequences]
        shortest = 1000000000000000000000000
        for sequence in set(sequences):
            sequence = ''.join(sequence)
            for d in range(depth - 13):
                sequence = transform(sequence)
            u = split_transform(''.join(sequence), min(13, depth))

            if u < shortest:
                shortest = u
        dc = int(i[:3]) * shortest
        acc += dc
    return acc
print("Part 1:", run(2))
print("Part 2:", run(25))
