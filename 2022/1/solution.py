s = open('input.txt').read().splitlines()
acc = [0]
for line in s:
    if line == '':
        acc.append(0)
    else:
        acc[-1] += int(line)
acc.sort()
print("Part 1:", acc[-1])
print("Part 2:", sum(acc[-3:]))