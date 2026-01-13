s = open("input.txt").read().splitlines()
p = 2019
for i in s:
    m = i.split(' ')
    if m[0] == 'cut':
        p -= int(m[1])
    elif m[1] == 'with':
        p *= int(m[3])
    elif m[1] == 'into':
        p = -p - 1
    p %= 10007
print('Part 1:', p)
#todo:: fully understand part 2
'''
Reference (possibly the ideal) implementation for part 2:

def solve(c, n, p, o = 0, i = 1):
    inv = lambda x: pow(x, c - 2, c)
    for s in [s.split() for s in open('input.txt').readlines()]:
        if s[0] == 'cut':  o += i * int(s[-1])
        if s[1] == 'with': i *= inv(int(s[-1]))
        if s[1] == 'into': o -= i; i *= -1
    o *= inv(1 - i)
    i = pow(i, n, c)
    return (p * i + (1 - i) * o) % c

print('Part 1:', solve(10007, 10005, 2019)) #10005 - repeats after every c
print('Part 2:', solve(119315717514047, 101741582076661, 2020))
'''

