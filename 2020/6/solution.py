s = open('input.txt').read().splitlines()
g = []
gs = []
s += ['']
for i in s:
    if i == '':
        gs.append(g)
        g = []
        continue
    g.append(i)
count_1 = 0
count_2 = 0
for i in gs:
    h = set()
    for k in i:
        for j in k:
            h.add(j)
    count_1 += len(h)
    for c in range(ord('a'), ord('z') + 1):
        for k in i:
            if chr(c) not in k:
                break
        else:
            count_2 += 1
print("Part 1:", count_1)
print("Part 2:", count_2)
'''
Based on idea from Reddit:
s = sum([0x10000 * len(set.intersection(*map(set, group.split('\n')))) + len(set(group.replace('\n', ''))) for group in open('input.txt').read().split('\n\n')])
print("Part 1:{}\nPart 2:{}".format(s & 0xffff, s >> 16))
'''