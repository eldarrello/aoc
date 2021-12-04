import datetime
s = open('input.txt').read().splitlines()
events = []
for i in s:
    t, e = i.split('] ')
    t = t.strip('[')
    t = datetime.datetime.strptime(t, "%Y-%m-%d %H:%M")
    events.append((t, e.split()[1]))
events.sort(key = lambda x: x[0])
m = {}
id = None
asleep = None
for i in events:
    if '#' in i[1]:
        id = int(i[1].strip('#'))
    elif i[1] == 'asleep':
        asleep = i[0].minute
    else:
        dur = set(t for t in range(asleep, i[0].minute))
        if id in m:
            m[id].append(dur)
        else:
            m[id] = [dur]
max_hit = 0
max_by_total_asleep = 0
for k, v in m.items():
    total_asleep = 0
    for i in v:
        total_asleep += len(i)
    hist = {}
    for i in range(60):
        for g in v:
            if i in g:
                hist[i] = hist[i] + 1 if i in hist else 1
    for i, j in hist.items():
        if j == max(hist.values()):
            minute = i
    if max(hist.values()) > max_hit:
        max_hit = max(hist.values())
        part2 = k * minute
    if total_asleep > max_by_total_asleep:
        max_by_total_asleep = total_asleep
        part1 = k * minute
print("Part 1:", part1)
print("Part 2:", part2)