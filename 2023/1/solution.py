def eval(d):
    acc = 0
    for l in open('input.txt').read().splitlines():
        for i, n in enumerate(d):
            l = l.replace(n, n[0] + str(i + 1) + n[1:])
        ds = [c for c in l if c.isdigit()]
        acc += int(ds[0] + ds[-1])
    return acc
print("Part 1:", eval([]))
print("Part 2:", eval(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))