def get_row(s):
    row = []
    row.append('^' if s[:2] in ['^^', '.^'] else '.')
    for i in range(1,len(s) - 1):
        k = s[i - 1:i + 2]
        row.append('^' if s[i - 1:i + 2] in ['^..','^^.','.^^','..^'] else '.')
    row.append('^' if s[-2:] in ['^^', '^.'] else '.')
    return ''.join(row)
s = open('input.txt').read().splitlines()[0]
count = s.count('.')
for i in range(400000 - 1):
    s = get_row(s)
    count += s.count('.')
    if i == 38:
        print("Part 1:", count)
print("Part 2:", count)
