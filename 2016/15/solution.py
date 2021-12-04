def eval(s):
    p = []
    n = []
    e = []
    for i in range(len(s)):
        words = s[i].split(' ')
        n.append(int(words[3]))
        p.append(int(words[11].strip('.')))
        end = n[-1] - 1 - i
        while end < 0:
            end += n[-1]
        e.append(end)
    t = 0
    while p != e:
        for i in range(len(p)):
            p[i] += 1
            if p[i] >= n[i]:
                p[i] = 0
        t += 1
    return t
s = open('input.txt').read().splitlines()
print("Part 1:", eval(s[0:-1]))
print("Part 2:", eval(s))
