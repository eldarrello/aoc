s = open('input.txt').read().splitlines()
r = []
for i in s:
    a, b = i.split('-')
    if a in r:
        print('ups)')
    r.append((int(a), int(b)))
r = sorted(r, key=lambda x: x[0])
allowed = 0
disabled = 0
for i in range(len(r)):
    if r[i][0] > disabled + 1:
        if allowed == 0:
            print("Part 1:", disabled + 1)
        allowed += r[i][0] - (disabled + 1)
    disabled = max(disabled, r[i][1])
print("Part 2:", allowed)
