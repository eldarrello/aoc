m = {}
for s in open('input.txt').read().split('\n\n'):
    lines = s.splitlines()
    if len(lines) == 2:
        state = lines[0].split()[3].strip('.')
        n = int(lines[1].split()[5])
        continue
    key = lines[0].strip(':').split()[2]
    values = []
    for i in range(1, len(lines)):
        line = lines[i]
        line = line.strip(':').strip('.')
        line = line.replace('left', '-1').replace('right', '1')
        values.append(line.split()[-1])
    m[key] = values
values = {}
pos = 0
for i in range(n):
    if pos in values and values[pos] == 1:
        l = m[state][4:]
    else:
        l = m[state][:4]
    values[pos] = int(l[1])
    pos += int(l[2])
    state = l[3]
print("Part 1:", sum(values.values()))

