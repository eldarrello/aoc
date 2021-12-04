def run(n):
    t = {17: 0, 1: 1, 3: 2, 16: 3, 19: 4}
    last = 0
    for i in range(len(t), n - 1):
        d = i - t[last] if last in t else 0
        t[last] = i
        last = d
    return last
print("Part 1:", run(2020))
print("Part 2:", run(30000000))
