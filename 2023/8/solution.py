def search(next):
    i = 0
    while next[2] != 'Z':
        next = m[next][0 if s[0][i % len(s[0])] == 'L' else 1]
        i += 1
    return i
import math
s = open('input.txt').read().replace('(', '').replace(')', '').replace('=', '').replace(',', '').splitlines()
m = {i.split()[0]:i.split()[1:] for i in s[2:]}
print("Part 1:", search('AAA'))
print("Part 2:", math.lcm(*[search(key) for key in [i for i in m.keys() if i[2] == 'A']]))
