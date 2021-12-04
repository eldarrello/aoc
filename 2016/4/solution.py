s = open('input.txt').read().splitlines()

def check(s, n):
    chars = [char for char in s]
    for i in range(len(chars)):
        chars[i] = chr(ord('a') + (ord(chars[i]) - ord('a') + n) % 26)
    if ''.join(chars) == "object":
        print('Part 2:', n)

sum = 0
for i in s:
    l = {}
    ls = i.split('-')
    id = int(ls[-1].split('[')[0])
    for k in ls:
        check(k, id)
    for k in "".join(ls[:-1]):
        if k not in l:
            l[k] = 1
        else:
            l[k] += 1
    sum += id
    last_count = -1
    last_letter = ''
    for k in ls[-1].split('[')[1][:-1]:
        if k in l:
            if last_count == -1 or l[k] < last_count or (l[k] == last_count and (last_letter == '' or k > last_letter)):
                if l[k] < last_count:
                    last_letter = ''
                last_count = l[k]
                last_letter = k
                continue
        sum -= id
        break
print('Part 1:', sum)
