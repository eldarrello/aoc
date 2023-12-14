def get_l():
    return sum([h - y for x in range(w) for y in range(h) if m[x, y] == 'O'])

s = open('input.txt').read().splitlines()
m = {(x, y): s[y][x] for y in range(len(s)) for x in range(len(s[0]))}
w = len(s[0])
h = len(s)
ls = []
for c in range(500):
    for i in range(4):
        for x in range(w):
            for y in range(1, h):
                if m[x, y] == 'O':
                    for n in range(1, y + 1):
                        if m[x, y - n] != '.':
                            n -= 1
                            break
                    m[x, y] = '.'
                    m[x, y - n] = 'O'
        if c + i == 0:
            print("Part 1:", get_l())
        m = {(w - y - 1, x): m[(x, y)] for x in range(w) for y in range(h)}
    ls.append(get_l())
    if ls.count(ls[-1]) == 4:
        c2, c3, c4 = [i for i in range(len(ls)) if ls[i] == ls[-1]][1:]
        q = c3 - c2
        if c4 - c3 == q:
            print("Part 2:", ls[c2 + (1000000000 - c) % q - 1])
            break


