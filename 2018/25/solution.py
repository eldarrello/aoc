def is_in_group(group, j):
    for i in group:
        if abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]) + abs(i[3] - j[3]) <= 3:
            return True
    return False
m = []
for s in open('input.txt').read().splitlines():
    m.append(list(map(int, s.split(','))))
groups = []
while m:
    i = m.pop(0)
    new_group = [i]
    collapsed_groups = []
    for group in groups:
        if is_in_group(group, i):
            new_group += group
            collapsed_groups.append(group)
    for i in collapsed_groups:
        groups.remove(i)
    groups.append(new_group)
print("Part 1:", len(groups))

