s = open('input.txt').read().splitlines()
sizes = []
path = []
for i in s:
    ii = i.split()
    if len(ii) == 3:
        if ii[2] == '..':
            sizes.append(path[-1])
            path[-2] += path[-1]
            path.pop()
        else:
            path.append(0)
    elif ii[0].isnumeric():
            path[-1] += int(ii[0])
print("Part 1:", sum([i for i in sizes + path if i <= 100000]))
print("Part 2:", [i for i in sorted(sizes) if i + 40000000 >= sum(path)][0])