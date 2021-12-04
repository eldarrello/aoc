s = open('input.txt').read()
garbage = False
skipNext = False
count = 0
depth = 0
garbage_count = 0
for i in s:
    if skipNext:
        skipNext = False
        continue
    if i == '!':
        skipNext = True
        continue
    if i == '>':
        garbage = False
        continue
    if garbage:
        garbage_count += 1
        continue
    if i == '<':
        garbage = True
        continue
    if i == '{':
        depth += 1
        count += depth
    if i == '}':
        depth -= 1
print("Part 1:", count)
print("Part 2:", garbage_count)

