acc1 = 0
acc2 = 0
for i, l in enumerate(open('input.txt').read().splitlines()):
    ms = [max([int(i.split(' ')[0]) for i in l[l.index(':') + 2:].replace(';', ',').split(', ') if i.split(' ')[1] == c]) for c in ['red', 'green', 'blue']]
    acc1 += i + 1 if (ms[0] <= 12 and ms[1] <= 13 and ms[2] <= 14) else 0
    acc2 += ms[0] * ms[1] * ms[2]
print("Part 1:", acc1)
print("Part 2:", acc2)