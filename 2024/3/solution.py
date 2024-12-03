def eval(s):
    acc = 0
    for i in s.split('mul('):
        ts = i.split(')')[0].split(',')
        if len(ts) == 2 and ts[0].isnumeric() and ts[1].isnumeric() and len(ts[0]) < 4 and len(ts[1]) < 4:
            acc += int(ts[0]) * int(ts[1])
    return acc
s = open('input.txt').read()
ds = s.split('don\'t()')
print("Part 1:", eval(s))
print("Part 2:", eval(ds[0] + ''.join([''.join(ss.split('do()')[1:]) for ss in ds[1:]])))

