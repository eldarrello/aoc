s = open('input.txt').read().splitlines()
t = int(s[0])
s = s[1].split(',')
bs = []
o = []
for i in range(len(s)):
    if s[i].isnumeric():
        bs.append(int(s[i]))
        o.append(i)
k = [bs[i] - t % bs[i] for i in range(len(bs))]
print("Part 1:", bs[k.index(min(k))] * min(k))

#external code taken from https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8
from functools import reduce
def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod//n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod
def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

print("Part 2:", chinese_remainder(bs, [bs[i] - o[i] % bs[i] for i in range(len(bs))]))