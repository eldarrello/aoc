def add(a, b):
    s = '[' + a + ',' + b + ']'
    while True:
        ms = p.finditer(s)
        for m in ms:
            left = s[:m.start()]
            if left.count('[') - left.count(']') > 3:
                right = s[m.end():]
                a, b = map(int, re.findall("(\d+)",s[m.start():m.end()]))
                if ps := list(re.finditer("\d+", left)):
                    m = ps[-1]
                    value = int(left[m.start():m.end()]) + a
                    left = left[:m.start()] + str(value) + left[m.end():]
                if ps := list(re.finditer("\d+", right)):
                    m = ps[0]
                    value = int(right[m.start():m.end()]) + b
                    right = right[:m.start()] + str(value) + right[m.end():]
                s = left + '0' + right
                break
        else:
            m = re.search("\d{2,}", (s))
            if not m:
                return s
            v = s[m.start():m.end()]
            vi = int(v)
            s = s.replace(v, '[{},{}]'.format(vi // 2, (vi + 1) // 2), 1)
def mag(s):
    while m := p.search(s):
        a, b = map(int, re.findall("(\d+)", s[m.start():m.end()]))
        s = s[:m.start()] + str(3 * a + 2 * b) + s[m.end():]
    return int(s)
import re, itertools
s = open('input.txt').read().splitlines()
p = re.compile("\[\d+,\d+\]")
t = s[0]
print("Part 1:", mag([t := add(t, s[i]) for i in range(1, len(s))][-1]))
print("Part 2:", max([mag(add(i[0], i[1])) for i in list(itertools.permutations(s, 2))]))