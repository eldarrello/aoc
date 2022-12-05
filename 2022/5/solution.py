def eval(part):
    s = open('input.txt').read().splitlines()
    z = range((len(s[0]) + 1) // 4)
    m = [[] for i in z]
    for line in s:
        if '[' in line:
            for i in z:
                v = line[4 * i + 1]
                if v != ' ':
                    m[i].insert(0, v)
        elif 'move' in line:
            _, n, _, s, _, d = line.split(' ')
            s = int(s) - 1
            d = int(d) - 1
            n = int(n)
            m[d] += m[s][-n:][::part]
            m[s] = m[s][:len(m[s]) - n:]
    return ''.join([m[i][-1] for i in z])
print("Part 1:", eval(-1))
print("Part 2:", eval(1))