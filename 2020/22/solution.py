p1, p2 = [i.splitlines() for i in open('input.txt').read().split('\n\n')]
p1 = [int(i) for i in p1[1:]]
p2 = [int(i) for i in p2[1:]]
def play(p1, p2, part2):
    state = set()
    p1 = list(tuple(p1))
    p2 = list(tuple(p2))
    while p1 and p2 and tuple(p1) not in state:
        state.add(tuple(p1))
        a = p1.pop(0)
        b = p2.pop(0)
        if part2 and a <= len(p1) and b <= len(p2):
            if play(p1[:a], p2[:b], part2)[0]:
                p1 += [a, b]
            else:
                p2 += [b, a]
        else:
            if a > b:
                p1 += [a, b]
            else:
                p2 += [b, a]
    return p1, sum((len(p1 + p2) - i) * k for i, k in enumerate(p1 + p2))
print("Part 1:", play(p1, p2, False)[1])
print("Part 2:", play(p1, p2, True)[1])
