import math
s = open('input.txt').read().replace('(', '').replace(')', '').replace('=', '').replace(',', '').splitlines()
m = {i.split()[0]:i.split()[1:] for i in s[2:]}

def search(next):
    steps = []
    i = 0
    while len(steps) < 2:
        next = m[next][0 if s[0][i % len(s[0])] == 'L' else 1]
        i += 1
        if next[2] == 'Z':
            steps.append(i)
    return steps[0], steps[1] - steps[0]

print("Part 1:", search('AAA')[0])
print("Part 2:", math.lcm(*[search(key)[1] for key in [i for i in m.keys() if i[2] == 'A']]))
