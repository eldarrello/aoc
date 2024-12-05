def eval(s):
    return sum([int(ts[0]) * int(ts[1]) for ts in [i.split(')')[0].split(',') for i in s.split('mul(')] if len(ts) == 2 and ts[0].isnumeric() and ts[1].isnumeric() and len(ts[0]) < 4 and len(ts[1]) < 4])
s = open('input.txt').read()
ds = s.split('don\'t()')
print("Part 1:", eval(s))
print("Part 2:", eval(ds[0] + ''.join([''.join(ss.split('do()')[1:]) for ss in ds[1:]])))

