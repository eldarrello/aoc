s = open('input.txt').read().splitlines()
def eval(d):
    acc = 0
    for l in s:
        first = ''
        for n in d:
            l = l.replace(n, n[0] + str(d.index(n) + 1) + n[1:])
        for i in range(len(l)):
            if (l[i].isnumeric()):
                if first == '':
                    first = l[i]
                last = l[i]
        acc += int(first + last)
    return acc
print("Part 1:", eval([]))
print("Part 2:", eval(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']))