import hashlib
s = open('input.txt').read().splitlines()
password_1 = []
password_2 = [' ' for x in range(8)]
for i in range(1000000000):
    ss = s[0] + str(i)
    result = hashlib.md5(ss.encode())
    p = result.hexdigest()
    if p[:5] == '00000':
        print(p)
        if len(password_1) < 8:
            password_1.append(p[5:6])
        offset = ord(p[5:6]) - ord('8')
        if offset < 8 and password_2[offset] == ' ':
            password_2[offset] = p[6:7]
            print('Part 2:', ''.join(password_2))
        if ' ' not in password_2:
            break
print('Part 1:', ''.join(password_1))
print('Part 2:', ''.join(password_2))
