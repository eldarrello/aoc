s = open('input.txt').read()
bs = [i // 2 for i in range(0, len(s), 2) for k in range(int(s[i]))]
print("Part 1:", sum([i * v for i, v in enumerate([bs.pop(-1 if i % 2 else 0) for i, v in enumerate(s) for k in range(int(v)) if len(bs)])]))
p = 0
ss = [(0, int(s[0]), 0)] + [(p := p + int(s[i - 1]), int(s[i]), i // 2 if i % 2 == 0 else 0) for i in range(1, len(s))]
for i, (p, bl, id) in enumerate(reversed(ss)):
    if i % 2 == 0:
        for j, (pos, fl, _) in enumerate(ss):
            if pos < p and fl >= bl and j % 2 == 1:
                ss[len(ss) - i - 1] = (pos, bl, id)
                ss[j] = (pos + bl, fl - bl, 0)
                break
print("Part 2:", sum([(p + k) * id for p, bl, id in ss for k in range(bl)]))