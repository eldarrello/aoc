s = open('input.txt').read()
total = 0
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        total += int(s[i])
if s[-1] == s[0]:
    total += int(s[0])
print("Part 1:", total)
total = 0
for i in range(len(s)):
    if s[i] == s[(i + len(s) // 2) % len(s)]:
        total += int(s[i])
print("Part 2:", total)