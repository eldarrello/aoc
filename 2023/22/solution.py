def compress(bs):
    cnt = 0
    bb = []
    for i, b in enumerate(bs):
        top_z = 0
        for a in reversed(bb):
            if not (a[3] < b[0] or a[0] > b[3] or a[4] < b[1] or a[1] > b[4]):
                top_z = a[5]
                break
        dz = max(0, b[2] - top_z - 1)
        cnt += 1 if dz > 0 else 0
        bb.append((b[0], b[1], b[2] - dz, b[3], b[4], b[5] - dz))
        bb.sort(key=lambda x: x[5])
    return bb, cnt
bs = compress(sorted([tuple(map(int, i.replace('~', ',').split(','))) for i in open('input.txt').read().splitlines()], key=lambda x: x[2]))[0]
cnts = [compress(bs[:i] + bs[i + 1:])[1] for i in range(len(bs))]
print("Part 1:", cnts.count(0))
print("Part 2:", sum(cnts))

