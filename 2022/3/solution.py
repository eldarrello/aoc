s = open('input.txt').read().splitlines()
p = {chr(ord('A') + i + k): i + j for i in range(26) for k, j in ((32, 1), (0, 27))}
print("Part 1:", sum([p[list(set(i[:len(i) // 2]).intersection(i[len(i) // 2:]))[0]] for i in s]))
print("Part 2:", sum([p[list(set(s[i]).intersection(s[i + 1]).intersection(s[i + 2]))[0]] for i in range(0, len(s), 3)]))