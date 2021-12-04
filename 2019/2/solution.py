def process(s):
    ip = 0
    while s[ip] != 99:
        if s[ip] == 1:
           s[s[ip + 3]] = s[s[ip + 1]] + s[s[ip + 2]]
        elif s[ip] == 2:
           s[s[ip + 3]] = s[s[ip + 1]] * s[s[ip + 2]]        
        ip += 4
    return s
        
def load():
    with open("input.txt") as f:
        s = f.read().split(',')
    s = [int(a) for a in s]
    return s
i = 0
while True:
    s = load()
    s[1] = i % 100
    s[2] = i / 100
    s = process(s)
    if s[0] == 19690720:
        print((i % 100) * 100 + (i / 100))
        break
    
    i += 1

