s = [int(x) for x in open('input.txt').read().splitlines()]
print("Part 1:", sum(s))
h = set()
acc = 0
i = 0
while True:
    acc += s[i]
    if acc in h:
        print("Part 2:", acc)
        break
    else:
        h.add(acc)
    i = (i + 1) % len(s)

