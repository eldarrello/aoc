'''
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
#Own code: Did 1. part and reversion for 2. part using a hint how to apply invmod. Didn't manage to complete iteration problem in part 2.
#todo: fully understand how this a*x + b stuff works
file = "input.txt"
s = open(file).read().splitlines()

def reverse(p, n):
    for i in range(len(s) - 1, -1, -1):
        m = s[i].split(' ')
        if m[0] == 'deal' and m[1] == 'with':
            inc = int(m[3])
            p = p * pow(inc, n - 2, n) % n
        elif m[0] == 'deal' and m[1] == 'into':
            p = n - p - 1
        elif m[0] == 'cut':
            cut = int(m[1])
            if cut < 0:
                cut += n
            if p >= n - cut:
                p = p + cut - n
            else:
                p = p + cut
    return p

#part_1
n = 10007
dec = list(range(n))
for i in s:
    m = i.split(' ')
    if m[0] == 'cut':
        cut = int(m[1])
        dec = dec[cut:] + dec[:cut]
    elif m[1] == 'with':
        inc = int(m[3])
        dec_1 = dec.copy()
        for x in range(n):
            dec_1[(x * inc) % n] = dec[x]
            #dec_1[x] = dec[ x * pow(inc, n - 2, n) % n]
        dec = dec_1.copy()
    elif m[1] == 'into':
        dec = dec[::-1]
    #print(dec)
print('Part 1:', dec.index(2019))
p = 2020
print('result', dec[p])

n = 119315717514047
times = 101741582076661
for i in range(times):
    p = reverse(p, n)
print(p)

#answer
#54168121233945
