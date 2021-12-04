def get_size(s, rec):
    d = 0
    while True:
        if '(' in s:
            i = s.index('(')
            d += i
            j = s.index(')')
            marker = ''.join(s[i + 1:j]).split('x')
            length = int(marker[0])
            count = int(marker[1])
            s = s[j + 1:]
            d += count * (len(s[:length]) if not rec else get_size(s[:length], rec))
            s = s[length:]
        else:
            return d + len(s)
ss = list(open('input.txt').read())

print('Part 1:', get_size(ss, False))
print('Part 2:', get_size(ss, True))