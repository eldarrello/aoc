s = open('input.txt').read().splitlines()
s = s[0]
s = list(s[::-1])

def inc():
    for i in range(len(s)):
        k = ord(s[i])
        k += 1
        if k > ord('z'):
            s[i] = 'a'
        else:
            s[i] = chr(k)
            break
def validate():
    pprev = '?'
    prev = '?'
    pairs = 0
    pair_pos = -1
    straight = False
    for i in range(len(s)):
        if s[i] in "iol": return False
        if s[i] == prev and i - pair_pos > 1:
            pairs += 1
            pair_pos = i
        if ord(pprev) == ord(prev) + 1 and ord(prev) == ord(s[i]) + 1:
            straight = True
        pprev = prev
        prev = s[i]
    return straight and pairs > 1
while validate() == False:
    inc()
print('Part 1:', ''.join(s[::-1]))
inc()
while validate() == False:
    inc()
print('Part 2:', ''.join(s[::-1]))
