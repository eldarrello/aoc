def compare(l, r):
    for i in range(len(l)):
        if i == len(r):
            return -1
        il = l[i]
        ir = r[i]
        if type(il) != list and type(ir) != list:
            d = ir - il
            if d:
                return d
        else:
            if type(ir) != list:
                ir = [ir]
            elif type(il) != list:
                il = [il]
            result = compare(il, ir)
            if result != 0:
                return result
    return 0 if len(r) == len(l) else 1
s = open('input.txt').read().split('\n\n')
acc = 0
m = []
for i in range(len(s)):
    m += s[i].splitlines()
    acc += (i + 1) if compare(eval(m[-2]), eval(m[-1])) > 0 else 0
print("Part 1:", acc)
import functools
m = sorted([eval(i) for i in m] + [[[2]], [[6]]], key=functools.cmp_to_key(compare), reverse = True)
print("Part 2:", (m.index([[2]]) + 1) * (m.index([[6]]) + 1))
