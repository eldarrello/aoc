def get_priority(a):
    y = ord(a)
    return y - ord('A') + 27 if y <= ord('a') else y - ord('a') + 1

s = open('input.txt').read().splitlines()
print("Part 1:", sum([get_priority(list(set(i[:len(i) // 2]).intersection(i[len(i) // 2:]))[0]) for i in s]))
print("Part 2:", sum([get_priority(list(set(s[i]).intersection(s[i + 1]).intersection(s[i + 2]))[0]) for i in range(0, len(s), 3)]))