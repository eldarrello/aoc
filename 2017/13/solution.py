s = open('input.txt').read().splitlines()
ds = []
for i in s:
    ws = i.split(': ')
    k = int(ws[0])
    ds.append((k, int(ws[1])))
severity = 0
for d in ds:
    p = 2 * (d[1] - 1)
    if d[0] % p == 0:
        severity += d[0] * d[1]
print("Part 1:", severity)

i = 0
while True:
    caught = False
    for d in ds:
        p = 2 * (d[1] - 1)
        if (i + d[0]) % p == 0:
            caught = True
            break
    if caught == False:
        print("Part 2:", i)
        exit()
    i += 1
