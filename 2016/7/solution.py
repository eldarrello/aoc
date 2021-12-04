s = open('input.txt').read().splitlines()
tls_count = 0
ssl_count = 0
for i in s:
    chars = list(i)
    balance = 0
    tls = 0
    for k in range(len(chars)):
        if chars[k] == '[':
            balance += 1
            continue
        if chars[k] == ']':
            balance -= 1
            continue
        if k > 2 and chars[k] == chars[k - 3] and chars[k - 1] == chars[k - 2] and chars[k] != chars[k - 1]:
            if balance > 0:
                tls = 0
                break
            else:
                tls = 1
    tls_count += tls
    balance = 0
    aba = []
    bab = []
    for k in range(len(chars)):
        if chars[k] == '[':
            balance += 1
            continue
        if chars[k] == ']':
            balance -= 1
            continue
        if k > 1 and chars[k] == chars[k - 2]:
            if balance == 0:
                aba.append(''.join([chars[k - 1], chars[k], chars[k - 1]]))
            else:
                bab.append(''.join([chars[k - 2], chars[k - 1], chars[k]]))
    for i in aba:
        if i in bab:
            ssl_count += 1
            break
print('Part 1:', tls_count)
print('Part 2:', ssl_count)