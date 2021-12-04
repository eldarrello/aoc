s = open('input.txt').read()
print(s)
print('Part1:',s.count('(') - s.count(')'))
floor = 0
for i in range(len(s)):
    if s[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print('Part 2:', i + 1)
        break
