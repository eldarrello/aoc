s = open('input.txt').read().splitlines()
scores = {')': 3, ']': 57,'}': 1197,'>': 25137}
m = {'{': '}', '[': ']', '<': '>', '(': ')'}
part_1 = 0
part_2 = []
for i in s:
    o = []
    for k in i:
        if k in m:
            o.append(k)
        else:
            top = o.pop()
            if k != m[top]:
                part_1 += scores[k]
                break
    else:
        n = 0
        for i in o[::-1]:
            n = n * 5 + ['(', '[', '{', '<'].index(i) + 1
        part_2.append(n)
print("Part 1:", part_1)
print("Part 2:", sorted(part_2)[(len(part_2) - 1) // 2])

