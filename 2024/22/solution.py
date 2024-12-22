acc = 0
scores = {}
for v in map(int, open('input.txt').read().splitlines()):
    vs = []
    for k in range(2000):
        v ^= v * 64 % 16777216
        v ^= v // 32
        v ^= v * 2048 % 16777216
        vs.append(v % 10)
    dvs = [0] + [vs[i + 1] - vs[i] for i in range(len(vs) - 1)]
    codes_seen = set()
    for i in range(1, len(dvs) - 3):
        code = tuple(dvs[i:i + 4])
        if code not in codes_seen:
            scores[code] = scores[code] + vs[i + 3] if code in scores else vs[i + 3]
            codes_seen.add(code)
    acc += v
print("Part 1:", acc)
print("Part 2:", sorted([(v, k) for k, v in scores.items()], key=lambda x: x[0], reverse=True)[0][0])

