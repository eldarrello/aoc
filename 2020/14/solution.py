s = open('input.txt').read().splitlines()
def decode(a, mask):
    ads = [''.join(['1' if a[i] == '1' and mask[i] == '0' else mask[i] for i in range(0, 36)])]
    for i in range(2 << ads[0].count('X')):
        d = ads.pop(0)
        ads.append(d.replace('X', '0', 1))
        ads.append(d.replace('X', '1', 1))
    return [int(x, 2) for x in ads]
def run(part):
    m = {}
    for i in s:
        a, b = i.split(' = ')
        if a == 'mask':
            mask = b
        else:
            if part == 1:
                m[int(a[4:-1])] = int(b) & int(mask.replace('X', '1'), 2) | int(mask.replace('X', '0'), 2)
            else:
                m = {**m, **{x: int(b) for x in decode(str(bin(int(a[4:-1])))[2:].zfill(36), list(mask))}}
    print("Part {}:".format(part), sum(m.values()))
run(1)
run(2)