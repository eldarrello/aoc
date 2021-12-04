def run(n):
    s = [0,4,5,8,7,3,2,6,9,1]
    cur = 5
    if n > 100:
        s[2] = 10
        s += [i + 1 for i in range(len(s), 1000000)] + [cur]
    for _ in range(n):
        dest = cur - 1
        while dest in [s[cur], s[s[cur]], s[s[s[cur]]], 0]:
            dest = dest - 1 if dest > 1 else max(s)
        r2 = s[s[s[cur]]]
        s[cur], s[r2], s[dest] = s[r2], s[dest], s[cur]
        cur = s[cur]
    i = 1
    return ''.join([i := str(s[int(i)]) for _ in range(8)]), s[1] * s[s[1]]
print("Part 1:", run(100)[0])
print("Part 2:", run(10000000)[1])