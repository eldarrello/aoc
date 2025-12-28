ss = open('input.txt').read().split("\n\n")
acc = 0
for s in ss[-1].splitlines():
    area, counts = s.split(': ')
    w, h = map(int, area.split('x'))
    counts = sum(map(int, counts.split()))
    if 3 * 3 * counts <= w * h:             # Insight is that the shapes can be ignored and all can be treated as taking 3x3 space
        acc += 1
print("Part 1:", acc)
