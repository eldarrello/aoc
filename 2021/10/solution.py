s = open('input.txt').read().splitlines()
part_1 = 0
part_2 = []
for i in s:
    o = []
    for k in i:
        if k in '([{<':
            o.append(k)
        elif k != {'{': '}', '[': ']', '<': '>', '(': ')'}[o.pop()]:
            part_1 += {')': 3, ']': 57, '}': 1197, '>': 25137}[k]
            break
    else:
        n = 0
        for k in o[::-1]:
            n = n * 5 + ['(', '[', '{', '<'].index(k) + 1
        part_2.append(n)
print("Part 1:", part_1)
print("Part 2:", sorted(part_2)[len(part_2) // 2])

