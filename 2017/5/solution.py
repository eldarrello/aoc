def do(part):
    s = open('input.txt').read().splitlines()
    s = [int(x) for x in s]
    i = 0
    steps = 0
    while i < len(s):
        d = s[i]
        if part == 2 and d > 2:
            s[i] -= 1
        else:
            s[i] += 1
        i += d
        steps += 1
    print("Part {}:".format(part), steps)
do(1)
do(2)
