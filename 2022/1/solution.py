acc = sorted([sum([int(i) for i in x]) for x in [x.split('\n') for x in open('input.txt').read().split('\n\n')]])
print("Part 1:", acc[-1])
print("Part 2:", sum(acc[-3:]))