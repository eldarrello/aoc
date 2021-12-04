s = open('input.txt').read().splitlines()

def encrypt(k):
    for t in s:
        w = t.split(' ')
        if w[0] == 'swap':
            if w[1] == 'position':
                k = list(k)
                k[int(w[2])], k[int(w[5])] = k[int(w[5])], k[int(w[2])]
                k = ''.join(k)
            else:
                a = k.index(w[2])
                b = k.index(w[5])
                k = list(k)
                k[a] = w[5]
                k[b] = w[2]
                k = ''.join(k)
        elif w[0] == 'rotate':
            if w[1] == 'based':
                i = k.index(w[6])
                n = 1 + i
                if i >= 4:
                    n += 1
                if n > len(k):
                    n -= len(k)
                k = k[-n:] + k[:-n]
            else:
                n = int(w[2])
                if w[1] == 'right':
                    n = -n
                k = k[n:] + k[:n]
        elif w[0] == 'reverse':
            a = int(w[2])
            b = int(w[4])
            k = k[:a] + k[a:b + 1][::-1] + k[b + 1:]
        elif w[0] == 'move':
            a = int(w[2])
            b = int(w[5])
            k = list(k)
            k.insert(b, k.pop(a))
            k = ''.join(k)
    return k
print("Part 1:", encrypt('abcdefgh'))

k = 'fbgdceah'
p = 0
for i in range(225):        #repeats in every 226, so one iteration before full cycle gives reverse of k
    k = encrypt(k)
print("Part 2:", k)

