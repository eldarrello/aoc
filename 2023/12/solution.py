def eval(a, p, l, b, visited):
    c = 0
    for i in range(p, len(a) - l):
        if a[i:i + l].count('.') == 0 and a[i + l] != '#':
            if not b:
                c += 1 if a[i + l:].count('#') == 0 else 0
            else:
                key = str(i + l + 1) + '-' + '-'.join(map(str, b))
                if key not in visited:
                    visited[key] = eval(a, i + l + 1, b[0], b[1:], visited)
                c += visited[key]
        if a[i] == '#':
            break
    return c

def run(expand):
    acc = 0
    for k, l in enumerate(s):
        a, b = l.split()
        a, b = expand(a, list(map(int, b.split(','))))
        acc += eval(a, 0, b[0], b[1:], {})
    return acc

s = open('input.txt').read().splitlines()
print("Part 1:", run(lambda a, b: (a + '.', b)))
print("Part 2:", run(lambda a, b: (a + '?' + a + '?' + a + '?' + a + '?' + a + '.', b + b + b + b + b)))