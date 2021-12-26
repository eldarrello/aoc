def move_2(p1, p2, s1, s2, d, u):
    for dp, du in [(9, 1), (8, 3), (7, 6), (6, 7), (5, 6), (4, 3), (3, 1)]:
        np = (p1 + dp - 1) % 10 + 1
        ns = s1 + np
        if ns < 21:
            move_2(p2, np, s2, ns, d + 1, u * du)
        else:
            w[d % 2] += u * du
def move_1(p1, p2, s1, s2, n, d):
        np = (p1 + sum([d := d % 100 + 1 for i in range(3)]) - 1) % 10 + 1
        ns = s1 + np
        if ns < 1000:
            move_1(p2, np, s2, ns, n + 3, d)
        else:
            print("Part 1:", (s2 * (n + 3)))
move_1(3, 7, 0, 0, 0, 0)
w = [0, 0]
move_2(3, 7, 0, 0, 0, 1)
print("Part 2:", max(w))
