s = open('input.txt').read().splitlines()
def do(d, skip):
    x = 0
    count = 0
    for t, i in enumerate(s):
        if skip and t % 2 == 0:
            continue
        if i[x] == '#':
            count += 1
        x = (x + d) % len(s[0])
    return count
print("Part 1:", do(3, False))
acc = do(1, True)
for i in [1, 3, 5, 7]:
    acc *= do(i, False)
print("Part 2:", acc)
