s = open('input.txt').read()
bs = [i // 2 for i in range(0, len(s), 2) for k in range(int(s[i]))]
print("Part 1:", sum([i * v for i, v in enumerate([bs.pop(-1 if i % 2 else 0) for i, v in enumerate(s) for k in range(int(v)) if len(bs)])]))
bs = []
fs = []
p = 0
for i, v in enumerate(s):
    if i % 2 == 0:
        bs.append((p, int(v), i // 2))
    else:
        if (int(v)):
            fs.append((p, int(v)))
    p += int(v)
for i, (p, bl, id) in enumerate(reversed(bs)):
    for j, (pos, fl) in enumerate(fs):
        if pos < p and fl >= bl:
            bs[len(bs) - i - 1] = (pos, bl, id)
            fs[j] = (pos + bl, fl - bl)
            break
print("Part 2:", sum([(p + k) * id for p, bl, id in bs for k in range(bl)]))

