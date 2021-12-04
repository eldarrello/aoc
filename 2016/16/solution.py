def rep(s):
    k = s.replace('1', 'A')
    k = k.replace('0', '1')
    k = k.replace('A', '0')
    return s + '0' + k[::-1]

def check_sum(s):
    cs = []
    for index in range(0, len(s), 2):
        t = s[index: index + 2]
        cs.append('1' if t[0] == t[1] else '0')
    return ''.join(cs)

def eval(s, n):
    while len(s) < n:
        s = rep(s)
    s = s[:n]
    while len(s) % 2 == 0:
        s = check_sum(s)
    return s

s = '11011110011011101'
print("Part 1:", eval(s, 272))
print("Part 2:", eval(s, 35651584))
